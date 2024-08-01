#!/usr/bin/env python3
"""Module returns key in dict"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Returns key else default"""
    if key in dct:
        return dct[key]
    else:
        return default
