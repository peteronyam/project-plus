# def students(**kwargs: object) -> object:
def james(funds=None):
    kind = input("Type in your name to see your examination score: ")
    name = funds
    score = 70
    grade = "A"
    if kind == name:
        return f"Congratulations {name}.\nYou scored {score} on your spanish test with Grade {grade}"
    else:
        return f"Hey! {kind}\nName missing\nCheck the general office for documentation"


print(james(funds="clak"))


def femi(me=None):
    kin = input("Type in your name to see your examination score: ")
    nam = me
    scor = '{0:8} | {1:9}'.format('score', 'Grade')
    fr = '{0:8} | {1:9}'.format(70, 'A')
    # grad = "B"
    if kin == nam:
        return f"Congratulations {nam}.\n{scor}\n{fr}\nsee your result on your spanish test above"
    else:
        return f"Hey! {kin}\nName missing\nCheck the general office for documentation"

print(femi(me="cv"))


# for key, value in **kwargs.items():
#     print("%s || %s" % (key, value))
#
# time = students(name=input('Type in your name to see your examination score: '), score='75', Grade='B')
# name = "%s" % (students())
#
# sur_name = input("SurName: ")
# first_name = input("first name: ")
# #
# name = "%s, %s" % (sur_name, first_name)
#
#
# def score(num):
#     x = num
#     if x >= 70:
#         return f"Congratulations {name}.\nYou scored {x} on your spanish test"
#     else:
#         return f"Hey! {name}.\nyour score didn't meet the minimum requirement for the test.\nYou might want to sit for the next session examinations "


# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("students do.")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0, 0))