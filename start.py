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

# print("Sum is : " , n1+n2)

# --------------conditional operations---------------

# budget = input("Provide your budget : ")

# price = float(budget)

# if price > 500:
#     print("You can buy the product")
# else:
#     print("Sorry..! You can't buy it")

# budget = input("Provide your budget : ")

# price = float(budget)

# if price > 1000:
#     print("You can buy iphone 12")
# elif 1000 >= price > 900:
#     print("You can buy iphone 11")
# elif 900 >= price > 800:
#     print("You can buy iphone 10")
# elif 800 >= price > 700:
#     print("You can buy iphone SE")
# elif 700 >= price > 600:
#     print("You can buy iphone 8")
# else:
#     print("You can buy iphone 7")


# ......................loop........................

ages = [13, 17, 15, 12, 20]

# for age in ages:
#     print("this friend age", age)

# for num in range(0,10):
#     print(num)

# num = 0
# while num < 10:
#     print(num)
#     num = num +1
# num = 10









# def brushTeeth(num):
#     print("Brushing")
#     return num * 2
# brushTeeth(num)







# import random
# num = random.randint(0,10)
# print(num)








# hello = 'HeLlo WorLd'
# print(hello.upper())
# print(hello.lower())
# print(hello.capitalize())
# print(hello.lower().count('l'))






# x = [4, True, 'hi']
# y = x
# # print(x.pop(1))
# x[0] = 'hello'

# print(x,y)




# --------------sliced---------------

# x = [0,1,2,3,4,5,6,7,8,9]
# y = ['hi', 'hello', 'cya', 'sure']
# s = 'hello'
# sliced = x[8:5:-1]
# print(sliced)






# --------------exception handeling---------------

# try:
#     x = 7/0
# except Exception as e:
#     print(e)
# finally:
#     print("finally")




# --------------lambda---------------


# x = lambda x: x + 5
# print(x(2))

# a = lambda a, b: a + b
# print(a(2, 32))




# --------------map function---------------

# x = [1,2,3,4,5,6,7,8,9]

# mp = map(lambda i: i + 2, x)
# print(list(mp))







# --------------filter---------------

x = [1,2,3,4,5,6,7,8,9]

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

#another way with using a function

def func(i):
    i = i + 3
    return i % 2 == 0

mp = filter(func, x)
print(list(mp))


