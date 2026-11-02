class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student) -> None:
        cls.student_list.append(student)

class Student:
    def __init__(self, student_id, name, department) -> None:
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False

        StudentDatabase.add_student(self)

    def enroll_student(self) -> None:
        if self.__is_enrolled:
            print("Student is already enrolled.")
        else:
            self.__is_enrolled = True
            print("Student enrolled successfully.")