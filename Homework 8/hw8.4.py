import string

username = input("Give me your username: ")

def is_valid_password(password):
    if password[0].isupper():
        if any(char in string.punctuation for char in password):
            if any(char.isdigit() for char in password):
                return True
            else:
                print("Password must contain at least one number")
        else:
            print("Password must contain at least one symbol.")
    else:
        print("Password must start with an uppercase letter.")

    return False

while True:
    password = input("Enter your password: ")
    if is_valid_password(password):
        password_doublecheck = input("Put your password once again: ")
        if password==password_doublecheck:
            print("Password is valid!")
            break
        else:
            print("Passwords are not the same, try again!")
    else:
        print("Password is invalid, try again!")

bank_account = 0
notzero = addamount != 0
try:
    addamount = input("What amount do you want to add? ")
    bank_account += addamount
except ValueError:
    print("Invalid input. Please enter a valid number.")
except notzero as nz:
    print("You cant add zero")
