# name = 'sam'
# last_letters = name[1:]
# print(last_letters)
# print('P' + last_letters)
# x = 'hello world'
# print(x + " it is beautiful outside!")
# letter = 'z'
# print(letter * 10)
# x = 'hello world'
# print(x.upper())
# print(x.split('l'))
# my_name = "keven"
# print("welcome " + my_name)
# print('This is a string {}'.format('INSERTED'))
# print('The {} {} {}'.format('fox', 'brown', 'quick'))
#
# # to rearrange the above, we can supply them according to the index of the word
# print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
#
# print('The {f} {q} {b}'.format(f='fox', b='brown', q='quick'))
#
# result = 100 / 777
# print(result)
# print("the result was {r}".format(r=result))
#
# # using precision
# print("the result was {r:1.5f}".format(r=result))
#
# result_plus = 104.12345
# print("the result was {pl:2.2f}".format(pl=result_plus))
#
# # f strings
# meme = "horses"
# print(f'hey, his name is {meme}')
#
# # making it mor complex, we try this
# s = "sam"
# age = 5
# gender = "male"
# print(f'{s} is a {gender} and he is {age} years old.')
# print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
# print('{0:8} | {1:9}'.format('Apples', 3.))
# print('{0:8} | {1:9}'.format('Oranges', 23.))
#
# p = "penny"
# print(f'A {p} saved is a {p} earned.')
#
# l = "Left"
# r = "Right"
# c = "Center"
# print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left', 'Center', 'Right'))
# print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11, 22, 33))
# print('This is my ten-character, two-decimal number:%10.2f' % 13.579)
# print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))
# # list
# # my_list = [1, 2, 3]
# my_list = ['string', 1000, 288, "run"]
# print(my_list[2:])
# print(my_list)
# mylist = ['one', 'two', 'three']
# print(mylist[1:])
# another_list = input("what number are you? ")
# print("your new number is " + another_list)
#
# print(f'{s} is a {gender} and he is {age} years old.')
#
# another_list = input("INPUT A NUMBER")
# digits_mapping = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
#     "+": "Plus"
# }
# output = ""
# for character in another_list:
#     output += digits_mapping.get(character, "!") + " "
# # print(output)
# print("your new number is " + output)

def multiply(a, b):
    return a , b
print(multiply(1 * 2,2 * 3))