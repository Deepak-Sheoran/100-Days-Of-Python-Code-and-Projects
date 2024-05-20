import string
from random import choice, shuffle

print("Welcome to Py Password Generator.")
num_letters = int(input("How many letters would you like in your password = "))
num_symbols = int(input("How about symbols. How many of those you want in your password = "))
num_numbers = int(input("How many numbers would you like = "))
letter_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
symbols = list('''~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/''')
numbers = list(range(0, 10))
password = ''
for num in range(num_letters):
    password += choice(letter_list)
for num in range(num_symbols):
    password += choice(symbols)
for num in range(num_numbers):
    password += str(choice(numbers))

password = list(password)
shuffle(password)
password = ''.join(password)

print(password)
