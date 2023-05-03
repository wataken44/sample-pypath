#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" init.py


"""

from library.irrp import IRRP
from modules.input import Input

def main():
    print("this is init.py")

    obj1 = IRRP()
    obj1.say()

    obj2 = Input()
    obj2.say()

if __name__ == "__main__":
    main()
