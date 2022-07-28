# # import pandas as pd
# # import os
# #
# # student = pd.read_excel("student.xlsx",sheet_name="students docs")
# #
# # i = input("enter store number: ")
# # print(student[student['Name'] == i])
# #
#
# # arithmetic operators in python
#
# print(10 ** 5)
#
# float1 = 13.55
# float2 = 4.56
# print(float1 - float2)
#
# num = 20
# ftc = 55
# flt = 10.58
# print(20 * (10.58 ** 55) % 1000)
# print(num * flt / ftc)
#
# print( num < flt)
# print(float1 > float2)
# james = 20
# second = james
# james = 55
# print(james, second)
# noble = True or False
# print(noble)
# nob = True and False
# print(nob)
# sam = False
# print( not sam)
# print(sam)
#
# # bit values
#
# time = 1000 * True or False
# print(time)
# time = 10 * False
# print(time)
#
# # bitwise operator
#
# name = 50
# time = 71
#
# print(name & time)
# print(name | time)
# print(~time)
# print(time ^ name)
# print(name << 5)
# print(time >> 5)
#
# print('a' < 'b')
#
# house = "Germany"
# house_copy = "Germany"
#
# print(house == house_copy)
# news = "Slytherin"
# print(house == news)
#
# print(news <= house)
#
# print("ha" * 3)
#
# #  checking the existense
# clak = "this is random"
#
# print('is' in clak)
# anf = [1, 2.9, "My string", True]
# print(anf)
# print(len(anf))
# print(anf[2])
# m = '123456789'
# print(m[-2: -6: -2])
# k = 20
# t = 5
# result = (k + True) / (4 - t * False)
# print(result)
# G = 6.67 * (10 ** -11)
# M = 6.0 * (10 ** 24)
# m = 7.34 * (10 ** 22)
# r = 3.84 * (10 ** 8)
#
# grav_force = (G * M * m) / (r ** 2)
#
# print(grav_force)
#
# hi = 80
#
# if (hi >= 76):
#     print("The hi is positive")
# else:
#     print("try again")
# if (hi == 76):
#     print("very nice")
# else:
#     print("not so cool")
#
# nu = 12
#
# if nu % 2 == 0 and nu % 3 == 0 and nu % 4 == 0:
#     print("multiple of 2 ,3, 4")
#
# if (nu % 5 == 0 or nu % 6 == 0):
#     print("multiple of 5 and/or 6")
#
# # nested if
#
# nu = 63
#
# if nu >= 0 and nu <= 100:
#     if nu >= 50 and nu <= 75:
#         if nu >= 60 and  nu <= 70:
#             print("the number is in 60-70 range")
#
#
#
# ke = 50
# if ke > 0:
#     if ke > 0:
#         print(ke)
#     ke = 20
#     new_ke = ke * 10
#
# print(ke)
# print(new_ke)

# the if-else
# mt = 40
# if mt > 50:
#     print("ths is fae")
# else:
#     if mt == 50:
#         print("time coming")
#     else:
#         print("data n type")
#
# mk = 60
#
# output = "can we walk for a while?"\
#     if mk <= 50 else "the time is bear"
#
# print(output)
#
# # the if-elif-else
# light = "off"
#
# if light == "Green":
#     print("Go")
#
# elif light == " Yellow":
#     print("Wait")
#
# elif light == "Red":
#     print("Stop")
#
# else:
#     if light == "off":
#         print("incorrect light signal\nwe are having a technical challenge")
#     elif light == "Walk way":
#         print("hult")
#     else:
#         print("free ride/drive")
#
# # for numbers
# num = 8
# if num == 0:
#     print("zero")
# elif num ==1:
#     print("one")
# elif num == 2:
#     print("two")
# elif num == 3:
#     print("three")
# elif num == 4:
#     print("four")
# elif num == 5:
#     print("five")
# elif num == 6:
#     print("six")
# elif num == 7:
#     print("seven")
# elif num == 8:
#     print("eight")
# elif num == 9:
#     print("nine")
# else:
#     print("sorry\nyou input isn't correct")

# An important thing to keep in mind is that an if-elif-else or\
# if-elif statement is not the same as multiple if statements. if\
# statements act independently.
# If the conditions of two successive ifs are True, both statements\
# will be executed.
# On the other hand, in if-elif-else, when a condition evaluates to\
# True, the rest of the statement’s conditions are not evaluated.
# if num % 2 == 0:
#     print("this is even")
# if num % 2 == 0:
#     print("i came back")
# elif num % 2 == 0:
#     print("this is m  even")
# else:
#     pass
#
# num1 = 10
# num2 = 20
# result1 = 4000
# if (num1 > 50 or not num2 <= 5):
#     result1 = (num1 * num2)
#     print(result1)
# else:
#     result1 = (num1 + num2)
#     print(result1)

price = 250
#
# if ("price => 300"):
#     discount = (30 * price) / 100
#     print(discount)
# elif price:
#     if ("price = 250"):
#         discount = (20 * price) / 100
#         print(discount)
#     elif ("price == 300"):
#         discount = (20 * price) / 100
#         print(discount)
# elif price:
#     if ("price == 200"):
#         discount = (10 * price) / 100
#         print(discount)
#     elif ("price == 100"):
#         discount = (10 * price) / 100
#         print(discount)
# elif ("price == 100"):
#     discount = (5 * price) / 100
#     print(discount)
# else:
#     print(price)

if price >= 300:
    price *= 0.7  # (1 - 0.3)
elif price >= 200:
    price *= 0.8  # (1 - 0.2)
elif price >= 100:
    price *= 0.9  # (1 - 0.1)
elif price < 100 and price >= 0:
    price *= 0.95  # (1 - 0.05)

print(price)

# Problem Statement#
# In this challenge, you must discount a price according to its value.
#
# If the price is 300 or above, there will be a 30% discount.
#
# If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.
#
# If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.
#
# If the price is less than 100, there will be a 5% discount.
#
# If the price is negative, there will be no discount.
time = 400

if time >= 300:
    time *= 1 - (30 / 100)
elif time >= 200:
    time *= 1 - (20 / 100)
elif time >= 100:
    time *= 1 - (10 / 100)
elif time < 100 and time >= 0:
    time *= 1 - (5 / 100)

print(time)

# funcctions

cup = 10
tea_bags = 20
if cup < tea_bags:
    minimum = cup
else:
    minimum = tea_bags
print(minimum)

cup = 250
tea_bags = 120
if cup < tea_bags:
    minimum = cup
else:
    minimum = tea_bags
print(minimum)

cup = 100
tea_bags = 100
if cup < tea_bags:
    minimum = cup
else:
    minimum = tea_bags
print(minimum)

# making the above code cleaner and better

minimum= min(10, 50)
print(minimum)

minimum = min(10, 1, 100, 1000)
print(minimum)

minimum = min("Superman", "Batman")
print(minimum)

