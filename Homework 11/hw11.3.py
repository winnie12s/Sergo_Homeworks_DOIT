def set_to_tuple(set1, set2):
    combined_set = set1.union(set2)
    result_tuple = tuple(combined_set)
    return result_tuple

set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_to_tuple(set_a, set_b)
print(result)