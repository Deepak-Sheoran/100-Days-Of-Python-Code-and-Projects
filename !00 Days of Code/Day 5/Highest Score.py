student_scores = input("Enter the student scores, make sure to only enter space between each entry = ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest = 0
for num in student_scores:
    if num > highest:
        highest = num
print(f"The highest score in the class is: {highest}")
