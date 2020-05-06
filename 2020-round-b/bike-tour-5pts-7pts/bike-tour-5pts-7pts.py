def count_peaks(heights):
    peaks = 0
    for x, y, z in ((heights[i], heights[i+1], heights[i+2])
                    for i in range(len(heights)-2)):
        if x < y and y > z:
            peaks += 1
    return peaks


for i in range(int(input())):
    N = input()
    heights = [int(elem) for elem in input().split()]
    print("Case #{}: {}".format(i + 1, count_peaks(heights)))
