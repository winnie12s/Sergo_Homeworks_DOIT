consumer_info = []

for i in range(3):
    name = input("Enter name for user {}: ".format(i + 1))
    surname = input("Enter surname for user {}: ".format(i + 1))
    age = input("Enter age for user {}: ".format(i + 1))

    user_info = [name, surname, age]
    consumer_info.append(user_info)

index = int(input("Enter the index to retrieve information: "))

if 0 <= index < len(consumer_info):
    user_info = consumer_info[index]
    print("Name: {}".format(user_info[0]))
    print("Surname: {}".format(user_info[1]))
    print("Age: {}".format(user_info[2]))
else:
    print("Invalid index. Please enter a valid index.")