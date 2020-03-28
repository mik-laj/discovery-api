from typing import List, Tuple

from googleapiclient import discovery as discovery_client
from tabulate import tabulate

from discovery_tracker.constants import API_SHORT_DEFINITION_URL_FORMAT, API_LONG_DEFINITION_URL_FORMAT
from discovery_tracker.data_sources.google_discovery import TrackedService, fetch_tracked_services_list
from discovery_tracker.utils.filesystem import load_text, save_text
from discovery_tracker.utils.git import create_commit
from discovery_tracker.utils.markdown import md_link, md_header


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
