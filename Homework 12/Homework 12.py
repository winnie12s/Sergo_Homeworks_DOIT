# Task 1

# def remove_duplicates(input_dict):
#     unique_values = list(set(input_dict.values()))
#     result_dict = {key: value for key, value in input_dict.items() if list(input_dict.values()).count(value) == 1}
#     return result_dict
#
# my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
# result = remove_duplicates(my_dict)
# print(result)

# Task 2

# def is_dict_empty(input_dict):
#     return not bool(input_dict)
#
# my_dict = {}
# result = is_dict_empty(my_dict)
# print(result)
#
# my_dict = {'a': 1, 'b': 2}
# result = is_dict_empty(my_dict)
# print(result)


# Task 3

# def create_char_count_dict(input_string):
#     char_count_dict = {}
#
#     for char in input_string:
#         if char in char_count_dict:
#             char_count_dict[char] += 1
#         else:
#             char_count_dict[char] = 1
#
#     return char_count_dict
#
#
# input_str = 'racoon'
# result = create_char_count_dict(input_str)
# print(result)
