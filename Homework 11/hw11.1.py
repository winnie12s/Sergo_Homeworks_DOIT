def unique_list(input_list):
    unique_elements = list(set(input_list))
    return unique_elements

my_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_list(my_list)
print(result)