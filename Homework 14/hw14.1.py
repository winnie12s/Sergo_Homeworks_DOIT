from collections import Counter

with open("article.txt", "r") as file:
    text = file.read()

words = text.split()

word_counts = Counter(words)

second_most_common_word = word_counts.most_common(2)[1][0]

print("Second most used word:", second_most_common_word)