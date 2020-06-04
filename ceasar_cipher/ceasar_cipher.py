import nltk
nltk.download('words')
from nltk.corpus import words



def encrypt(phrase, key):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    shifted = ''

    for i in phrase:
        pass

def decrypt(phrase, key):
    return encrypt(phrase, -key)
