sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

rule1 = all(symbol in sentence2 for symbol in sentence1)
rule2 = all(symbol in sentence1 for symbol in sentence2)

if rule1 and rule2:
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")