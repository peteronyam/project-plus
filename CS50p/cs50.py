# #ask users for their names
# name = input("what is your name? ").strip().title()
#
# # say hello to user
# print("hello, " + name)
# home = name.strip().title()
# # about to split user surname frim other names
# last, first = name.split(" ")
# # another
# print(f"hello, {last}")
# # print(home)

# functions
# def = define


def main(to="EUROPE"):
    kent = input("what's your name? ")
    hello(kent)


def hello(to="EUROPE"):
    print("hello,", to)


main()
