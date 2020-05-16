#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fun(X, Y):
    return X + Y


for t in range(int(input())):
    X, Y = [int(k) for k in input().split()]
    print("Case #{}: {}".format(
        t+1, fun(X, Y)))
