# Task 2 - გამრავლების ტაბულა

# ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.

# n = int(input("give me a number: "))
# i=0
# y=0
# for i in range(1,n+1):
#     for y in range (1,10):
#         mult = i*y
#         print(f"{i}*{y}={mult}")



# Task 3 - საბანკო ანგარიში
# შეადგინე პროგრამა რომელიც განასახიერებს საბანკო ანგარიშს. მასზე განთავსებულია თანხა 3000 ლარისოდენობით.
# პროგრამა გეკითხება გაწეულ ხარჯს და აკლებს ანგარიშს მანამ, სანამ არ შეიყვან 0_ს.
# შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს ფუნქციონირებას. თუ ანგარიშზე არსებული თანხა ნაკლებია დანახარჯის თანხაზე
# პროგრამამ უნდა დაბეჭდოს, რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება.

# bank_acc = 3000
#
# while True:
#     expense = int(input("Whats your expense?: "))
#     if expense != 0:
#         bank_acc = bank_acc - expense
#         continue
#     elif expense > bank_acc:
#         print(f"Not enough money")
#         continue
#     else:
#         print(f"Your balance is {bank_acc}")
#         break

# Task 4 - თუთიყუშის პროგრამა
# დაწერე პროგრამა_ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ შეიყვან სიტყვას quit,თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat!?”
# “User Said Hello”

# stop_phrase = "quit"
#
# while True:
#     phrase_to_repeat = input("Give me a phrase to repeat:")
#     if phrase_to_repeat != stop_phrase:
#         print("User said Whaaaat?")
#         print(f"User said {phrase_to_repeat}")
#     else:
#         break



