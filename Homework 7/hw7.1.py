def hello(number):
    if number != 0:
        print("hey")
        number = number -1
        hello(number)

hello(10)
