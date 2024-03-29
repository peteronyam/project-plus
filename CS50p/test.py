# from calculator import square
#
#
# def main():
#     test_square()
#
#
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared wasn't 4")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared wasn't 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared wasn't 9")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared wasn't 9")
#     try:
#         assert square(-0) == 0
#     except AssertionError:
#         print("0 squared wasn't 0")
#
#
# if __name__ == "__main__":
#     main()

# testing for user inputs
from calculator import hello


def test_new():
    assert hello("peter") == "hello, peter"


# using loops to test multiple values
def test_multiple():
    for name in ["kendrick", "michael", "testimony", "isaac"]:
        assert hello(name) == f"hello, {name}"


def test_default():
    assert hello() == "hello, world"