num_letters = 0
num_digits = 0
num_symbols = 0

user_input = input("Enter a string: ")

for char in user_input:
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_digits += 1
    else:
        num_symbols += 1

print(f"Number of letters: {num_letters}")
print(f"Number of digits: {num_digits}")
print(f"Number of other symbols: {num_symbols}")