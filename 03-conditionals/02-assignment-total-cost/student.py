# write your code here

def total_cost(amount):
    delivery_fee = amount + 10 if amount < 100 else None
    discount = amount - (amount * 0.05) if amount >= 200 else None
    return delivery_fee or discount or amount

print(total_cost(500))

