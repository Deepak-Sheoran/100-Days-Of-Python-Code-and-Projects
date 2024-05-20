# Instructions
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the
# names of the students and the values are their exam scores.
#
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and their grades for values.

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Creating an empty dictionary called student_grades.
student_grades = {}

# Writing our code below to add the grades to student_grades.
for student in student_scores:
    student_score = student_scores[student]
    if student_score >= 91:
        student_grades[student] = "Outstanding"
    elif student_score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

for student in student_grades:
    print(f"The grade for {student} is {student_grades[student]}")
