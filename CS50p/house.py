# # name = input("what is your name? ")
# #
# # if name == "james" or name == "nath" or name == "line":
# #     print("marian Road")
# # elif name == "harry":
# #     print("atimbo")
# # elif name == "clark":
# #     print("zone 6")
# # elif name == "kenny":
# #     print("etta agbo")
# # elif name == "virtue":
# #     print("time manto")
# # else:
# #     print("who? please")
# #
# # # using to match key
# #
lamp = input("what is your time? ")

match lamp:
    case "cartrine":
        print("marian road")
    case "thelma":
        print("nathy")
    case "thempletine":
        print("atimbo")
    case _:
        print("who?")

#         for the casee where two or more persons are staying or from the
# same place

match lamp:
    case "cartrine" | "james" | "kian":
        print("marian road")
    case "thelma":
        print("nathy")
    case "thempletine":
        print("atimbo")
    case _:
        print("who?")


# # loops
# # print("meow")
# # print("meow")
# # print("meow")
#
# # jim = 3
# # while jim != 0:
# #     print("meow")
# #     jim = jim - 1
# #
# # # modifying
# # jim = 1
# # while jim <= 3:
# #     print("shie")
# #     jim = jim + 1
# #
# # # remodifying
# #
# # jim = 0
# # while jim < 3:
# #     print("mmm")
# #     jim = jim + 1
# # # +=
# # jim = 0
# # while jim < 3:
# #     print("oops")
# #     jim += 1
#
# # using for loop
# #
# # for jim in [0,1,2]:
# #     print("meow")
#
# # using range
# # for jim in range(3):
# #     print("meow")
#
# print("meow\n"*3)
#
# #  to clear the extra line below
#
# print("meow\n" * 3, end="")
#
# # getting iput from the user
while True:
    sound = int(input("how many times do you want the cat to cry? "))
    if sound < 0:
        continue
    else:
        break

for _ in range(sound):
    print("meow")


# def mac(mc="keven"):
#     print("hello,", mc)
#
#
# name = input("what is your name? ")
# mac(name)

# / defining a main function
def main():
    time = get_number()
    cat(time)


def get_number():
    while True:
        sound = int(input("what is your number? "))
        if sound > 0:
            break
    return sound


def cat(sound):
    for _ in range(sound):
        print("meow")


main()
