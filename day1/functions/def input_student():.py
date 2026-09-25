def input_student():
    student_name = input('enter name of student:')
    marks_python = float(input('enter marks of python:'))
    marks_comm = float(input('enter marks of comm:'))
    marks_math = float(input('enter marks of math:'))
    dict_student_info={
        'name': student_name,
        'marks_python': marks_python,
        'marks_comm': marks_comm,
        'marks_math': marks_math
    }
    return dict_student_info


def calculate_percentage(marks_python, marks_comm, marks_math):
    total = marks_python + marks_comm + marks_math
    percentage = (total / 300) * 100
    return percentage
def calculate grade_percentage


if __name__ == "__main__":
    print("\n..Result..")
    student_info = input_student()
    print(student_info)
    print("student:", student_info["name"])
    percentage = calculate_percentage(
        student_info["marks_python"],
        student_info["marks_comm"],
        student_info["marks_math"]
    )
    print("percentage:", percentage)