# Original list
original_list = [1, 2, 3, 4, 5]

# Aliasing: another_list is now an alias for original_list
another_list = original_list

# Modifying the alias will affect the original list
another_list.append(6)

# Both lists will show the same content
print("Original list:", original_list)
print("Another list:", another_list)


############################################

# Original list
original_list = [1, 2, 3, 4, 5]

# Using append to add an element to the list
append_list = original_list.copy()
append_list.append([6, 7])
print("After append:")
print("Original list:", original_list)
print("Append list:", append_list)

# Using extend to add elements to the list
extend_list = original_list.copy()
extend_list.extend([6, 7])
print("\nAfter extend:")
print("Original list:", original_list)
print("Extend list:", extend_list)


############################################
num = 10

if num > 0:
    print("Positive number")
else:
    if num == 0:
        print("Zero")
    else:
        print("Negative number")


############################################

# Dictionary to store student names and their grades
student_grades = {}

def add_student():
    student_name = input("Enter the student's name: ")
    if student_name in student_grades:
        print(f"{student_name} is already in the system.")
    else:
        student_grades[student_name] = []
        print(f"{student_name} has been added.")

def add_student_grade():
    student_name = input("Enter the student's name: ")
    if student_name not in student_grades:
        print(f"{student_name} is not in the system. Please add the student first.")
        return
    
    grade = input("Enter the student's grade: ")
    student_grades[student_name].append(grade)
    print(f"Grade {grade} has been added for {student_name}.")

def print_student_grades():
    student_name = input("Enter the student's name to retrieve grades: ")
    
    if student_name in student_grades:
        print(f"{student_name}'s grades: {', '.join(student_grades[student_name])}")
    else:
        print("Student not found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add student")
        print("2. Add student grade")
        print("3. Print student grades")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            add_student_grade()
        elif choice == '3':
            print_student_grades()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#    main()


###############################################

# Global variable
global_var = "I am a global variable"

def demonstrate_scope():
    local_var = "I am a local variable"
    print("Inside function:")
    print(local_var)  # Local variable
    print(global_var)  # Global variable

def modify_global():
    global global_var
    global_var = "I have been modified globally"

print("Before modifying global variable:")
demonstrate_scope()

modify_global()

print("\nAfter modifying global variable:")
demonstrate_scope()


#######################################

class StudentGrades:
    def __init__(self):
        self.student_grades = {}

    def add_student(self):
        student_name = input("Enter the student's name: ")
        if student_name in self.student_grades:
            print(f"{student_name} is already in the system.")
        else:
            self.student_grades[student_name] = []
            print(f"{student_name} has been added.")

    def add_student_grade(self):
        student_name = input("Enter the student's name: ")
        if student_name not in self.student_grades:
            print(f"{student_name} is not in the system. Please add the student first.")
            return
        
        grade = input("Enter the student's grade: ")
        self.student_grades[student_name].append(grade)
        print(f"Grade {grade} has been added for {student_name}.")

    def print_student_grades(self):
        student_name = input("Enter the student's name to retrieve grades: ")
        
        if student_name in self.student_grades:
            print(f"{student_name}'s grades: {', '.join(self.student_grades[student_name])}")
        else:
            print("Student not found.")

def main():
    student_grades = StudentGrades()
    
    while True:
        print("\nOptions:")
        print("1. Add student")
        print("2. Add student grade")
        print("3. Print student grades")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_grades.add_student()
        elif choice == '2':
            student_grades.add_student_grade()
        elif choice == '3':
            student_grades.print_student_grades()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()