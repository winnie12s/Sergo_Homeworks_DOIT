print("Which empire's water-supply system (aqueduct) is still functioning today?")
print("Possible answers")
print("1.Sumer")
print("2.Selchuk")
print("3.Rome")
print("4.Mongol")

user_answer = input("Enter the number or text of the correct answer: ").strip().lower()

if user_answer == "3" or user_answer == "rome":
    print('Correct!')
else:
    print('No! Rome is correct!')




