# Day 1 - Python Fundamentals

student_name = input("Enter student name:")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:"))

#TODO:
def calculate_percentage():
    total(marks_comm+marks_math+marks_python)
    percentage=(total/300)*100
    return percentage

#Create a function to calculate the percentage
print("\n -- Result --")
print("Student:", student_name)
print("Percentage",percentage)
