DIRECTIONS = {"W": (-1, 0), "E": (1, 0), "S": (0, 1), "N": (0, -1)}
MAX_DIM = int(1E9)


def normalize(dimension):
    if dimension > MAX_DIM:
        dimension %= MAX_DIM
    if dimension <= 0:
        dimension = MAX_DIM + dimension
    return dimension


def get_displacement(routine, i=0):
    displ = (0, 0)
    while i < len(routine):
        if routine[i].isdigit():
            m = int(routine[i])
            i += 2  # following char is "("
            ((dw, dh), sr_len) = get_displacement(routine, i)
            displ = tuple(map(sum, zip(displ, (dw * m, dh * m))))
            displ = tuple(map(normalize, displ))
            i = sr_len
        elif routine[i] == ')':
            r = tuple([displ, i])
            return r
        else:
            direction = routine[i]
            step = DIRECTIONS.get(direction, (0, 0))
            displ = tuple(map(sum, zip(displ, step)))
        i += 1
    return (displ, i)


def run(routine, start=(1, 1)):
    (w, h) = start
    ((dw, dh), i) = get_displacement(routine)
    return tuple(map(normalize, (w + dw, h + dh)))


for t in range(int(input())):
    routine = input()
    result = run(routine)
    print("Case #{}: {} {}".format(t + 1, result[0], result[1]))
