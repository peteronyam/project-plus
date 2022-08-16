# from tabulate import tabulate_formats
# import tabulate
#
# students = ["mady", "harry", "toms", "guest"]
#
# for student in students:
#     print(students)
# print(*students)
# print(students[0])
# print(students[1])
# print(students[2])
# print(len((students)))
# # disctionaries
# studentt = {
#     "maddy": "marian",
#     "harry": "fiesta",
#     "toms":"etta abgo",
#     "guest": "high way",
#     "manna": "crutech"
# }
#
# print(studentt["maddy"])
# print(studentt["harry"])
# print(studentt["toms"])
# print(studentt["guest"])
# print(studentt["manna"])
#
# for student in studentt:
#     print(student, studentt[student], sep=",")

students  = [
    {"name": "james", "score": 78, "Grade": "A"},
    {"name": "manna", "score": 68, "Grade": "B"},
    {"name": "clark", "score": 54, "Grade": "C"},
    {"name": "sam", "score": 98, "Grade": "A"},
    {"name": "jark", "score": 60, "Grade": "B"},
    {"name": "kiev", "score": 44, "Grade": None}
]
for student in students:
    print(student["name"], student["score"], student["Grade"], sep=",")

