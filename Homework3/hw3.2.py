n = int(input("give me a number: "))
i=0
y=0
for i in range(1,n+1):
    for y in range (1,10):
        mult = i*y
        print(f"{i}*{y}={mult}")