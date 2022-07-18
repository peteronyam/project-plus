# a = 10
# ai = "Hi \nHow are you?"
# print(a)
# print(ai)
#
#
# def scan():
#     if 2 > 3:
#         print("yes")
#     else:
#         print("Input Error")
#
#
# print(scan())
# pass
# print("""
# Good morning, sir
# this is how i want the above code to appear but it's not working , please check it out for me
# this is how
# first, How are you?
# secondly, input your responds
# thirdly, input your name and you will be able to see a message on your screen
# then if your score is 70 and above you should see a message saying you are blah blah blah
# while if your score is less than 70 you should see a message saying you should try again
# """)
# name = input("type in your name here to know your examination score ")
# # score = 96
#
#
# def score():
#     if score < 70:
#         print("your score didn't meet the minimum requirement for the test")
#     else:
#         print("you are blah blah blah")
#
#
# s = "I'm fine"
# print(f"{ai}\n{s} \nHI, {name}\nYou scored {score} on the spanish test")
#
# # Slicing is the process of obtaining a portion (substring) of a string by using its indices
# # string[start:end:step]
# my_string = "This bu MY string!"
# print(my_string[0:7])  # A step of 1
# print(my_string[0:13:2])  # A step of 2
# print(my_string[0:6:5])  # A step of 5
#
# my_string = "This is MY string!"
# print(my_string[13:2:-1])  # Take 1 step back each time
# print(my_string[17:0:-2])  # Take 2 steps back. The opposite of what happens in the slide above
#
# my_string = "This is MY string!"
# print(my_string[:8])  # All the characters before 'M'
# print(my_string[8:])  # All the characters starting from 'M'
# print(my_string[:])  # The whole string
# print(my_string[::-1])  # The whole string in reverse (step is -1)
#
# ring1 = "525system"
# ring2 = "i like %s" % "Python"
#
# print(ring1)
# print(ring2)
# rin = "%s and %s" % (ring1, ring2)
# nam = "%s\n%i" % (ring1, 525)
# print(rin)
# print(nam)
# s = 4 * 5
# p = -24 + 5
# print("%s %s = %s" % (s, p, s+p))
#
# # inserting floats within a string
# std = 1.11
# st = 1.137
# cd = 1.117
# print("%f and %.2f plus %.2f = %.2f" % (std, st, cd, std+st*cd))
#
# # from mr solo
# #
# greetings = input("Hi!\nHow is it going?\n>>> ")
# name = input("Enter your name here to see your examination score: ")
# 
# 
# def score(num):
#     x = num
#     if x >= 70:
#         return f"Congratulation {name}!\nYou scored {x} on the spanish test."
#     else:
#         return "your score didn't meet the minimum requirement for the test"
# 
# 
# print(score(4))
#
# # salutation =
# sur_name = input("SurName: ")
# first_name = input("first name: ")
# #
# name = "%s, %s" % (sur_name, first_name)
#
#
# def score(num):
#     x = num
#     if x >= 70:
#         return f"Congratulations {name}.\nYou scored {x} on your spanish test"
#     else:
#         return f"Hey! {name}.\nyour score didn't meet the minimum requirement for the test.\nYou might want to sit for the next session examinations "
#
#
# peter = {
#     'mac': '{0:8} | {1:9}'.format('score', 'Grade'),
#     'macs': '{0:8} | {1:9}'.format(score(70), 'A')}
# ne = "phone_book['mac']"
# nn = "phone_book['macs']"
# # def score(num):
# #     x = num
# #     if x >= 70:
# #         return f"Congratulations {name}.\nYou scored {x} on your spanish test"
# #     else:
# #         return f"Hey! {name}.\nyour score didn't meet the minimum requirement for the test.\nYou might want to sit for the next session examinations "
#
# print("%s with grade %s" % (score(500), peter ))

# print(score(9))
# name = input("Type in your name: ")
# phone_book = {"batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# # print(phone_book["batman"])
# output = ""
# for character in name:
#     output += phone_book.get(character, "!") + ""
# print("%s with grade %s" % (score(500), output))
# my_string = "This is MY string!"
# print(my_string[:8])  # All the characters before 'M'
# print(my_string[8:])  # All the characters starting from 'M'
# print(my_string[:])  # The whole string
# print(my_string[::-1])  # The whole string in reverse (step is -1)
#
# ring1 = "525system"
# ring2 = "i like %s" % "Python"
#
# print(ring1)
# print(ring2)
# rin = "%s and %s" % (ring1, ring2)
# nam = "%s\n%i" % (ring1, 525)
# print(rin)
# print(nam)
# s = 4 * 5
# p = -24 + 5
# print("%s %s = %s" % (s, p, s+p))


# mac = '{0:8} | {1:9}'.format('score', 'Grade')
# macs = '{0:8} | {1:9}'.format(70, 'A')
# print('{0:8} | {1:9}'.format('Apples', 3.))
# print('{0:8} | {1:9}'.format('Oranges', 23.))
# print("%s \n%s" %(mac, macs))
# class score_bored():
#     def score(num):
#         print("score(67)")
#
#
# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# # child class which inherit functions from parents class
#
# class Dog(Mammal):
#     pass
#
#
# class Cat(Mammal):
#     pass
#
#
# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.walk()
#
#
# # to add more attributes related to a specific item
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     def smilie(self):
#         print("smilie")
#
#
# cat1 = Cat()
# cat1.smilie()
#

#
# def students(name, score, Grade):
#     pass


# students(name='James maison', score='75', Grade='B')
#
# def students(**kwargs: object) -> object:
#         def james(**kwargs):
#             james(
#
#             )
#     for key, value in kwargs.items():
#         print("%s || %s" % (key, value))
#
#
# time = students(name=input('Type in your name to see your examination score: '), score='75', Grade='B')
# name = "%s" % (students())

# def score(students):
#     assert isinstance(students(), object)
#     x = input("type in your name: ")
#     if x >= 70:
#         return f"Congratulations {name}.\nYou scored {x} on your spanish test"
#     else:
#         return f"Hey! {name}.\nyour score didn't meet the minimum requirement for the test.\nYou might want to sit for the next session examinations "
#
# # print(time)
# is_near = False
# is_nice = False
# has_family = False
# james = True
# transport = False
# ten = ['{0:8} | {1:9}'.format('score', 'Grade')] or ['{0:8} | {1:9}'.format(70, 'A')]
# conditions = [
#     is_nice, is_near, has_family, james, transport, *ten
# ]
# print(conditions[is_nice])