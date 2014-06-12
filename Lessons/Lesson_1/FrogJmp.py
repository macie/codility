#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Problem:
    Lesson 1. FrogJmp

In short:
    Count minimal number of jumps from position X to Y.

Result:
    https://codility.com/demo/results/demoEU9S2X-PJ6/

"""


def solution(X, Y, D):
    """
    (distance // D)                 number of whole jumps
    + (1 * ((distance % D) > 0))    if remainder of division then add 1

    """
    distance = Y - X
    return (distance // D) + (1 * ((distance % D) > 0))


if __name__ == "__main__":
    X, Y, D = 10, 85, 30
    print 'X =', X
    print 'Y =', Y
    print 'D =', D
    print 'solution(X, Y, D) =', solution(X, Y, D)
