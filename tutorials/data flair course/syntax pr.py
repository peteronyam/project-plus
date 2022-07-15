a = 10
ai = "Hi \nHow are you?"
print(a)
print(ai)


def scan():
    if 2 > 3:
        print("yes")
    else:
        print("Input Error")


print(scan())
pass
print("""
Good morning, sir
this is how i want the above code to appear but it's not working , please check it out for me
this is how 
first, How are you?
secondly, input your responds
thirdly, input your name and you will be able to see a message on your screen
then if your score is 70 and above you should see a message saying you are blah blah blah
while if your score is less than 70 you should see a message saying you should try again
""")
name = input("type in your name here to know your examination score ")
# score = 96


def score():
    if score < 70:
        print("your score didn't meet the minimum requirement for the test")
    else:
        print("you are blah blah blah")


s = "I'm fine"
print(f"{ai}\n{s} \nHI, {name}\nYou scored {score} on the spanish test")

# Slicing is the process of obtaining a portion (substring) of a string by using its indices
# string[start:end:step]
my_string = "This bu MY string!"
print(my_string[0:7])  # A step of 1
print(my_string[0:13:2])  # A step of 2
print(my_string[0:6:5])  # A step of 5

my_string = "This is MY string!"
print(my_string[13:2:-1])  # Take 1 step back each time
print(my_string[17:0:-2])  # Take 2 steps back. The opposite of what happens in the slide above

my_string = "This is MY string!"
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)

ring1 = "525system"
ring2 = "i like %s" % "Python"

print(ring1)
print(ring2)
rin = "%s and %s" % (ring1, ring2)
nam = "%s\n%i" % (ring1, 525)
print(rin)
print(nam)
s = 4 * 5
p = -24 + 5
print("%s %s = %s" % (s, p, s+p))

