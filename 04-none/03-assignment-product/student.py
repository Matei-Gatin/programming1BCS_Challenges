from math import prod


def product(a, b, c):
    non_none_values = []
    for i in [a, b, c]:
        if i is not None:
            non_none_values.append(i)

    if a is None and b is None and c is None:
        return 1

    product_of_nums = prod(non_none_values)

    return product_of_nums