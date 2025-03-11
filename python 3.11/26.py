class Student:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append({"name": name, "grades": []})

    def add_grade(self, name, grade):
        for student in self.students:
            if student["name"] == name:
                student["grades"].append(grade)
                break

    def show_students(self):
        for student in self.students:
            print(f"{student['name']} - Oceny: {student['grades']}")


s = Student()
s.add_student("Anna")
s.add_student("Kasia")
s.add_grade("Anna", 5)
s.add_grade("Kasia", 4)
s.show_students() 
