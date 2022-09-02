from dataclasses import dataclass


@dataclass
class Student:
    # all this is not required in data classes:
    # def __init__(self, name, school_id, gpa):
        # self.name = name
        # self.school_id = school_id
        # self.gpa = gpa
        
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f"Name: {self.name}\nschool id: {self.school_id}\nGPA: {self.gpa}\n"


def main():
    aiden = Student("Aiden", "1", 4.0)
    print(aiden)

    karen = Student("Karen", "3928293", 1.49)
    print(karen)


if __name__ == "__main__":
    main()
