class StudentRegistry:
    students = []

    @staticmethod
    def add_student(name):
        if name not in StudentRegistry.students:
            StudentRegistry.students.append(name)
            return 'student is add'
        else:
            return 'student already in the list'

    @staticmethod
    def get_student_count():
        return len(StudentRegistry.students)

    @staticmethod
    def get_all_students():
        return StudentRegistry.students

    @classmethod
    def clear_registry(cls):
        cls.students.clear()


print(StudentRegistry.add_student('Max'))
print(StudentRegistry.add_student('Jack'))
print(StudentRegistry.add_student('Besedin'))
print(StudentRegistry.add_student('Max'))
print(StudentRegistry.get_student_count())
print(StudentRegistry.get_all_students())
StudentRegistry.clear_registry()
print(StudentRegistry.get_all_students())
