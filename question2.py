def calculate_grade(percentage):
    if percentage < 40:
        grade = 'D'
    elif percentage < 60:
        grade = 'C'
    elif percentage < 80:
        grade = 'B'
    else:
        grade = 'A'
    return grade

def print_grade_card(stu_code, name, maths, physics, chemistry, english):
    total_marks = maths + physics + chemistry + english
    percentage = total_marks / 4
    grade = calculate_grade(percentage)

    print("\n" + "="*45)
    print(" "*12 + "STUDENT GRADE CARD")
    print("="*45)
    print(f"Student Code : {stu_code}")
    print(f"Name         : {name}")
    print("-"*45)
    print(f"Maths        : {maths}")
    print(f"Physics      : {physics}")
    print(f"Chemistry    : {chemistry}")
    print(f"English      : {english}")
    print("-"*45)
    print(f"Total Marks  : {total_marks}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print("="*45)
stu_code = input("Enter Student Code: ")
name = input("Enter Student Name: ")
maths = float(input("Enter Marks in Maths: "))
physics = float(input("Enter Marks in Physics: "))
chemistry = float(input("Enter Marks in Chemistry: "))
english = float(input("Enter Marks in English: "))

print_grade_card(stu_code, name, maths, physics, chemistry, english)