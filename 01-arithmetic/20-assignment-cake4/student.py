# write your code here

def cake4(eggs, flour, butter, sugar,
          eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    eggs_cake_count = eggs // eggs_per_cake
    flour_cake_count = flour // flour_per_cake
    butter_cake_count = butter // butter_per_cake
    sugar_cake_count = sugar // sugar_per_cake

    return min(eggs_cake_count, flour_cake_count, butter_cake_count, sugar_cake_count)