def multiply_numbers(*numbers):
    if len(numbers) < 3:
        print("Please provide at least three numbers.")
        return None

    result = numbers[0]
    for num in numbers[1:]:
        result *= num
    print("Result:", result)
    return result

result = multiply_numbers(2, 3, 4)
