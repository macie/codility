#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Problem:
    Lesson 2. FrogRiverOne.

In short:
    Find the earliest time when a frog can jump to the other side
    of a river.

Result:
    https://codility.com/demo/results/demoFTZ6VW-UZ4/

"""


def solution(X, A):
    all_minutes = len(A)
    count = [0] * (X + 1)
    sum_of_all = X * (X+1) / 2
    minutes = -1
    for i in xrange(all_minutes):
        if count[A[i]] == 0:
            sum_of_all -= A[i]
            count[A[i]] = 1
        if sum_of_all == 0:
            minutes = i
            break

    return minutes


if __name__ == "__main__":
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    X = 5
    print 'X =', X
    print 'A =', A
    print 'solution(X, A) =', solution(X, A)
