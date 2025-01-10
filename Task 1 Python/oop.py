students = {}

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


def add(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades = list(map(float, input("Enter student grades: ").split(',')))
    students[name] = Student(name, age, grades)
    print(f"Student '{name}' added successfully.")

def view(students):
    if not students:
        print("No students available.")
        return
     
    for student in students.values():
        student.display_details()
        print(f"Average Grade: {student.calculate_average_grade():.2f}")
            
def update(students):
    name = input("Enter the name of the student to update: ")
    if name not in students:
        print(f"Student '{name}' not found.")
        return
    else:
        age = int(input("Enter new age: "))
        grades = list(map(float, input("Enter new grades: ").split(',')))
        students[name] = Student(name, age, grades)
        print(f"Student '{name}' updated successfully.")

def delete(students):
    name = input("Enter the name of the student to delete: ")
    if name  in students:
        del students[name]
        print(f"Student '{name}' deleted successfully.")
    else:
        print(f"Student '{name}' not found.")



while True:
    print(" 1. Add Student \n 2. View Student \n 3. Update Student \n 4. Delete Student \n 5. Exit ")
    choice = input("Enter your choice: ")
    if choice == '1':
        add(students)
    elif choice == '2':
        view(students)
    elif choice == '3':
        update(students)
    elif choice == '4':
        delete(students)
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")