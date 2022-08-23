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