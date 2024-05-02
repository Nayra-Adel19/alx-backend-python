#!/usr/bin/env python3
"""  type-annotated function to_kv that takes a string k """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """  type-annotated function to_kv that takes a string k """
    return (k, v**2)
