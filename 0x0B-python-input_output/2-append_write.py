#!/bin/usr/python3
"""Append string and return num of chars added"""


def append_write(filename="", text=""):
    """"appends string at end of text file (UTF8)
    and returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
