#!/usr/bin/env python3
""" type-annotated function sum_mixed_list which takes a list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ type-annotated function sum_mixed_list which takes """
    return float(sum(mxd_lst))
