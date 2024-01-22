def write_to_file():
    file_path = "user_input.txt"

    with open(file_path, 'a') as file:
        while True:
            user_input = input("Enter text (type 'enough' to stop): ")
            if user_input.lower() == 'enough':
                break
            file.write(user_input + '\n')

    print("Data has been written to the file.")

write_to_file()
