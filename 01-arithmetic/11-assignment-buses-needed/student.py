# write your code here
import math

def buses_needed(people_count, bus_capacity):
    return math.ceil(people_count / bus_capacity)

print(buses_needed(300, 30))