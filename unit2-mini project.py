# Student Grading Automation

print("======================================")
print("       STUDENT GRADING SYSTEM")
print("======================================")

name = input("Enter student name: ")

mark1 = float(input("Enter marks in Python: "))
mark2 = float(input("Enter marks in Mathematics: "))
mark3 = float(input("Enter marks in Computer Science: "))

total = mark1 + mark2 + mark3
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n========== RESULT ==========")
print("Student Name :", name)
print("Total Marks  :", total, "/ 300")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)

if grade == "F":
    print("Result       : FAIL")
else:
    print("Result       : PASS")

print("============================")