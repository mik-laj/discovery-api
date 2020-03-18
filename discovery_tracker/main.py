import json
from copy import deepcopy

from googleapiclient import discovery as discovery_client
from tqdm import tqdm

NUM_RETRIES: int = 5


def save_json(filename, content):
    with open(filename, 'w') as outfile:
        json.dump(content, outfile, indent=" " * 4, sort_keys=True)


def run_main(args):
    discovery = discovery_client.build("discovery", "v1")

    tracked_service_list = fetch_index(discovery)

    fetch_services(discovery, tracked_service_list)


def fetch_services(discovery, tracked_service_list):
    pbar = tqdm(tracked_service_list)
    for api_service in pbar:
        name = api_service["name"]
        version = api_service["version"]
        pbar.set_description(f"Fetching: {name} {version}")
        fetch_service(discovery, name, version)


def remove_key(obj, key):
    def _walk_recursive(_inner_obj):
        if _inner_obj is None:
            pass
        if isinstance(_inner_obj, list):
            for o in _inner_obj:
                _walk_recursive(o)
        if isinstance(_inner_obj, dict):
            if key in _inner_obj:
                del _inner_obj[key]
            for o in _inner_obj.values():
                _walk_recursive(o)

    result = deepcopy(obj)
    _walk_recursive(result)
    return result


def fetch_service(discovery, name: str, version: str):
    api_definition = (
        discovery.apis()
        .getRest(
            api=name,
            version=version
        ).execute(num_retries=NUM_RETRIES)
    )
    if 'revision' in api_definition:
        del api_definition['revision']
    if 'etag' in api_definition:
        del api_definition['etag']

    save_json(
        filename=f"gen_data/services/{name}__{version}.json",
        content=api_definition
    )
    api_definition_without_descriptions = remove_key(api_definition, "description")
    api_definition_without_descriptions = remove_key(api_definition_without_descriptions, "enumDescriptions")

    save_json(
        filename=f"gen_data/services_without_descriptions/{name}__{version}.json",
        content=api_definition_without_descriptions
    )


def fetch_index(discovery):
    print(f"Fetching index")
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
    return tracked_service_list
