#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import log2
MAX_H = 100000
MAX_W = 100000


def L2F():
    result = [0, 0]  # lg(0!), lg(1!)
    i = 2
    while i <= MAX_H + MAX_W - 2:
        result.append(result[-1] + log2(i))
        i += 1
    return result


def entering_field_probability(w, h):
    return 2 ** (L2F[w + h-2] - L2F[w - 1] - L2F[h - 1] - w - h + 2)


def success_probability(W, H, L, U, R, D):
    success = 0
    while L > 1 and D < H:
        (L, D) = (L - 1, D + 1)
        success += entering_field_probability(L, D)
    while U > 1 and R < W:
        (R, U) = (R + 1, U - 1)
        success += entering_field_probability(R, U)
    return success


L2F = L2F()
for t in range(int(input())):
    W, H, L, U, R, D = [int(k) for k in input().split()]
    print("Case #{}: {}".format(
        t+1, float(success_probability(W, H, L, U, R, D))))
