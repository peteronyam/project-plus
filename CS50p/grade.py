# score = int(input("score: "))
# #
# if score >= 70 and score <= 100:
#     print("Grade: A")
# elif score >= 60 and score < 70:
#     print("Grade: B")
# elif score >= 50 and score < 60:
#     print("Grade: C")
# elif score >= 40 and score < 50:
#     print("Grade: D")
# elif score >= 31 and score < 40:
#     print("Grade: E")
# elif score < 31:
#     print("Grade: F")
#
# # increasing readability
#
# # if 70 <= score <= 100:
#     print("Grade: A")
# elif 60 >= score < 70:
#     print("Grade: B")
# elif 50 <= score < 60:
#     print("Grade: C")
# elif 40 <= score < 50:
#     print("Grade: D")
# elif 31 <= score < 40:
#     print("Grade: E")
# elif score < 31:
#     print("Grade: F")
#
# # remodifying it
#
# if score >= 70:
#     print("Grade: A")
# elif score >= 60:
#     print("Grade: B")
# elif score >= 50:
#     print("Grade: C")
# elif score >= 40:
#     print("Grade: D")
# elif score >= 31:
#     print("Grade: E")
# else:
#     print("Grade: F")

def main():
    y = int(input("what is y? "))
    if is_even(y):
        print("even")
    else:
        print("odd")
    g = int(input("what's g? "))
    if maker(g):
        print("time")
    else:
        print("start now")

def maker(l):
    if l % 3 == 0:
        return True
    else:
        return False

# making the code look cleaner and readable

def is_even(n):
    return True if n % 2 == 0 else False
# better
def is_even(n):
    return (n % 2 == 0)

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
# y = int(input("what is y? "))
#
# if y % 2 == 0:
#     print("Even")
# else:
#     print("Odd")