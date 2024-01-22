bank_acc = 0

while True:
    expense = int(input("Whats your expense?: "))
    if expense == 0 or bank_acc == 0:
        print(f"Your balance is {bank_acc}")
        break


    if expense> bank_acc:
        print("Not enough money")
        continue
    else:
        bank_acc -= expense



