# write your code here

"""
+-----------------+
| Put me in a box |
+-----------------+
"""

def box(string):
    len_of_string = len(string)
    first_lower_row = "".join("+" + ((len_of_string + 2) * "-") + "+")
    middle_row = "| " + string + " |"

    return first_lower_row + "\n" + middle_row + "\n" + first_lower_row

print(box("Hey there matthew"))