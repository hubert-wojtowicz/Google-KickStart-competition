for t in range(int(input())):
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    max_houses = 0
    for j in range(len(a)):
        if b - a[j] < 0:
            break
        b -= a[j]
        max_houses += 1
    print("case #{}: {}".format(t+1, max_houses))
