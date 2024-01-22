# Task 1
#
# from collections import Counter
#
# with open("article.txt", "r") as file:
#     text = file.read()
#
# words = text.split()
#
# word_counts = Counter(words)
#
# second_most_common_word = word_counts.most_common(2)[1][0]
#
# print("Second most used word:", second_most_common_word)



# Task 2

# import csv
#
# with open('names.csv', 'r') as csv_file:
#     with open('names.txt', 'w') as txt_file:
#         csv_reader = csv.reader(csv_file)
#
#         for row in csv_reader:
#             txt_file.write(','.join(row) + '\n')
#
# print("Data copied from names.csv to names.txt.")