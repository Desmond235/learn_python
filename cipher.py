import string
import random

from streamlit import radio

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# encrypt
plain_text  = input('Enter text to encrypt: ')
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'original text: {plain_text}')
print(f'ciphered text: {cipher_text}')


#  decrypt
cipher_text = input("Enter encrypted text: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f'ciphered text: {cipher_text} ')
print(f'plain text : {plain_text}')