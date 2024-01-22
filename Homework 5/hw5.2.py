user_list = []

login = input("Enter your login: ")
password = input("Enter your password (8 characters or more): ")

if login and len(password) >= 8:
    user_list.append({'login': login, 'password': password})
    print("Registration successful!")
else:
    print("Registration failed. Please ensure login is not empty and password is 8 characters or more.")

login_attempt = input("Enter your login for login attempt: ")
password_attempt = input("Enter your password for login attempt: ")

if any(user['login'] == login_attempt and user['password'] == password_attempt for user in user_list):
    print("Login successful!")
else:
    print("Login failed. Please check your login and password.")