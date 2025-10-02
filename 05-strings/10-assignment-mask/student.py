# write your code here

def mask(password: str) -> str:
    len_of_pass = len(password)
    if len_of_pass == 0:
        return ""
    return len_of_pass * "*"

print(mask(""))