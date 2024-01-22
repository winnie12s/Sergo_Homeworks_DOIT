def remove_duplicates(input_dict):
    unique_values = list(set(input_dict.values()))
    result_dict = {key: value for key, value in input_dict.items() if list(input_dict.values()).count(value) == 1}
    return result_dict

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
result = remove_duplicates(my_dict)
print(result)