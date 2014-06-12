#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Problem:
    Lesson 1. PermMissingElem.

In short:
    Find the missing element in a given permutation.

Result:
    https://codility.com/demo/results/demoQXGA7N-75W/

"""


def solution(A):
    """
    Arithmetic series minus sum of A

    """
    N = len(A) + 1
    sum_of_all = N * (1 + N)/2
    for a in A:
        sum_of_all -= a
    return sum_of_all


if __name__ == "__main__":
    A = [2, 3, 1, 5]
    print 'A =', A
    print 'solution(A) =', solution(A)
