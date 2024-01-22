def immutable_set(input_list):
    unique_elements = frozenset(input_list)
    return unique_elements

my_list = [1, 2, 2, 3, 4, 4, 5]
result = immutable_set(my_list)
print(result)