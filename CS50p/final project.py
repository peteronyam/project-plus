# # students = [
# #     {"name": "mary", "house": "marian"},
# #     {"name": "jammy", "house": "marian"},
# #     {"name": "account", "house": "lagos"},
# #     {"name": "becky", "house": "kebbi"},
# #     {"name": "tobi", "house": "ibadan"},
# #     {"name": "temz", "house": "lagos"},
# #     {"name": "test", "house": "ibadan"}
# #
# # ]
# #
# # houses = []
# # for student in students:
# #     if student["house"] not in houses:
# #         houses.append(student["house"])
# #
# #
# # for house in sorted(houses):
# #     print(house)
# #
# # modifying the above code using set
#
# # students = [
# #     {"name": "mary", "house": "marian"},
# #     {"name": "jammy", "house": "marian"},
# #     {"name": "account", "house": "lagos"},
# #     {"name": "becky", "house": "kebbi"},
# #     {"name": "tobi", "house": "ibadan"},
# #     {"name": "temz", "house": "lagos"},
# #     {"name": "test", "house": "ibadan"}
# #
# # ]
# #
# # houses = set()
# # for student in students:
# #    houses.add(student["house"])
# #
# # for house in sorted(houses):
# #     print(house)
#
#
# # bank bal
# balance = 0
#
#
# def main():
#     # print("Balance:", balance)
#     deposit(100)
#     withdraw(20)
#     print("Balance:", balance)
#
#
#
# def deposit(n):
#     global balance
#     balance += n
#
#
# def withdraw(n):
#     global balance
#     balance -= n
#
#
#
# if __name__=="__main__":
#     main()


# class Account:
#     def __init__(self):
#         self._balance = 0
#
#     @property
#     def balance(self):
#         return self._balance
#
#     def deposit(self, n):
#         self._balance += n
#
#     def withdraw(self, n):
#         self._balance -= n
#
#
# def main():
#     account = Account()
#     print("Balance:", account.balance)
#     account.deposit(100)
#     account.withdraw(30)
#     print("Balance:", account.balance)
#
#
# if __name__ == "__main__":
#     main()
#
#
# # meows.py
#
# class Cat:
#     MEOWS = 3
#
#     def meows(self):
#         for _ in range(Cat.MEOWS):
#             print("meows")
#
#
# cat = Cat()
# cat.meows()


# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")
#
#
# number = int(input("Number: "))
# meows: str = meow(number)
# print(meows)

# clearing the error code from the above code
# def meow(n: int) -> str:
#     """
#     :param n: Number of times to meow
#     :type n: int
#     :raise\ TypeError: if n is not an int
#     :return: A string of n mweow, one per line
#     :rtype: str
#     """
#     return "meow\n" * n
#
#
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

# using the command line
# import sys
#
# if len(sys.argv) == 1:
#     print("hey")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("hey, there")
# else:
#     print("user: iconic")

# using argparse

# import argparse
#
#
# parser = argparse.ArgumentParser(description="get his attention")
# parser.add_argument("-n", default=2, help="number of time to to call", type=int)
# args = parser.parse_args()
#
# for _ in range(int(args.n)):
#     print("hey, there!")


# unpacking

# first, _ = input("what is your name? ").title().split(" ")
# print(f"hello, {first}")

# def total_value(sand, water, jar):
#     return (sand * 20 + water) * 30 + jar
# sum = [100, 60, 150]
#
# print(total_value(100, 5000, 0), "jar")

# modifying the code above
# def total_value(sand, water, jar):
#     return (sand * 20 + water) * 30 + jar
# sum = [100, 54, 165]
# xem = {"sand": 300, "water": 599, "jar": 509}
#
# print(total_value(sum[0], sum[1], sum[2]), "jar")
# # unpacking sum
# print(total_value(*sum), "jar")
# print(total_value(sand=1000, water=60, jar=98), "jar")
# print(total_value(**xem), "jar")

# using *args and **kwargs
# def kley(*args, **kwargs):
#     print("Positional:", args)
#
# kley(1920, 201, 5948)

# new

# def main():
#     hey("this", "is", "final", "project,", "CS50")
#
#
# def hey(*words):
#     upper = []
#     for word in words:
#         upper.append(word.upper())
#     print(*upper)
#
#
# if __name__ == "__main__":
#     main()
#
# # using map
# def main():
#     hey("this", "is", "final", "project,", "CS50")
#
#
# def hey(*words):
#     up = map(str.upper, words)
#     print(*up)
#
#
# if __name__ == "__main__":
#     main()

# # list comprehensions
# def main():
#     hey("this", "is", "final", "project,", "CS50")
#
#
# def hey(*words):
#     up = [word.upper() for word in words]
#     print(*up)
#
#
# if __name__ == "__main__":
#     main()
#
#
# # sorting students  who passed their exams
#
#
# students = [
#     {"name": "james cla", "score": 70, "grade": "A", "remark": "passed"},
#     {"name": "quency", "score": 94, "grade": "A", "remark": "passed"},
#     {"name": "laseen", "score": 62, "grade": "C", "remark": "passed"},
#     {"name": "johny", "score": 38, "grade": "D", "remark": "passed"},
#     {"name": "gasp", "score": 60, "grade": "B", "remark": "passed"},
#     {"name": "heck", "score": 38, "grade": "E", "remark": "passed"},
#     {"name": "clark", "score": 28, "grade": "F", "remark": "passed"},
#     {"name": "ned", "score": 48, "grade": "D", "remark": "passed"},
#     {"name": "mardy", "score": 84, "grade": "B", "remark": "passed"},
#     {"name": "naty", "score": 88, "grade": "A", "remark": "passed"},
#     {"name": "venis", "score": 60, "grade": "B", "remark": "passed"},
#     {"name": "becky", "score": 72, "grade": "A", "remark": "passed"},
#     {"name": "joe", "score": 40, "grade": "D", "remark": "passed"},
#     {"name": "mark", "score": 50, "grade": "C", "remark": "passed"},
#     {"name": "union", "score": 90, "grade": "A", "remark": "passed"},
#     {"name": "jadden", "score": 56, "grade": "C", "remark": "passed"},
#     {"name": "jack", "score": 80, "grade": "A", "remark": "passed"},
#     {"name": "niki", "score": 60, "grade": "B", "remark": "passed"},
#     {"name": "naomi", "score": 25, "grade": "F", "remark": "passed"},
# ]
#
# As = [
#     student["name"] for student in students if student["grade"] == "A"
# ]
#
# for a in sorted(As):
#     print(a)
# print(f"congratulations, if you can find your "
#       f"name on the list above\nYou have successfully passed the "
#       f"test with distinction")
#
#
# # using filter
#
# students = [
#     {"name": "james cla", "score": 70, "grade": "A", "remark": "passed"},
#     {"name": "quency", "score": 94, "grade": "A", "remark": "passed"},
#     {"name": "laseen", "score": 62, "grade": "C", "remark": "passed"},
#     {"name": "johny", "score": 38, "grade": "D", "remark": "passed"},
#     {"name": "gasp", "score": 68, "grade": "B", "remark": "passed"},
#     {"name": "heck", "score": 38, "grade": "E", "remark": "passed"},
#     {"name": "clark", "score": 28, "grade": "F", "remark": "passed"},
#     {"name": "ned", "score": 48, "grade": "D", "remark": "passed"},
#     {"name": "mardy", "score": 84, "grade": "B", "remark": "passed"},
#     {"name": "naty", "score": 88, "grade": "A", "remark": "passed"},
#     {"name": "venis", "score": 66, "grade": "B", "remark": "passed"},
#     {"name": "becky", "score": 72, "grade": "A", "remark": "passed"},
#     {"name": "joe", "score": 40, "grade": "D", "remark": "passed"},
#     {"name": "mark", "score": 50, "grade": "C", "remark": "passed"},
#     {"name": "union", "score": 90, "grade": "A", "remark": "passed"},
#     {"name": "jadden", "score": 56, "grade": "C", "remark": "passed"},
#     {"name": "jack", "score": 80, "grade": "A", "remark": "passed"},
#     {"name": "niki", "score": 64, "grade": "B", "remark": "passed"},
#     {"name": "naomi", "score": 25, "grade": "F", "remark": "passed"},
# ]
#
#
# def is_B(s):
#     return s["grade"] == "B"
#
#
# Bs = filter(is_B, students)
#
# for B in sorted(Bs, key=lambda s: s["score"]):
#     print(B["name"])
#

# dictionary comprehension

# staffs = ["thamos", "benny", "yestor"]
#
# # unical = [{"name": staff, "field": "unica"} for staff in staffs]
# unical = {staff: "unica"  for staff in staffs}
# print(unical)

# # attaching numbers to a list of students
#
# kind = ["name", "james cla", "score", "grade", "A", "remark", "passed"]
#
# for i in range(len(kind)):
#     print(i + 1, kind[i])


# using enumerate

# kind = ["name", "james cla", "score", "grade", "A", "remark", "passed"]
#
# for i, kind in enumerate(kind):
#     print(i + 1, kind)

# #using generators
# #sleep.py
# def main():
#     n = int(input("what is n? "))
#     for i in range(n):
#         print("HR" * i)
#
#
# if __name__ =="__main__":
#     main()

# # modifying sleepy.py
# def main():
#     n = int(input("what is n? "))
#     for i in range(n):
#         print(shop(i))
#
#
# def shop(n):
#     return "HR" * n
#
#
# if __name__=="__main__":
#     main()
#
# #remodifying

# def main():
#     n = int(input("what is n? "))
#     for s in shop(n):
#         print(s)
#
#
# def shop(n):
#     store = []
#     for i in range(n):
#         store.append("HR" *(i + 1))
#     return store
#
#
# if __name__=="__main__":
#     main()

# # modifying the above so the memory can carry
#
# def main():
#     n = int(input("what is n? "))
#     for s in shop(n):
#         print(s)
#
#
# def shop(n):
#     for i in range(n):
#         yield "HR" * i
#
#
# if __name__=="__main__":
#     main()

# say.py
# text to speach

import cowsay
import pyttsx3

letme = pyttsx3.init()
this = input("what? ")
cowsay.dragon(this)
letme.say(this)
letme.runAndWait()