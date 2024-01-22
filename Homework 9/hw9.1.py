import random

random_list = [random.randint(-100,100) for _ in range(10)]
random_list.sort()
print(random_list)