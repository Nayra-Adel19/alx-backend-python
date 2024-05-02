#!/usr/bin/env python3
""" type-annotated function make_multiplier that takes a float """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier that takes a float """
    return lambda x: x * multiplier
