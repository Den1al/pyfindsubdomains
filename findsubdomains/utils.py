import re

compress_whitespace_regex = re.compile(r'\s+')


def compress_whitespaces(some_string):
    """ Compresses whitespaces within a given string """
    return compress_whitespace_regex.sub(' ', some_string)


def strip_dict_items(d):
    """ Returns a new dict with stripped values """
    def transform_value(v):
        return compress_whitespaces(v.replace('\r', '').replace('\n', '')).strip()

    return {
        k: transform_value(v)
        for k, v
        in d.items()
    }


def strip_dict_items_decorator(f):
    """ A decorator to returns a new dict with stripped values """
    def _strip_dict_items_decorator(*args, **kwargs):
        return strip_dict_items(f(*args, **kwargs))

    return _strip_dict_items_decorator
