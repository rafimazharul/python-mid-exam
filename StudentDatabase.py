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

    def drop_student(self) -> None:
        if not self.__is_enrolled:
            print("Student is not enrolled.")
        else:
            self.__is_enrolled = False
            print("Student dropped successfully.")

    def view_student_info(self) -> None:
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")

        if self.__is_enrolled:
            print("Enrollment Status: Enrolled")
        else:
            print("Enrollment Status: Not Enrolled")