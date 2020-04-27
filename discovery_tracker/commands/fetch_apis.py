from copy import deepcopy

from googleapiclient import discovery as discovery_client
from googleapiclient.errors import HttpError
from tqdm import tqdm

from discovery_tracker.data_sources.google_discovery import TrackedService, fetch_api_definition, \
    fetch_tracked_services_list
from discovery_tracker.utils.filesystem import load_json, save_json
from discovery_tracker.utils.git import create_commit
from discovery_tracker.utils.primitives import remove_key, is_json_equals


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
        try:
            process_service(
                discovery, tracked_service,
                remove_description=args.remove_descriptions,
                output_dir=args.output
            )
        except HttpError as e:
            if e.resp['status'] == '404' or e.resp['status'] == '403':
                print(e)
            else:
                raise
