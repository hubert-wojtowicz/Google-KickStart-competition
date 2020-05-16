#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import log2
MAX_H = 100000
MAX_W = 100000


def L2F():
    """
    Precompute array lg(0!), lg(1!),..., lg((MAX_H+MAX_W-2)!)
    """
    result = [0, 0]
    i = 2
    while i <= MAX_H + MAX_W - 2:
        result.append(result[-1] + log2(i))
        i += 1
    return result


def entering_field_probability(w, h):
    return 2 ** (L2F[w + h-2] - L2F[w - 1] - L2F[h - 1] - w - h + 2)


def success_probability(W, H, L, U, R, D):
    success = 0.0
    while L > 1 and D < H:
        (L, D) = (L - 1, D + 1)
        success += entering_field_probability(L, D)
    while U > 1 and R < W:
        (R, U) = (R + 1, U - 1)
        success += entering_field_probability(R, U)
    return success


def success_probability_2(W, H, L, U, R, D):
    failure = 0.0
    print("Right top")
    for i in range(R - L + 1):  # go right top edge
        entp = entering_field_probability(L + i, U)
        print("P({}, {})={}".format(L + i, U, entp))
        failure += entp
    print("Left to down")
    for i in range(D - U):  # go down left edge
        entp = entering_field_probability(L, U+i+1)
        print("P({}, {})={}".format(L, U+i+1, entp))
        failure += entp
    return 1-failure


L2F = L2F()
for t in range(int(input())):
    W, H, L, U, R, D = [int(k) for k in input().split()]
    print("Case #{}: {}".format(
        t+1, float(success_probability(W, H, L, U, R, D))))
