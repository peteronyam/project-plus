# # x = input("what's x? ")
# # y = input("what's y? ")
# #
# # z = int(x) + int(y)
# #
# # print("The sum of your inputted values is ", z)
# #
# #
# # x = int(input("what's x? "))
# # y = int(input("what's y? "))
# #
# # print("The sum of your inputted values is ", x + y)
#
# # IN PROGRAMMING,READABILITY IS VERY IMPORTANT I.E MAKING YOUR CODE VERY READABLE TO SOMONE ELSE LOOKING AT THE CODE
# #  AND CODE SIMLICITY
#
# # float
# x = float(input("what's x? "))
# y = float(input("what's y? "))
# z = round(x + y)
# print("The sum of your inputted values is ", z)
# # using round to
# # to print degits in the form of 1,000,000 and more
# m = round(x / (-y))
# print(f"{m:,}")


# def main():
#     x = int(input("what's x? "))
#     print("x squared is", square(x))
#
# def square(n):
#     return n * n
#
# main()

# compare.py

mac = int(input("what's the value of mac? "))
jame = int(input("what's the value of jame? "))
# making all if
if mac < jame:
    print("mac is less than jame")
if mac > jame:
    print("mac is greater than jame")
if mac == jame:
    print("mac is equal jame")

# adding elif
if mac < jame:
    print("mac is less than jame")
elif mac > jame:
    print("mac is greater than jame")
elif mac == jame:
    print("mac is equal jame")

# adding else
if mac < jame:
    print("mac is less than jame")
elif mac > jame:
    print("mac is greater than jame")
else:
    print("mac is equal jame")

# adding or
if mac < jame or mac > jame:
    print("mac not equal to jame")
else:
    print("mac is equal jame")

# using not equal to
if mac != jame:
    print("mac not equal to jame")
else:
    print("mac is equal jame")

# using equal equal (==)
if mac == jame:
    print("mac is equal jame")
else:
    print("mac not equal to jame")
# and
