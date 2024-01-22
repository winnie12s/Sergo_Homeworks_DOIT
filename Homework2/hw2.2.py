user_category = input("Choose one of the categories(Laptops, PCs, Mobiles): ").strip().lower()
user_budget = int(input("Your max budget? "))

if user_category == "laptops" or user_category=="laptop" :
    if user_budget < 500:
        print("We dont have offers for that amount")
    elif user_budget <1000:
        print("Acer MX1524")
    elif user_budget <1500:
        print("Lenovo 3824")
    else:
        print("Macbook Air")
elif user_category =="pcs" or user_category=="pc":
    if user_budget < 500:
        print("We dont have offers for that amount")
    elif user_budget < 1000:
        print("Intel i5 8 ram")
    elif user_budget < 1500:
        print("Intel i7 16 ram")
    else:
        print("Intel i9 32 ram")
elif user_category =="mobiles" or user_category =="mobile":
    if user_budget < 500:
        print("We dont have offers for that amount")
    elif user_budget < 1000:
        print("Xiaomi")
    elif user_budget < 1500:
        print("Samsung")
    else:
        print("Apple")
else:
    print("we dont have that!")
