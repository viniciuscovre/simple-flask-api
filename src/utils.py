import inflection


def _convert_case(obj, func, *args, **kwargs):
    if isinstance(obj, list):
        return [_convert_case(i, func, *args, **kwargs) for i in obj]

    new_obj = {}

    if isinstance(obj, dict):
        for k, v in obj.items():
            # For any other type as object key (like integers)
            if not isinstance(k, str):
                new_obj[k] = v
                continue

            new_value = _convert_case(v, func, *args, **kwargs)
            new_obj[func(k, *args, **kwargs)] = new_value
    else:
        new_obj = obj

    return new_obj


def to_snake_case(obj):
    return _convert_case(obj, inflection.underscore)


def to_camel_case(obj):
    return _convert_case(obj, inflection.camelize, False)
