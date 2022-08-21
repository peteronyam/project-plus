# from FIO
import csv
#
# marks = []
#
# with open("unical.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         marks.append({"name": row["name"], "score": row["score"], "grade": row["grade"], "remark": row["remark"]})
#
#
# for mark in sorted(marks, key=lambda mark: mark["grade"], reverse=True):
#     print(f"{mark['name']} you scored {mark['score']} with Grade {mark['grade']}\n"
#           f"Congratulations, {mark['name']}\n"
#           f"you {mark['remark']}")

# writing csv files from the code

name = input("what is your name? ")
score = int(input("what is your test score? "))

with open("rom.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, score])