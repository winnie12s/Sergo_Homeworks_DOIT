my_list = ["Apple", "banana", "Cherry", "date", "Elderberry"]

length = lambda lst: len(list(filter(lambda x: x[0].isupper(), lst)))

print(length(my_list))