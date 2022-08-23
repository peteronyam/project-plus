# while True:
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
while True:
    try:

        email = input("type in your email: ").strip()

        username, domain = email.split("@")

        if username and domain.endswith(".com"):
            print("valid")
            break
        else:
            print("invalid")

#         if "@" and "." in email:
#             print("valid")
#             break
#         else:
#             print("invalid\nplease re-enter a\
# valid email to complete your registration")
    except SyntaxError:
        print("not now")