# write your code here

def decode1(word: str):
    """
    SchAAl
    """
    list_of_words = []

    for i in word:
        list_of_words.append(i)

    for i in range(len(list_of_words[1:]) + 1):
        if list_of_words[i] == 'A':
            list_of_words[i] = 'o'

    return "".join(list_of_words)


def decode2(word: str):
    """
    hqovtzdpozgm
    """

    decrypted_word = word[0::2]
    return decrypted_word

def decode3(word: str):
    parts = word.split(" ")
    first_word_reversed = parts[0][::-1]
    new_word = " ".join(parts[1:])
    return first_word_reversed + (" " + new_word if new_word else "")

def decode4(word: str):
    word_length = len(word) // 2
    org_word = word[2:word_length + 2]
    return org_word

print(decode1("SchAAl"))
print(decode2("hqovtzdpozgm"))
print(decode3("sepocseleT are too expensive."))
print(decode4("oddolfijnnjiflK"))
