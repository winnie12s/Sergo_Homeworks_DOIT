sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

sentence3 = sentence1[0] + sentence2[-1] + sentence1[1] + sentence2[-2]

print("Third sentence:", sentence3)