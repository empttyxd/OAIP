from typing import List, Iterator


class Student:
    def __init__(self, first_name: str, last_name: str, average_grade: float):
        self.first_name = first_name
        self.last_name = last_name
        self.average_grade = average_grade

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} — средний балл: {self.average_grade:.2f}"


class StudentGroup:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def __iter__(self) -> Iterator[Student]:
        return StudentGroupIterator(self.students)


class StudentGroupIterator:
    def __init__(self, students: List[Student]):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Student:
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


if __name__ == "__main__":
    group = StudentGroup("ПИ-41")

    group.add_student(Student("Иван", "Петров", 4.35))
    group.add_student(Student("Анна", "Смирнова", 4.87))
    group.add_student(Student("Дмитрий", "Соколов", 3.92))
    group.add_student(Student("Екатерина", "Кузнецова", 4.61))
    group.add_student(Student("Михаил", "Иванов", 4.12))

    print(f"Группа: {group.group_name}")
    print("Студенты:\n")

    for student in group:
        print(student)

    print("\n" + "-" * 50)

    print("Список отличников (балл ≥ 4.5):")
    excellent = [str(s) for s in group if s.average_grade >= 4.5]
    for line in excellent:
        print("  " + line)
