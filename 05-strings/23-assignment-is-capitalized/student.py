# write your code here

def is_capitalized(string: str):
    if string == '':
        return False

    flag = False

    first_letter = string[0]

    if first_letter.isupper():
        flag = True

    for i in string[1:]:
        if i.isupper():
            flag = False

    return flag



print(is_capitalized("Ab def"))
print(is_capitalized("AB def"))
print(is_capitalized("ad deF"))
print(is_capitalized("A"))
print(is_capitalized("''"))

letter = "A"
if not letter.islower():
    print("isNotLower")