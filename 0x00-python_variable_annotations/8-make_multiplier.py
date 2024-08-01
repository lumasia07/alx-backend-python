#!/usr/bin/env python3
"""Module that returns a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def times(val: float) -> float:
        """Returns Callable type"""
        return val * multiplier
    return times
