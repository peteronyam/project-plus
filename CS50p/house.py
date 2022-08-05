name = input("what is your name? ")

if name == "james" or name == "nath" or name == "line":
    print("marian Road")
elif name == "harry":
    print("atimbo")
elif name == "clark":
    print("zone 6")
elif name == "kenny":
    print("etta agbo")
elif name == "virtue":
    print("time manto")
else:
    print("who? please")

# using to match key

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