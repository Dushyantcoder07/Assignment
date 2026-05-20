# Taking student details
name = input("Enter student name: ")
student_class = input("Enter class: ")

# Taking marks for 5 subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

# Calculating total and percentage
total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total / 500) * 100

# Finding grade using conditional statements
if percentage >= 60:
    grade = 'A'
elif percentage >= 50 and percentage < 60:
    grade = 'B'
elif percentage >= 40 and percentage < 50:
    grade = 'C'
elif percentage >= 33 and percentage < 40:
    grade = 'D'
else:
    grade = 'Fail'

# Displaying result
print("\n----- Student Result -----")
print("Name       :", name)
print("Class      :", student_class)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)