print("Welcome to average height calculator")
student_heights = input("Enter the student heights with nothing but space between each entry= ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total, numbers = 0, 0
for height in student_heights:
    total += height
    numbers += 1
average_height = round(total / numbers)
print(f"total height = {total}\nnumber of students = {numbers}\naverage height = {average_height}")
