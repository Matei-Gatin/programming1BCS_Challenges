# write your code here
import random

def roll_dice(n):
    return random.randint(1, n)

def fake_casino(n):
    random.seed(42)
    for _ in range(5):
        print(roll_dice(n))


fake_casino(6)