# write your code here

import math

def movie_ticket(duration: int, imax: bool,
            student: bool, ticket_count: int):

    if duration <= 90:
        base_price = 10
    elif duration <= 120:
        base_price = 11
    elif duration <= 150:
        base_price = 12
    else:
        base_price = 15

    if imax:
        base_price = math.ceil(base_price * 1.2)

    if student:
        base_price -= 3

    return base_price * ticket_count

print(movie_ticket(180, True, False, 2))