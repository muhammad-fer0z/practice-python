from student import Student
from grade import check_student_grade

# initialize variable
student_id = None
student_name = None
student_marks = None

while True:
    try:
        # take input from user
        student_id = str(input("Enter your student ID: "))
        student_name = str(input("Enter your student name: "))
        student_marks = int(input("Enter your total marks: "))

        # check if mark is greater than 0 and also less than 100
        while True:
            if student_marks > 100 or student_marks < 0:
                student_marks = int(input("Please ReEnter your total marks (Make sure your marks between 0 - 100): "))
                continue
            else:
                break

    except ValueError:
        print("Something Went Wrong!!!")
        continue
    else:
        break

# create student object
student = Student(student_id, student_name, student_marks)

# check student grade
student_grade = check_student_grade(student_marks)

# print student details
print(f"Hi ! {student.get_student_name()} your grade is {student_grade}.")
