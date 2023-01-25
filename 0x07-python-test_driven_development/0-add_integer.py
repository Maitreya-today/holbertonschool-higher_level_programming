#!/usr/bin/python3
"""Add integers"""


def add_integer(a, b=98):
    """"Returns sum of a and b""""

	if type(a) != int and type(a) != float:
		raise TypeError("a must be an integer")
	
