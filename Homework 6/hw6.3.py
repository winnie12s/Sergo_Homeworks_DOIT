user_input = input("give me the question: ").split()


def calculator(question):
    first = question[0]
    second = question[1]
    third = question[2]

    if second == "/" and third == "0":
        print("You cant divide by zero")
    else:
        if first.isdigit() and third.isdigit():

        else:
            print("You entered symbols instead of numbers")




calculator(user_input)