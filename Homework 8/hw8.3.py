numbers = [1, -2, 3, -4, 5, -6, -2, 5]

sumpos = sum(filter(lambda num: num>0,numbers ))
sumneg = sum(filter(lambda num: num<0,numbers ))

print("Sum of positive numbers:", sumpos)
print("Sum of negative numbers:", sumneg)