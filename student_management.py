class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.get_id() == student_id:
                return student
        return None


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        
        StudentDatabase.add_student(self)

    def get_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled == True:
            print(f"{self.__name} is already enrolled!")
        else:
            self.__is_enrolled = True
            print(f"{self.__name} enrolled successfully.")

    def drop_student(self):
        if self.__is_enrolled == False:
            print(f"{self.__name} is not enrolled, can't drop!")
        else:
            self.__is_enrolled = False
            print(f"{self.__name} dropped successfully.")

    def view_student_info(self):
        if self.__is_enrolled:
            status = "Enrolled"
        else:
            status = "Not Enrolled"

        print(f"ID: {self.__student_id}, Name: {self.__name}, "
              f"Department: {self.__department}, Status: {status}")


# students
Student("101", "Ashik", "CSE", True)
Student("102", "Samir", "EEE")
Student("103", "Rahim", "BBA", True)
Student("104", "Karim", "CSE")


# menu
while True:
    print("\n----- Student Management -----")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(StudentDatabase.student_list) == 0:
            print("No students found.")
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == "2":
        sid = input("Enter student ID: ")
        student = StudentDatabase.find_student(sid)
        if student == None:
            print("Invalid student ID!")
        else:
            student.enroll_student()

    elif choice == "3":
        sid = input("Enter student ID: ")
        student = StudentDatabase.find_student(sid)
        if student == None:
            print("Invalid student ID!")
        else:
            student.drop_student()

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid choice, try again.")