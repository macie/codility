#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Problem:
    Lesson 1. TapeEquilibrium.

In short:
    Minimize the value
        | (A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1]) |.

Result:
    https://codility.com/demo/results/demo6S3TW3-EMT/

"""


def solution(A):
    """
    | (a_0 + a_1 + ... + a_{P-1}) − (a_P + a_{P+1} + ... + a_{N−1}) |

    => | sum_{i=0}^{P-1} a_i - sum_{i=P}^{N-1} a_i  |

    => | sum_{i=0}^{P-1} a_i -
            (sum_{i=0}^{N-1} a_i - sum_{i=0}^{P-1} a_i) |

    => | 2 * sum_{i=0}^{P-1} a_i - sum_{i=0}^{N-1} a_i |

    """
    current_sum = 0
    sum_of_all = sum(A)
    min_difference = 100000000  # max possible sum
    del A[-1]  # remove to iterate without last element
    for a in A:
        current_sum += a
        current_difference = abs(2 * current_sum - sum_of_all)
        min_difference = min(min_difference, current_difference)
    return min_difference


if __name__ == "__main__":
    A = [3, 1, 2, 4, 3]
    print 'A =', A
    print 'solution(A) =', solution(A)
