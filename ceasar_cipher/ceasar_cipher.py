# import nltk
# nltk.download('words')
from nltk.corpus import words
word_list = words.words()


test_string = "ZZZ" # AAA // 1
break_string = 'It was the best of times, it was the worst of times.'
joseph_string = 'the sun is blue, i dont care.'

def encrypt(phrase, key):
    """takes in a phrase and a shfit key and returns encrypted plain phrase"""
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in phrase:
        if char in lower:
            idx = lower.find(char) # a -0
            shift = (idx + key) % len(lower) # 1
            encrypted += lower[shift]
        elif char in upper:
            idx = upper.find(char) # a -0
            shift = (idx + key) % len(upper) # 1
            encrypted += upper[shift]
        else: # whitespace - / ; ...
            encrypted += char
    return encrypted

def decrypt(phrase, key):
    return encrypt(phrase, -key)

def hack(encrypted): #
    for key in range(26):
        real_words = 0
        hacked = decrypt(encrypted, key)

        for word in hacked.split(' '):
            if word in word_list:
                real_words += 1

        if (real_words / len(hacked.split(' '))) >= 0.5: # left is percent right 1 / 100%
            return hacked
        else:
            continue



    # return hacked


secret = encrypt(joseph_string, 500)
plane = decrypt(secret, 500)
print(hack(secret))
# print(secret, plane, hack)
