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

import re
#
# url = input("URL: ").strip()
#
# name_match = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if name_match:
#     print(f"username:", name_match.group(1))
#
# fixing the error from the name_match.group(1 to group(2))

url = input("URL: ").strip()

name_match = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if name_match:
    print(f"username:", name_match.group(2))

# using the :=

url = input("URL: ").strip()

if name_match := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"username:", name_match.group(2))