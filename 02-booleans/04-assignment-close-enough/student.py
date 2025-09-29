# write your code here

def close_enough(x, y):
    epsilon = 0.1

    if x == y:
        return True

    return abs(x - y) <= epsilon
