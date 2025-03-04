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


