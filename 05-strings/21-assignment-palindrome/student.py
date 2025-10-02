# write your code here

def palindrome(string: str):
    if string[0:] == string[::-1]:
        return True
    return False
