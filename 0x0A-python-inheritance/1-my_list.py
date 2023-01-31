#!/usr/bin/python3
"""My List"""


class MyList(list):
    def print_sorted(self):
        print(sorted(list(self)))
        
    def __lt__(self, other):
        return list(self) < list(other)
