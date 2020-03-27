from typing import NamedTuple, List

from googleapiclient import discovery as discovery_client
from tqdm import tqdm

from discovery_tracker.file_utils import save_json
from discovery_tracker.utils import remove_key, NUM_RETRIES


class TrackedService(NamedTuple):
    title: str
    name: str
    version: str

    def __str__(self):
        return f"{self.name} {self.name} {self.version}"


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
        )
        for discovery_item in discovery_items
    ]
    tracked_service_list = sorted(tracked_service_list, key=lambda d: (d.name, d.version))
    return tracked_service_list


def fetch_service(discovery, tracked_service: TrackedService, remove_description: bool, output_dir: str):
    api_definition = (
        discovery.apis()
        .getRest(
            api=tracked_service.name,
            version=tracked_service.version
        ).execute(num_retries=NUM_RETRIES)
    )
    if 'revision' in api_definition:
        del api_definition['revision']

    if 'etag' in api_definition:
        del api_definition['etag']

    if remove_description:
        api_definition = remove_key(api_definition, "description")
        api_definition = remove_key(api_definition, "enumDescriptions")

    save_json(
        filename=f"{output_dir}/{tracked_service.name}__{tracked_service.version}.json",
        content=api_definition
    )


def cmd_fetch_discovery(args):
    discovery = discovery_client.build("discovery", "v1")

    tracked_service_list = fetch_tracked_services_list(discovery)

    pbar = tqdm(tracked_service_list)
    for tracked_service in pbar:
        pbar.set_description(f"Fetching: {tracked_service}")
        fetch_service(
            discovery, tracked_service,
            remove_description=args.remove_descriptions,
            output_dir=args.output
        )
