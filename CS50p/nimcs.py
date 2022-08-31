import random


class Hdd:
    # def __init__(self):
    places = ["marian", "jeep", "fortron", "jack", "berlin"]

    @classmethod
    def sort(cls, name):
        first = input("firstname: ")
        surname = input("surname: ")
        name = f"{surname}, {first}".title()
        print(f"congratulations {name}\nYour new home is", random.choice(cls.places).upper())


# hdd = Hdd()
Hdd.sort("name")
