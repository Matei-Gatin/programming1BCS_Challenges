# write your code here

from math import ceil

def internet_costs(duration_in_seconds, cost_per_block):
    time_in_min = ceil(duration_in_seconds / 360)
    return time_in_min * cost_per_block
