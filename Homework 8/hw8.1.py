numbers = [1,2,3]
mult_factor = int(input("Give me a number to multiply on: "))
multiply = lambda x, y: x*y
result = list(map(lambda x: multiply(x,mult_factor), numbers))

print(result)