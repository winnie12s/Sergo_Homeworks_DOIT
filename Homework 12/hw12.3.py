def create_char_count_dict(input_string):
    char_count_dict = {}

    for char in input_string:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    return char_count_dict


input_str = 'racoon'
result = create_char_count_dict(input_str)
print(result)
