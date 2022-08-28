while True:
    try:
        email = input("type in your email: ").strip()

        if "@" and "." in email:
            print("valid")
            break
        else:
            print("invalid\nplease re-enter a\
valid email to complete your registration")
    except SyntaxError:
        print("not now")
# next step, we will need to save inputs from users


# \d = decimal digit
# \D = not a decimal digit
# \s = whitespace characters
# \S = not a whitespace character
# \w = word character as well as numbers and the underscore
# \W = not a word character
