print("Welcome to the Quest Game!")
print("You find yourself in a mystical forest. There are three paths ahead. Which one will you choose?")

print("\n1. Take the left path")
print("2. Take the middle path")
print("3. Take the right path")

choice1 = input("Enter your choice (1, 2, or 3): ")

if choice1 == '1':
    print("\nYou chose the left path.")
    print("As you walk along the path, you discover a hidden cave.")
    print("Inside the cave, you find a treasure chest. Congrats!")
elif choice1 == '2':
    print("\nYou chose the middle path.")
    print("You encounter a wise old wizard who gives you a magical map.")
    print("The map reveals a shortcut, and you continue your journey more efficiently.")
    print("Do you go left or right?")
    choice2 = input("Enter your choice (left or right): ")

    if choice2 == 'left':
        print("\nYou fall into the trap.")
        print("Game over")
    elif choice2 == 'right':
        print("\nYou see a great amount of gold")
        print("Congrats!")
    else:
        print("\nInvalid choice. You stand frozen, and bear kills you. Game over.")
elif choice1 == '3':
    print("\nYou chose the right path.")
    print("You stumble upon a group of bandits. They demand your belongings.")
    print("You can either:")
    print("1. Fight the bandits")
    print("2. Try to negotiate with the bandits")

    choice2 = input("Enter your choice (1 or 2): ")

    if choice2 == '1':
        print("\nYou choose to fight the bandits.")
        print("After a fierce battle, you emerge victorious but injured.")
    elif choice2 == '2':
        print("\nYou choose to negotiate with the bandits.")
        print("Surprisingly, they agree to let you go in exchange for a small offering.")
    else:
        print("\nInvalid choice. You stand frozen, and the bandits take advantage. Game over.")
else:
    print("\nInvalid choice. You are lost in the forest. Game over.")

