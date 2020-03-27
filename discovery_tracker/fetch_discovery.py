import json
from copy import deepcopy
from typing import NamedTuple, List, Tuple, Dict

from googleapiclient import discovery as discovery_client
from tabulate import tabulate
from tqdm import tqdm

from discovery_tracker.constants import API_SHORT_DEFINITION_URL_FORMAT, API_LONG_DEFINITION_URL_FORMAT
from discovery_tracker.file_utils import save_json, save_text, load_json, load_text
from discovery_tracker.git_utils import create_commit
from discovery_tracker.markdown_utils import md_link, md_header
from discovery_tracker.utils import remove_key, NUM_RETRIES


class TrackedService(NamedTuple):
    title: str
    name: str
    version: str
    documentation: str

    def __str__(self):
        return f"{self.title} ({self.name}:{self.version})"


def is_json_equals(left: Dict, right: Dict) -> bool:
    left_str = json.dumps(left, indent=" " * 4, sort_keys=True)
    right_str = json.dumps(right, indent=" " * 4, sort_keys=True)
    return left_str == right_str


def fetch_tracked_services_list(discovery) -> List[TrackedService]:
    print(f"Fetching index")
    api_service_response = discovery.apis().list().execute()
    discovery_items = [
        api_service
        for api_service in api_service_response['items']
        if api_service["preferred"]
    ]
    tracked_service_list = [
        TrackedService(
            title=discovery_item["title"],
            name=discovery_item["name"],
            version=discovery_item["version"],
            documentation=discovery_item["documentationLink"],
        )
        for discovery_item in discovery_items
    ]
    tracked_service_list = sorted(tracked_service_list, key=lambda d: (d.name, d.version))
    return tracked_service_list


def clear_api_definitions(api_definition, remove_description):
    api_definition = deepcopy(api_definition)
    if 'revision' in api_definition:
        del api_definition['revision']
    if 'etag' in api_definition:
        del api_definition['etag']
    if remove_description:
        api_definition = remove_key(api_definition, "description")
        api_definition = remove_key(api_definition, "enumDescriptions")
    return api_definition


def fetch_api_definition(discovery, tracked_service):
    api_definition = (
        discovery.apis()
            .getRest(
            api=tracked_service.name,
            version=tracked_service.version
        ).execute(num_retries=NUM_RETRIES)
    )
    return api_definition


def process_service(discovery, tracked_service: TrackedService, remove_description: bool, output_dir: str):
    filename = f"{output_dir}/{tracked_service.name}__{tracked_service.version}.json"

    api_definition = fetch_api_definition(discovery, tracked_service)
    api_definition = clear_api_definitions(api_definition, remove_description)

    old_api_definitions = load_json(filename)
    if not is_json_equals(old_api_definitions, api_definition):
        save_json(
            filename=filename,
            content=api_definition
        )
        if not remove_description:
            messsage = f"Update API long definitions- {tracked_service}"
        else:
            messsage = f"Update API short definitions - {tracked_service}"
        create_commit(
            message=messsage,
            files=[filename]
        )


def cmd_fetch_apis(args):
    discovery = discovery_client.build("discovery", "v1")

    tracked_service_list = fetch_tracked_services_list(discovery)

    pbar = tqdm(tracked_service_list)
    for tracked_service in pbar:
        pbar.set_description(f"Fetching: {tracked_service}")
        process_service(
            discovery, tracked_service,
            remove_description=args.remove_descriptions,
            output_dir=args.output
        )


def prepare_table(tracked_service_list):
    headers = ["Title", "API", "Links"]
    table_data = prepare_table_data(tracked_service_list)
    table = tabulate(table_data, headers, tablefmt="github")
    return table


def prepare_table_data(tracked_service_list: List[TrackedService]) -> List[Tuple[str, str, str]]:
    table_data: List[Tuple[str, str, str]] = []
    for service in sorted(tracked_service_list, key=lambda d: d.title):
        short_link = md_link("API Short",
                             API_SHORT_DEFINITION_URL_FORMAT.format(service.name, service.version))
        long_link = md_link("API Long", API_LONG_DEFINITION_URL_FORMAT.format(service.name, service.version))
        doc_link = md_link("Doc", service.documentation)

        table_data.append(
            (
                service.title,
                f"{service.name}:{service.version}",
                ", ".join([short_link, long_link, doc_link])
            )
        )
    return table_data


def cmd_fetch_index(args):
    discovery = discovery_client.build("discovery", "v1")

    title = "All services"
    tracked_service_list = fetch_tracked_services_list(discovery)
    if args.only_cloud:
        title = "Google Cloud APIs"
        tracked_service_list = [
            t
            for t in tracked_service_list
            if "cloud.google.com" in t.documentation
        ]

    table = prepare_table(tracked_service_list)
    current_index = md_header(title) + table
    filename = args.output
    old_index = load_text(filename)
    if old_index != current_index:
        save_text(filename, current_index)
        create_commit(
            message=f"Update API Index",
            files=[filename]
        )
