#!/usr/bin/env python3
"""Module to sum list of mixed items"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of mxd list"""
    return sum(mxd_lst)
