# # modules
# # generating infomation
# import random
# import statistics
# import sys
# #
# # names = random.choice(["heads", "tails", "bait", "time"])
# # print(names)
#
# #  importing a specific file from the random
#
# # from random import choice
# # names = random.choice(["make", 15, 10, 20, 1, 11, 50, 40, 31])
# # print(names)
#
# # using the randint(a, b)
# #
# # numbers = random.randint(4, 78)
# # print(numbers)
# #
# # vest = ["hikv", "jack", "unit", "union"]
# # random.shuffle(vest)
# # for ves in vest:
# #     print(ves)
# #
# # print(statistics.mean([100, 89]))
# # print(statistics.mode([100, 89]))
# # print(statistics.median([100, 89]))
# #
# # try:
# #     print("hello my name is", sys.argv[1])
# # except IndexError:
# #     print("no input")
#
# # adding a conditional
# check for errors
# if len(sys.argv) < 2:
#     print("hello my name is")
# elif len(sys.argv) > 2:
#     print("nope nope")
# else:
#     print("hey, buddy", sys.argv[1])
#print name tags
# # print("hello, name is", sys.argv[1])
# # adding the exit funtion
#
# # if len(sys.argv) < 2:
# #     print("hello my name is")
# # elif len(sys.argv) > 2:
# #     print("nope nope")
# # else:
# #     print("hey, buddy", sys.argv[1])
#
#
# if len(sys.argv) < 2:
#     sys.exit("maybe")
#
# for arg in sys.argv[1:-1]:
#     print("good to go", arg)
#
#
#
# # packages
import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])
#

# if len(sys.argv) < 2:
#     sys.exit("tin")
#
# for arg in sys.argv:
#     print("hello", arg)

# slicing
if len(sys.argv) < 2:
    sys.exit("rignt now")

for arg in sys.argv[1:-1]:
    print("hey,", arg)
# APIs
# application programing interface third party
# move to music
