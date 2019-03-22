#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : regular_expression_base.py
# @Author: lucas
# @Date  : 3/21/19
# @Desc  : 


import re
from pprint import pprint


def is_phone_number(phone=None, pattern=r'\d\d\d-\d\d\d-\d\d\d\d'):
    if not phone:
        return False
    pattern = re.compile(pattern)
    mo = pattern.match(phone)
    if not mo:
        return
    return mo.group()


def do_pattern(text=None, pattern=r'(.*) are (.*?) .*'):
    if not text:
        return
    match_obj = re.match(pattern, text, re.M | re.I)

    if match_obj:
        print("match_obj.group()  : ", match_obj.group())
        print("match_obj.group(1) : ", match_obj.group(1))
        print("match_obj.group(2) : ", match_obj.group(2))
    else:
        print("No match!")


def run():
    pprint(is_phone_number('my phone number is: 123-121-4567'))
    pprint(is_phone_number('hello, are Elon Musk? This\'s 123-131-4508'))
    do_pattern(text="We are the champions!")


if __name__ == '__main__':
    run()
