print("Welcome to the BMI Calculator.")
weight = float(input("Enter your weight in Kilograms = "))
height = float(input("Enter your height in meters = "))
bmi = weight / height ** 2
print(f"Your BMI Index is = {str(int(bmi))}")
