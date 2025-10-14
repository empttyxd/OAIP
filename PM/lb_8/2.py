from dataclasses import dataclass
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def full_name(self):
        pass

    @abstractmethod
    def get_id(self):
        pass

@dataclass
class Student(Person):
    first_name: str
    last_name: str
    student_id: int

    def full_name(self):
        return self.first_name, self.last_name

    def get_id(self):
        return self.student_id

@dataclass
class Teacher(Person):
    first_name: str
    last_name: str
    employee_id: int
    courses: str

    def full_name(self):
        return self.first_name, self.last_name

    def get_id(self):
        return self.employee_id


def print_name_id(person):
    for i in person:
        print(f'name: {i.full_name()}, id: {i.get_id()}')


students = [Student('Артем', 'Максимович', 11),
            Student('Анна', 'Сидорова', 12),
            Student('Олег', 'Беседин', 31),
            Student('Петр', 'Павел', 13)]
teachers = [Teacher('Косиняк', 'Камыш', 101, 'польский язык'),
            Teacher('Татьяна', 'Иванова', 102, 'философия'),
            Teacher('Андрей', 'Бледный', 103, 'история')]

print('Студенты:')
print_name_id(students)
print('Учителя:')
print_name_id(teachers)
