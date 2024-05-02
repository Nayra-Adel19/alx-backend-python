#!/usr/bin/env python3
""" Write a type-annotated function sum_list which takes a list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ type-annotated function sum_list which takes list """
    return float(sum(input_list))
