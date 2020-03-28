from typing import NamedTuple, List

from discovery_tracker.constants import DISCOVERY_NUM_RETRIES


class TrackedService(NamedTuple):
    title: str
    name: str
    version: str
    documentation: str

    def __str__(self):
        return f"{self.title} ({self.name}:{self.version})"


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


def fetch_api_definition(discovery, tracked_service):
    api_definition = (
        discovery.apis()
            .getRest(
            api=tracked_service.name,
            version=tracked_service.version
        ).execute(num_retries=DISCOVERY_NUM_RETRIES)
    )
    return api_definition
