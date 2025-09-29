# write your code here

def cake3(eggs, flour, butter, sugar):
    eggs_cake_count = eggs // 5
    flour_cake_count = flour // 250
    butter_cake_count = butter // 200
    sugar_cake_count = sugar // 250

    return min(eggs_cake_count, flour_cake_count,
               butter_cake_count, sugar_cake_count)