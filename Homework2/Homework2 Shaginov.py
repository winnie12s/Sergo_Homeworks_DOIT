#Task 1
# print("Which empire's water-supply system (aqueduct) is still functioning today?")
# print("Possible answers")
# print("1.Sumer")
# print("2.Selchuk")
# print("3.Rome")
# print("4.Mongol")
#
# user_answer = input("Enter the number or text of the correct answer: ").strip().lower()
#
# if user_answer == "3" or user_answer == "rome":
#     print('Correct!')
# else:
#     print('No! Rome is correct!')








#Task 2
# user_category = input("Choose one of the categories(Laptops, PCs, Mobiles): ").strip().lower()
# user_budget = int(input("Your max budget? "))
#
# if user_category == "laptops" or user_category=="laptop" :
#     if user_budget < 500:
#         print("We dont have offers for that amount")
#     elif user_budget <1000:
#         print("Acer MX1524")
#     elif user_budget <1500:
#         print("Lenovo 3824")
#     else:
#         print("Macbook Air")
# elif user_category =="pcs" or user_category=="pc":
#     if user_budget < 500:
#         print("We dont have offers for that amount")
#     elif user_budget < 1000:
#         print("Intel i5 8 ram")
#     elif user_budget < 1500:
#         print("Intel i7 16 ram")
#     else:
#         print("Intel i9 32 ram")
# elif user_category =="mobiles" or user_category =="mobile":
#     if user_budget < 500:
#         print("We dont have offers for that amount")
#     elif user_budget < 1000:
#         print("Xiaomi")
#     elif user_budget < 1500:
#         print("Samsung")
#     else:
#         print("Apple")
# else:
#     print("we dont have that!")


#Task 3
# print("Welcome to the Quest Game!")
# print("You find yourself in a mystical forest. There are three paths ahead. Which one will you choose?")
#
# print("\n1. Take the left path")
# print("2. Take the middle path")
# print("3. Take the right path")
#
# choice1 = input("Enter your choice (1, 2, or 3): ")
#
# if choice1 == '1':
#     print("\nYou chose the left path.")
#     print("As you walk along the path, you discover a hidden cave.")
#     print("Inside the cave, you find a treasure chest. Congrats!")
# elif choice1 == '2':
#     print("\nYou chose the middle path.")
#     print("You encounter a wise old wizard who gives you a magical map.")
#     print("The map reveals a shortcut, and you continue your journey more efficiently.")
#     print("Do you go left or right?")
#     choice2 = input("Enter your choice (left or right): ")
#
#     if choice2 == 'left':
#         print("\nYou fall into the trap.")
#         print("Game over")
#     elif choice2 == 'right':
#         print("\nYou see a great amount of gold")
#         print("Congrats!")
#     else:
#         print("\nInvalid choice. You stand frozen, and bear kills you. Game over.")
# elif choice1 == '3':
#     print("\nYou chose the right path.")
#     print("You stumble upon a group of bandits. They demand your belongings.")
#     print("You can either:")
#     print("1. Fight the bandits")
#     print("2. Try to negotiate with the bandits")
#
#     choice2 = input("Enter your choice (1 or 2): ")
#
#     if choice2 == '1':
#         print("\nYou choose to fight the bandits.")
#         print("After a fierce battle, you emerge victorious but injured.")
#     elif choice2 == '2':
#         print("\nYou choose to negotiate with the bandits.")
#         print("Surprisingly, they agree to let you go in exchange for a small offering.")
#     else:
#         print("\nInvalid choice. You stand frozen, and the bandits take advantage. Game over.")
# else:
#     print("\nInvalid choice. You are lost in the forest. Game over.")


#Task4
# print("Welcome to the Profession Selector!")
#
# age = int(input("How old are you? "))
# experience = int(input("How many years of experience do you have? "))
# education = input("What is your highest level of education? (High school/College/Graduate) ").lower()
#
# if age < 25 and experience < 2 and education == "high school":
#     profession = "Sales Manager"
# elif age >= 25 and experience >= 5 and education == "graduate":
#     profession = "Doctor"
# else:
#     profession = "General Worker"
#
# print(f"Based on your answers, we suggest the profession of: {profession}")






