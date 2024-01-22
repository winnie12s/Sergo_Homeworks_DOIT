import random
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def sort_list(input_list):
    return sorted(input_list)

@measure_time
def linear_search(input_list, target):
    for index, value in enumerate(input_list):
        if value == target:
            return index
    return -1

@measure_time
def binary_search(input_list, target):
    low, high = 0, len(input_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

list_sizes = [10, 100, 1000]

for size in list_sizes:
    print(f"\nList size: {size}")
    random_list = generate_random_list(size)
    sorted_list = sort_list(random_list)

    linear_search_result = linear_search(sorted_list, sorted_list[size // 2])

    binary_search_result = binary_search(sorted_list, sorted_list[size // 2])

    print(f"Linear Search Result: {linear_search_result}")
    print(f"Binary Search Result: {binary_search_result}")
