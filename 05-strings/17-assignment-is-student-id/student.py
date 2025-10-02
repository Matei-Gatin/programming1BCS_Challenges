# write your code here

def is_student_id(string: str) -> bool:
    len_of_string = len(string)

    if len_of_string != 8:
        return False

    first_char = string[0]
    rest_of_nums = string[1:]

    if first_char.lower() not in ["r", "s"]:
       return False

    try:
        check_if_rest_of_nums_ints = [int(rest_of_nums)]
        for i in check_if_rest_of_nums_ints:
            if not isinstance(i, int):
                return False
    except ValueError:
        return False

    return True

print(is_student_id('r0123456')) #true
print(is_student_id('r123456')) #false
print(is_student_id('R0123456')) #true
print(is_student_id('RR000000')) #false
print(is_student_id('R00000001')) #false

