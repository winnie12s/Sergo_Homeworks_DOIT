# Task 1

# def write_to_file():
#     file_path = "user_input.txt"
#
#     with open(file_path, 'a') as file:
#         while True:
#             user_input = input("Enter text (type 'enough' to stop): ")
#             if user_input.lower() == 'enough':
#                 break
#             file.write(user_input + '\n')
#
#     print("Data has been written to the file.")
#
# write_to_file()


# Task 2

import os

# def create_and_list_files():
#     # Get user input for folder location and file name
#     folder_location = input("Enter the folder location: ")
#     file_name = input("Enter the file name to create: ")
#
#     # Create the file in the specified location
#     file_path = os.path.join(folder_location, file_name)
#
#     try:
#         with open(file_path, 'w') as file:
#             file.write("This is a sample file content.")
#         print(f"File '{file_name}' has been created in '{folder_location}'.")
#     except Exception as e:
#         print(f"Error creating the file: {e}")
#
#     # Print a list of all files in the specified folder
#     try:
#         file_list = os.listdir(folder_location)
#         print(f"\nList of files in '{folder_location}':")
#         for file in file_list:
#             print(file)
#     except Exception as e:
#         print(f"Error listing files: {e}")
#
# create_and_list_files()


