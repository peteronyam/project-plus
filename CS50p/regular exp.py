# name = input("what is your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

# using regular expressions
# import re
#
# name = input("what is your name? ").strip()
# rename = re.search(r"(.+), *(.+)$", name)
# if rename:
#     # last = rename.group(1)
#     # first = rename.group(2)
#     name = rename.group(2) + " " + rename.group(1)
# print(f"hello, {name}")

# using the walruses to modify the code
# import re
#
# name = input("what is your name? ").strip()
# if rename := re.search(r"(.+), *(.+)$", name):
#     name = rename.group(2) + " " + rename.group(1)
# print(f"hello, {name}")
#
# # extracting data from users input
# url = input("URL: ").strip()
#
# username = url.replace("https://twitter.com/", "")
# print(f"hello, {name}\nyour twitter username is: {username}")

# modifying to allow other input work very well
# using re.sub() to clean up the code
# import re
# from datetime import datetime

# import today as today
#
# url = input("URL: ").strip()
#
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"username: {username}")

# NOTE: (https?://)?(www\.)? the question mark here
# refers to optional input from the user

# using re.search()
#
# import re

# url = input("URL: ").strip()

# import xlsxwriter
#
# def linest(path):
#     workbook = xlsxwriter.workbook(path)
#     sheet = workbook.add_worksheet(name="sparky")
#     spark_styles =[{'range': 'sparkkl!A2:E2',
#                     'markers': True},
#                    {'range': 'sparky!A2:E2',
#                     'type': 'coiumn',
#                     'style': 12}
#                    {'range': 'sparky!A3:E3',
#                     'tyle': 'win_loss',
#                     'negative_points': True}
#                    ]
#     data = [[-5, 5, 3, -2, 0,],
#             [50, 40, 44, 20, 35],
#             ]

print(True and True)