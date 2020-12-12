# hello = "kushan"

# print(10+20)
# print(hello)

# firstname = input("firstname : ")
# lastname = input("lastname : ")

# print("your full name is ",firstname,lastname)

# ----------math operations-----------

# num1 = input("first number :")
# num2 = input("second number :")

# n1 = int(num1)
# n2 = int(num2)

# print(n1*n2)

# --------------conditional operations---------------

# budget = input("Provide your budget : ")

# price = float(budget)

# if price > 500:
#     print("You can buy the product")
# else:
#     print("Sorry..! You can't buy it")

budget = input("Provide your budget : ")

price = float(budget)

if price > 1000:
    print("You can buy iphone 12")
elif 1000 >= price > 900:
    print("You can buy iphone 11")
elif 900 >= price > 800:
    print("You can buy iphone 10")
elif 800 >= price > 700:
    print("You can buy iphone SE")
elif 700 >= price > 600:
    print("You can buy iphone 8")
else:
    print("You can buy iphone 7")