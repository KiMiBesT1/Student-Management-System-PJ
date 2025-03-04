class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.courses = []
        self.grades = {}
        self.attendance = {}

    def register_course(self, course_name):
        self.courses.append(course_name)
        self.grades[course_name] = None
        self.attendance[course_name] = 0

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.grades[course_name] = grade
        else:
            print("You are not registered for this course.")

    def mark_attendance(self, course_name):
        if course_name in self.courses:
            self.attendance[course_name] += 1
        else:
            print("You are not registered for this course.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print("Courses Registered:")
        for course in self.courses:
            print(f"- {course}")
        print("Grades:")
        for course, grade in self.grades.items():
            print(f"- {course}: {grade}")
        print("Attendance:")
        for course, attend in self.attendance.items():
            print(f"- {course}: {attend} times")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, email, password):
        if email in self.students:
            print("Student with this email already exists.")
        else:
            self.students[email] = Student(name, email, password)
            print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("Student List:")
            for student in self.students.values():
                print(student)

    def update_student(self, email, name=None, password=None):
        if email in self.students:
            if name:
                self.students[email].name = name
            if password:
                self.students[email].password = password
            print(f"Student with email {email} updated successfully!")
