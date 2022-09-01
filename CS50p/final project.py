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

