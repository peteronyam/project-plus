# def main():
#     student = get_student()
#     if student[0] == "peter":
#         student[1] = "cross river"
#     print(f"{student[0].upper()} from {student[1].upper()}")
#
#
# def get_student():
#     name = input("name: ")
#     house = input("house: ")
#     return [name, house]
#
#
# if __name__=="__main__":
#     main()
#
#
# # using a dictionary to solve
# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")
#
#
# def get_student():
#     student = {}
#     student["name"] = input("name: ")
#     student["house"] = input("house: ")
#     return student
#
#
# if __name__=="__main__":
#     main()

# we can aswell use this method

# def main():
#     student = get_student()
#     if student["name"] == "peter":
#         student["house"] = "united kingdom"
#     print(f"{student['name']} from {student['house']}")
#
#
# def get_student():
#     name = input("name: ")
#     house = input("house: ")
#     return {"name": name, "house": house}
#
#
# if __name__=="__main__":
#     main()
#

# using classes
# class Student():
#     ...
#
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
#
# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student
#
#
# if __name__=="__main__":
#     main()

# modifying with classes and checking the correctness and data


class Student():
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["cross river state", "delta state", "abuja state", "kogi state"]:
            raise ValueError("Invalid state")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__=="__main__":
    main()