#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_search.py
# @Author: lucas
# @Date  : 3/27/19
# @Desc  :

##
#
# T(n): O(log n)
def binary_search_without_recursion(array, query):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]

        if val == query:
            return mid

        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1

    return None


def binary_search(array, low, high, value):
    if low > high:
        return -1

    mid = (low + high) // 2

    if mid < array[mid]:
        return binary_search(array, low, mid - 1, value)

    elif value > array[mid]:
        return binary_search(array, mid + 1, high, value)

    return mid


def run():
    from pprint import pprint
    array = [1,2,4,6,16,90,345]

    index = binary_search_without_recursion(array,query=90)
    pprint(index)

    index = binary_search(array,low=0,high=len(array)-1,value=90)
    pprint(index)


if __name__ == '__main__':
    run()
