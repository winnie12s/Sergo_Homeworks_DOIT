def is_dict_empty(input_dict):
    return not bool(input_dict)

my_dict = {}
result = is_dict_empty(my_dict)
print(result)  # This will print True

my_dict = {'a': 1, 'b': 2}
result = is_dict_empty(my_dict)
print(result)  # This will print False
