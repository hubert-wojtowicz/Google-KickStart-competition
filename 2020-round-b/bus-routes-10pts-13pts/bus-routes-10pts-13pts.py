def last_chance_day(arrival_day: int, bus_ferquencies: int) -> int:
    last_travel_day = arrival_day
    while bus_ferquencies:
        last_bus = bus_ferquencies.pop()
        last_travel_day = (last_travel_day // last_bus) * last_bus
    return last_travel_day


for i in range(int(input())):
    (N, D) = input().split()
    X = [int(item) for item in input().split()]
    print("Case #{}: {}".format(i + 1, last_chance_day(int(D), X)))
