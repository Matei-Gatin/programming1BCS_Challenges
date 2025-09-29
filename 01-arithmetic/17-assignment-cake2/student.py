# write your code here


def cake2(eggs, flour):
    egg_cake_count = eggs // 5
    flour_cake_count = flour // 250
    return min(egg_cake_count, flour_cake_count)