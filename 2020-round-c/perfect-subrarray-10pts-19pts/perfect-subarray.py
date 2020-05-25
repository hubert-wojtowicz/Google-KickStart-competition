#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
MAX_SUM = int(1E7)


def test_set(N, A, ps):
    res = [0] * N
    P = defaultdict(lambda: 0)
    msum = 0
    s = 0
    P[0] += 1
    for i in range(N):
        s += A[i]
        if msum > s:
            msum = s
        k = 0
        while s-msum >= 0 and ps[k] <= s-msum:
            res[i] += P[s - ps[k]]
            k += 1
        P[s] += 1

    return sum(res)


ps = [i*i for i in range(int(MAX_SUM ** 0.5))]
for t in range(int(input())):
    N = int(input())
    A = [int(k) for k in input().split()]

    print("Case #{}: {}".format(t+1, test_set(N, A, ps)))
