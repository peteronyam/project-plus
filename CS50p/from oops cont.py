class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def tick(cls):
        name = input("Name: ").title()
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.tick()
    print(student)


if __name__=="__main__":
    main()