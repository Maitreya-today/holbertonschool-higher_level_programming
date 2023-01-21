#!/usr/bin/python3
"""Square class is square"""


class square:
    """it's a square with a size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
