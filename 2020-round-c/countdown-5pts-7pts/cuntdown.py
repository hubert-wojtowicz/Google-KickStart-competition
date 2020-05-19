#!/usr/bin/env python
# -*- coding: utf-8 -*-

for t in range(int(input())):
    N, K = [int(k) for k in input().split()]
    stack = [int(k) for k in input().split()]
    count = 0
    temp = 0

    while (len(stack) != 0):
        top = stack.pop()
        if (top == 1):
            temp = 1
        elif (top == temp + 1):
            temp += 1
            if (temp == K):
                count += 1
                temp = 0
        else:
            temp = 0

    print("Case #{}: {}".format(t+1, count))
