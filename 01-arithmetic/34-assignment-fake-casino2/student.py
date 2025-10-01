# write your code here

import random

def generate_number(n):
    return round(random.uniform(1, n), 1)

print(generate_number(15))

def fake_casino_revisited(n):
    random.seed(42)
    for _ in range(5):
        print(generate_number(n))