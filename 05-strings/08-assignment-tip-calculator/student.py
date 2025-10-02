# write your code here

"""
100
"""

def tip_calculator():
    total_price = float(input("Enter total price: "))

    default_tip_percentage = 20

    enter_tip_percentage = input(f"Enter tip percentage (default={default_tip_percentage}): ")

    if enter_tip_percentage == '':
        enter_tip_percentage += str(default_tip_percentage)

    additional_tip = total_price * (float(enter_tip_percentage) / 100)
    final_amount_to_pay = total_price + additional_tip

    print(f"You have to pay {round(final_amount_to_pay)}")

# tip_calculator()
