#!/usr/bin/env python3
"""Module that iterates to return length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a duck typed list"""
    return [(i, len(i)) for i in lst]
