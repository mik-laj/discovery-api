import json

from googleapiclient import discovery as discovery_client
from tqdm import tqdm

NUM_RETRIES: int = 5

def save_json(filename, tracked_service_list):
    with open(filename, 'w') as outfile:
        json.dump(tracked_service_list, outfile, indent=" " * 4, sort_keys=True)


def run_main(args):
    discovery = discovery_client.build("discovery", "v1")

    print(f"Fetching index")

    tracked_service_list = fetch_index(discovery)

    fetch_services(discovery, tracked_service_list)


def fetch_services(discovery, tracked_service_list):
    pbar = tqdm(tracked_service_list)
    for api_service in pbar:
        name = api_service["name"]
        version = api_service["version"]
        pbar.set_description(f"Fetching: {name} {version}")
        fetch_service(discovery, name, version)


def fetch_service(discovery, name: str, version: str):
    api_description = (
        discovery.apis()
            .getRest(
            api=name,
            version=version
        ).execute(num_retries=NUM_RETRIES)
    )
    save_json(f"gen_data/services/{name}_{version}.json", api_description)


def fetch_index(discovery):
    api_service_response = discovery.apis().list().execute()
    api_service_list = [
        api_service
        for api_service in api_service_response['items']
        if api_service["preferred"]
    ]
    tracked_service_list = [
        {
            "title": api_service["title"],
            "version": api_service["version"],
            "name": api_service["name"],
        }
        for api_service in api_service_list
    ]
    tracked_service_list = sorted(tracked_service_list, key=lambda d: (d["name"], d["version"]))
    save_json("gen_data/index.json", tracked_service_list)
    return tracked_service_list
