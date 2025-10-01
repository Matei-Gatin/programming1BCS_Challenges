# write your code here

def middle(a, b, c):
    lowest = min(a, b, c)
    highest = max(a, b, c)
    sum = a + b + c
    return sum - lowest - highest

    # list_of_numbers = [a, b, c]
    # sorted_list = sorted(list_of_numbers)
    # return sorted_list[1]
#
# if __name__ == "__main__":
#     print(middle(6, 7, 5))
