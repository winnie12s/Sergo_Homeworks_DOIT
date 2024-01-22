#Create a function which will take users weight and return their weight on the moon(Gravitation of the moon is 6 times less than on Earth)

user_weight = int(input("What is your weight? "))
def moon_weight(weight):
    return round(weight/6,2)


#additional
print("Your weight on a moon is", moon_weight(user_weight))