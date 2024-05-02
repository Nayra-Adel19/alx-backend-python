#!/usr/bin/env python3
""" Augment the following code with the correct duck-typed """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Augment the following code with the correct duck-typed """
    if lst:
        return lst[0]
    else:
        return None
