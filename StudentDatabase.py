class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student) -> None:
        cls.student_list.append(student)