#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
MAX_SUM = int(1E7)


def test_set(N, A, ps):
    P = [0] * (2*MAX_SUM+1)
    P[-MAX_SUM] += 1
    res, s, msum = (0, 0, 0)
    for i in range(N):
        s += A[i]
        if msum > s:
            msum = s
        k = 0
        while ps[k] <= s-msum:
            res += P[s+MAX_SUM-ps[k]]
            k += 1
        P[s+MAX_SUM] += 1
    return res


ps = [i*i for i in range(int(MAX_SUM ** 0.5))]
for t in range(int(input())):
    N = int(input())
    A = [int(k) for k in input().split()]

    print("Case #{}: {}".format(t+1, test_set(N, A, ps)))
