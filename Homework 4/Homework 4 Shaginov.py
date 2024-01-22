# Task 1

# num_letters = 0
# num_digits = 0
# num_symbols = 0
#
# user_input = input("Enter a string: ")
#
# for char in user_input:
#     if char.isalpha():
#         num_letters += 1
#     elif char.isdigit():
#         num_digits += 1
#     else:
#         num_symbols += 1
#
# print(f"Number of letters: {num_letters}")
# print(f"Number of digits: {num_digits}")
# print(f"Number of other symbols: {num_symbols}")





# Task 2

# sentence1 = input("Enter the first sentence: ")
# sentence2 = input("Enter the second sentence: ")
#
# sentence3 = sentence1[0] + sentence2[-1] + sentence1[1] + sentence2[-2]
#
# print("Third sentence:", sentence3)





# Task 3

# sentence1 = input("Enter the first sentence: ")
# sentence2 = input("Enter the second sentence: ")
#
# rule1 = all(symbol in sentence2 for symbol in sentence1)
# rule2 = all(symbol in sentence1 for symbol in sentence2)
#
# if rule1 and rule2:
#     print("Strings are balanced!")
# else:
#     print("Strings are not balanced!")