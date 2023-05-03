#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" input.py


"""

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../"))

from library.irrp import IRRP


class Input:

    def __init__(self):
        pass
        
    def say(self):
        print("Hello Input!")

if __name__ == "__main__":
    print("this is input.py")

    obj = IRRP()
    obj.say()
