import json
from copy import deepcopy
from typing import Dict


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


def is_json_equals(left: Dict, right: Dict) -> bool:
    left_str = json.dumps(left, indent=" " * 4, sort_keys=True)
    right_str = json.dumps(right, indent=" " * 4, sort_keys=True)
    return left_str == right_str
