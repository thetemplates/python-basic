"""
Module root.py
"""

import math


class Roots:
    """
    Description
    -----------
    A class that returns the square root of integer values only.
    """

    def __init__(self) -> None:
        pass

    def exc(self, value: float) -> float:
        """

        :param value: An integer value
        """

        return math.sqrt(value)
