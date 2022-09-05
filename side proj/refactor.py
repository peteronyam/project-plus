# # word replacement
# def refactor():
#
#     str = "Hello, world, replace this world"
#     here = input("enter word to refactor: ")
#     here_replace = input("enter new word: ")
#     print(str.replace(here, here_replace))
#
# # refactor()
#
# # basic calculator
# def add(a, b):
#     sum = a + b
#     print(str(a) + " + " + str(b)+" ="+str(sum))
#     # print(a,b)
#
#
# def sub(a, b):
#     sum = a - b
#     print(str(a) + " -" + str(b) + " =" + str(sum))
#
#
# def mul(a, b):
#     sum = a * b
#     print(str(a) + " *" + str(b) + " =" + str(sum))
#
#
# def div(a, b):
#     sum = a/ b
#     print(str(sum) + "\n")
# while True:
#
#     print("A. Addition")
#     print("B. subtraction")
#     print("C. multiplication")
#     print("D. division")
#     print("T.  Terminate calculator")
#     option = input("type in an option from above list: ")
#
#     if option == "A" or option == "a":
#         print("Addition")
#         a = int(input("first number: "))
#         b = int(input("second number"))
#         add(a, b)
#     elif option == "B" or option == "b":
#         print("Subtraction")
#         a = int(input("first number: "))
#         b = int(input("second number: "))
#         div(a, b)
#     elif option == "C" or option == "c":
#         print("multiplication")
#         a = int(input("enter first number: "))
#         b = int(input("enter second number: "))
#         mul(a, b)
#     elif option == "d" or option == "D":
#         print("division")
#         a = int(input("type in first number: "))
#         b = int(input("type in second number: "))
#         div(a, b)
#     else:
#         print("Thank you for choosing us!")
#         quit()


# email slicer