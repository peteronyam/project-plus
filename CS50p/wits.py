# #talking about inheritance in python oops
#
# class Common:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#
#
# class Student(Common):
#     def __init__(self, name, house):
#         super().__init__(name)
#         self.name = name
#         self.house = house
#
#         ...
#
#
# class Professor(Common):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.name = name
#         self.subject = subject
#         ...
#
#
# common = Common("vestrous")
# student = Student("mary", "marian")
# professor = Professor("stephen", "Technology of the future")


# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts
#
#     def __str__(self):
#         return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} knuts"
# painter = Vault(100, 500, 430)
# print(painter)
#
# font = Vault(200, 50, 90)
# print(font)
#
# # to combine to vaults of two
# galleons = painter.galleons + font.galleons
# sickles = painter.sickles + font.sickles
# knuts = painter.knuts + font.knuts
#
# total = Vault(galleons, sickles, knuts)
# print(total)

# mdifying and simplifying the code with opertor overlaoding

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} knuts"


    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


painter = Vault(100, 500, 430)
print(painter)

font = Vault(200, 50, 90)
print(font)

# to combine to vaults of two using the overload operator


total = painter + font
print(total)