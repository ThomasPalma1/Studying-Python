from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.names = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
