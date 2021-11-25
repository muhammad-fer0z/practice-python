def check_student_grade(student_marks):
    if student_marks < 50:
        return "F"
    elif 50 <= student_marks < 65:
        return "C"
    elif 65 <= student_marks < 75:
        return "B"
    elif 75 <= student_marks < 90:
        return "A"
    else:
        return "A+"
