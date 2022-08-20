# names = []
#
# # for _ in range(3)
# #     name = input("what is your name? ")
# #     names.append(name)
#
# # making it shorter and readable
# for _ in range(3):
#     names.append(input("what is your name? "))
#
# # to arrange or sort the name in an alphabetical order
# for name in sorted(names):
#     print(f"hello, {name}")

# # saving the data on our local computer
# stand_name = input("what is your name? ")
#
# file = open("stand_names.txt", "a")
# file.write(f"{stand_name}\n")
# file.close()

# introducing the with keyword
# this will help us to do away with the file.close() code
# here comes the new formated code
# stand_name = input("what is your name? ")

# with open("stand_names.txt", "a") as file:
#     file.write(f"{stand_name}\n")


# code to read an existing test file
#
# with open("stand_names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# beginning from skratch
# stand_names = []


# with open("stand_names.txt") as file:
#     for line in file:
#         stand_names.append(line.rstrip())
#
# for name in sorted(stand_names):
#     print(f"hello, {name}")

# for csv file
# from tabulate import tabulate
students = []

# with open('students.csv') as file:
#     for line in file:
#         students.append(line.rstrip())
#
# for name in sorted(students):
#     print({name})

# sorting the file itself
# formating the above code

# with open("students.csv") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())
#
# # sorting in reverse
# with open("students.csv") as file:
#     for line in sorted(file, reverse=True):
#         print("hello,", line.rstrip())

# to read a csv file @unical.csv
# # from the instructor
# with open("unical.csv") as file:
#     for line in file:
#         student_row = line.rstrip().split(",")
#         print(f"{student_row[0]} you scored {student_row[1]}\n"
#               f" with Grade {student_row[2]}\n"
#               f"Congratulations, {student_row[0]}\n"
#               f"you {student_row[3]}")
#
# # modifying for me
# with open("unical.csv") as file:
#     for line in file:
#         student_row = line.rstrip().split(",")
#         print(f"{student_row[0]} you scored {student_row[1]} with Grade {student_row[2]}\n"
#               f"Congratulations, {student_row[0]}\n"
#               f"you {student_row[3]}!")

# remodifying it
#
# with open("unical.csv") as file:
#     for line in file:
#         student_name, scores, Grades, remark = line.rstrip().split(",")
#         print(f"{student_name} you scored {scores} with Grade {Grades}\n"
#               f"Congratulations, {student_name}\n"
#               f"you {remark}!")

# sorting the above code
# mark = []
#
# with open("unical.csv") as file:
#     for line in file:
#         student_name, scores, Grades, remark = line.rstrip().split(",")
#         mark.append(f"{student_name} you scored {scores} with Grade {Grades}\n"
#                       f"Congratulations, {student_name}\n"
#                       f"you {remark}!")
#
# for mark in sorted(mark):
#     print(mark)

# # sorting by an individual key either by grade,
# # student name or score
# marks = []
#
# with open("unical.csv") as file:
#     for line in file:
#         student_name, scores, grades, remark = line.rstrip().split(",")
#         mark = {"student_name": student_name, "scores": scores, "grades": grades, "remark": remark}
#         marks.append(mark)
#
#
# def get_name(mark):
#     return mark["student_name"]
#
#
# def get_score(mark):
#     return mark["scores"]
#
#
# def get_grade(mark):
#     return mark["grades"]
#
# # to sort by score
#
# for mark in sorted(marks, key=get_score, reverse=True):
#     # to sort by grades
#     # for mark in sorted(marks, key=get_grades):
#     # #to sort by students name
#     # for mark in sorted(marks, key=get_name)
#     print(f"{mark['student_name']} you scored {mark['scores']} with Grade {mark['grades']}\n"
#           f"Congratulations, {mark['student_name']}\n"
#           f"you {mark['remark']}")
#
# # re-remodifying the code
marks = []

with open("unical.csv") as file:
    for line in file:
        student_name, scores, grades, remark = line.rstrip().split(",")
        mark = {"student_name": student_name, "scores": scores, "grades": grades, "remark": remark}
        marks.append(mark)

for mark in sorted(marks, key=lambda mark: mark["student_name"], reverse=True):
    print(f"{mark['student_name']} you scored {mark['scores']} with Grade {mark['grades']}\n"
          f"Congratulations, {mark['student_name']}\n"
          f"you {mark['remark']}")

