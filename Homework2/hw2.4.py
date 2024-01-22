print("Welcome to the Profession Selector!")

age = int(input("How old are you? "))
experience = int(input("How many years of experience do you have? "))
education = input("What is your highest level of education? (High school/College/Graduate) ").lower()

if age < 25 and experience < 2 and education == "high school":
    profession = "Sales Manager"
elif age >= 25 and experience >= 5 and education == "graduate":
    profession = "Doctor"
else:
    profession = "General Worker"

print(f"Based on your answers, we suggest the profession of: {profession}")

