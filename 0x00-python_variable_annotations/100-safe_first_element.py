#!/usr/bin/env python3
"""Module returns first element in a list"""
from typing import Sequence, Any, Union 


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element if list"""
    if lst:
        return lst[0]
    else:
        return None
