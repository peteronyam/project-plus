# # from FIO
# # import csv
# #
# # marks = []
# #
# # with open("unical.csv") as file:
# #     reader = csv.DictReader(file)
# #     for row in reader:
# #         marks.append({"name": row["name"], "score": row["score"], "grade": row["grade"], "remark": row["remark"]})
# #
# #
# # for mark in sorted(marks, key=lambda mark: mark["grade"], reverse=True):
# #     print(f"{mark['name']} you scored {mark['score']} with Grade {mark['grade']}\n"
# #           f"Congratulations, {mark['name']}\n"
# #           f"you {mark['remark']}")
#
# # writing csv files from the code
#
# # name = input("what is your name? ")
# # score = int(input("what is your test score? "))
#
# # with open("rom.csv", "a") as file:
# #     writer = csv.writer(file)
# #     writer.writerow([name, score])
# #
# # # using the dictionary writer
# # with open("rom.csv", "a") as file:
# #     writer = csv.DictWriter(file, fieldnames=["name", "score"])
# #     writer.writerow({"name": name, "score": score})
#
# # working with img files
# import sys
#
# from PIL import Image
#
# img = []
#
# for arg in sys.argv[1:]:
#     img = Image.open(arg)
#     img.append(img)
#
# img[0].save(
#     "cost.gif", save_all=True, append_images=[img[1]], duration=200, loop=0
# )
#
# size = (128, 128)
#
# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.thumbnail(size)
#                 im.save(outfile, "JPEG")
#         except OSError:
# #             print("cannot create thumbnail for", infile)
# import os, sys
# from PIL import Image
#
# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if outfile != infile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("unable to create", infile)
# print(infile)
# twitteer
# import math


# def main(number):
#     math = number ** 2
#     print(f"the square root of {number} is {math.sqrt(number)}")
#
#
# def math(*args):
#     return sum(args)
#
#
# main(8)
