# write your code here

def coins(amount):
    count_5 = amount // 5
    amount = amount % 5
    count_2 = amount // 2
    amount = amount % 2
    count_1 = amount
    return count_5 + count_2 + count_1