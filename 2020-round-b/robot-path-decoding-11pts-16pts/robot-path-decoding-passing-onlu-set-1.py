DIRECTIONS = {"W": (-1, 0), "E": (1, 0), "S": (0, 1), "N": (0, -1)}
MAX_DIM = int(1E9)


def normalize(dimension):
    if dimension > MAX_DIM:
        dimension %= MAX_DIM
    if dimension <= 0:
        dimension = MAX_DIM + dimension
    return dimension


def move(position, direction, times):
    (w, h) = DIRECTIONS.get(direction, (0, 0))
    destination = tuple(map(sum, zip(position, (w * times, h * times))))
    return tuple(map(normalize, destination))


def perform(position, routine):
    multipliers = [1]
    i = 0
    while i < len(routine):
        if routine[i].isdigit():
            multipliers.append(int(routine[i]) * multipliers[-1])
            i += 1
        elif routine[i] == ')':
            multipliers.pop()
        else:
            position = move(position, routine[i], multipliers[-1])
        i += 1
    return position


for t in range(int(input())):
    routine = input()
    result = perform((1, 1), routine)
    print("Case #{}: {} {}".format(t + 1, result[0], result[1]))
