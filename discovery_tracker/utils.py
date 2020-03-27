from copy import deepcopy


NUM_RETRIES: int = 5


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



