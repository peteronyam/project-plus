# # print("#")
# # print("#")
# # # print("#")
# #
# # def main():
# #     print_column(3)
# #
# #
# # def print_column(height):
# #     # for _ in range(height):
# #         print("#\n" * height, end="")
# #
# #
# # main()
#
# def main():
#     print_row(4)
#
# def print_row(width):
#     print("?" * width)
#
#
# main()
#
# def foo(n):
#     time_table = [n * i for i in range(1, 11)]
#     for num in time_table:
#         print(foo(n))
#
#
#  Exceptions
# more correct
# try:
#     name =  int(input("what is your name? "))
#     print(f"name is {name}")
# except ValueError:
#     print("name is not an interger")

# best way
# try:
#     name =  int(input("what is your name? "))
# except ValueError:
#     print("name is not an interger")
# else:
#     print(f"name is {name}")

# THANK YOU JESUS
# telling the user to re-enter a name or number when first entry is incorrect
# while True:
#     try:
#         name =  int(input("what is your name? "))
#     except ValueError:
#         print("name is not an interger")
#     else:
#         break
#
# print(f"name is {name}")

# remodifyng
# def main():
#     name = get_em()
#     print(f"name is {name}")
#
#
# def get_em():
#     while True:
#         try:
#             name = int(input("what is your name? "))
#         except ValueError:
#             print("name is not an interger")
#         else:
#             break
#     return name
#
#
# main()

# remodifying plus more compact and not saying anything but
# # using the pass keyword
# def main():
#     name = get_em()
#     print(f"name is {name}")
#
#
# def get_em():
#     while True:
#         try:
#             return int(input("what is your name? "))
#         except ValueError:
#             pass
#
# main()

# remodification applied
# def main():
#     name = get_em("what is your name? ")
#     print(f"name is {name}")
#
#
# def get_em(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass
#
#
# main()


# debugging
# mistakes in your codes
# def main():
#     height = int(input("Height: "))
#     pyramid(height)
#
#
# def pyramid(n):
#     for i in range(n):
#         print("#" * i)
#
#
# if __name__ == "__main__":
#     main()

# modifying the debugging
#
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))

if __name__ == "__main__":
        main()