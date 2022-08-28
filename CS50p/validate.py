#regular expressions

#while True:
#     try:
#
#         email = input("type in your email: ").strip()
#
#         if "@" and "." in email:
#             print("valid")
#             break
#         else:
#             print("invalid\nplease re-enter a\
# valid email to complete your registration")
#     except SyntaxError:
#         print("not now")
# modifying
import re
# while True:
#     try:
#
#         email = input("type in your email: ").strip()
#
#         username, domain = email.split("@")
#
#         if username and domain.endswith(".com"):
#             print("valid")
#             break
#         else:
#             print("invalid")
#
# #         if "@" and "." in email:
# #             print("valid")
# #             break
# #         else:
# #             print("invalid\nplease re-enter a\
# # valid email to complete your registration")
#     except SyntaxError:
#         print("not now")

# comment convention
# while True:
#     try:
#         email = input("what is your email? ")
#
#         if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
#             print("valid")
#             break
#         else:
#             print("invalid")
#     except SyntaxError:
#         print("time up" )


# adding the \w which means word character and to add .domains

# while True:
#     try:
#         email = input("what is your email? ")
#
#         if re.search(r"^\w+@\w+\.(com|gov|ng|net|edu|org|site)$", email, re.IGNORECASE):
#             print("valid")
#             break
#         else:
#             print("invalid")
#     except SyntaxError:
#         print("time up")

# modifying to accept subdomain

while True:
    try:
        email = input("what is your email? ")

        if re.search(r"^\w+@(\w+\.)\w+\.?(com|gov|ng|net|edu|org|site)$", email, re.IGNORECASE):
            print("valid")
            break
        else:
            print("invalid")
    except SyntaxError:
        print("time up")
# this part (\w+\.)\w+\.?(com|gov|ng|net|edu|org|site) in the
# code represent a domain name or a subdomain


# for a case where te username has a . in it/ the code will look like this

while True:
    try:
        email = input("what is your email? ")

        if re.search(r"^(\w|\.)+@(\w+\.)\w+\.?(com|gov|ng|net|edu|org|site)$", email, re.IGNORECASE):
            print("valid")
            break
        else:
            print("invalid")
    except SyntaxError:
        print("time up")

# using a library to validate email addresses
