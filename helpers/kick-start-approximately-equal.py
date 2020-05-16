def IsApproximatelyEqual(x, y, epsilon):
    """Returns True if y is within relative or absolute 'epsilon' of x.

    By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?0.
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon
            or -epsilon <= (x - y) / y <= epsilon)


(x, y) = [float(item) for item in input().split()]
print(IsApproximatelyEqual(x, y, 0.00001))
