import random
import time
from statistics import mean
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_sorting_time(sorting_function, data):
    start_time = time.time()
    sorting_function(data)
    end_time = time.time()
    return end_time - start_time

# Generate lists of random numbers
list_1000 = generate_random_list(1000)
list_2000 = generate_random_list(2000)
list_3000 = generate_random_list(3000)

# Measure sorting time for Bubble Sort
time_bubble_1000 = measure_sorting_time(bubble_sort, list_1000.copy())
time_bubble_2000 = measure_sorting_time(bubble_sort, list_2000.copy())
time_bubble_3000 = measure_sorting_time(bubble_sort, list_3000.copy())
time_bubble = (time_bubble_1000,time_bubble_2000,time_bubble_3000)
# Measure sorting time for Selection Sort
time_selection_1000 = measure_sorting_time(selection_sort, list_1000.copy())
time_selection_2000 = measure_sorting_time(selection_sort, list_2000.copy())
time_selection_3000 = measure_sorting_time(selection_sort, list_3000.copy())
time_selection = (time_selection_1000, time_selection_3000, time_selection_2000)
# Print the results
print("Bubble Sort:")
print(f"1000 numbers: {time_bubble_1000} seconds")
print(f"2000 numbers: {time_bubble_2000} seconds")
print(f"3000 numbers: {time_bubble_3000} seconds")

print("\nSelection Sort:")
print(f"1000 numbers: {time_selection_1000} seconds")
print(f"2000 numbers: {time_selection_2000} seconds")
print(f"3000 numbers: {time_selection_3000} seconds")

print()
if mean(time_bubble) < mean(time_selection):
    print("Bubble sort is faster")
else:
    print("Selection sort is faster")