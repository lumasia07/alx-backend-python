#!/usr/bin/env python3
"""Module that returns a tuple from a string & float"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, float(v**2))
