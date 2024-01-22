# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n=int(input("Number of stars: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


n=int(input("Number of stars: "))
for i in range(1, n * 2):
    if i <= n:
        print("* " * i)
    else:
        print("* " * (2 * n - i))