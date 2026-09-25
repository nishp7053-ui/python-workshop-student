# TODO
# Create a function called calculate_percentage()



def calculate_percentage():
    total(marks_comm+marks_math+marks_python)
    percentage=(total/300)*100
    return percentage
    return percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
if __name__ == "__main__":
    print("\n..Result..")
    student_info = input_student()
    print(student_info)
    print("student:", student_info["name"])
    percentage = calculate_percentage(
        student_info["marks_python"],
        student_info["marks_comm"],
        student_info["marks_math"],
    )
    print("percentage:", percentage)
    grade = calculate_grade(percentage)
    print("grade:", grade) 

# It should :
# 1. Accept three marks
# 2. Calculate the total
# 3. Calculate the percentage
# 4. Return the percentage



#TODO:
def calculate_percentage():
    total(marks_comm+marks_math+marks_python)
    percentage=(total/300)*100
    return percentage



