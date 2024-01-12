#!/usr/bin/env python3
"""
    type-annotated function sum_list and take a list input_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Args:
            input_list: float numbers

        Return:
            Sum of the float numbers
    """

    result: float = 0

    for x in input_list:
        result += x

    return result
