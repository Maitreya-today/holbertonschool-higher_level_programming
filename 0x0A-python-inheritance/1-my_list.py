#!/usr/bin/python3
"""My List"""


class MyList(list):
    """My list print sorted"""
    def print_sorted(self):
        print(sorted(self))
