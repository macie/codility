#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Problem:
    Lesson 2. PermCheck.

In short:
    Check whether array A is a permutation.

Result:
    https://codility.com/demo/results/demo63426Z-YBE/

"""


def solution(A):
    N = len(A)
    count = [1] * (N+1)
    count[0] = 0
    for i in xrange(N):
        try:
            count[A[i]] = 0
        except IndexError:
            count[0] = 1
    return 1 * (sum(count) == 0)


if __name__ == "__main__":
    A = [4, 1, 3, 2]
    print 'A =', A
    print 'solution(A) =', solution(A)
    B = [4, 1, 3]
    print 'B =', B
    print 'solution(B) =', solution(B)
