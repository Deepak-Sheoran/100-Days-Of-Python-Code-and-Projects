height = float(input("Enter your height in meters = "))
weight = float(input("Enter your weight in kilograms = "))

bmi = weight / height ** 2

evaluation = ["underweight", "normal weight", "slightly overweight", "obese", "clinically obese"]
index = 0
if bmi < 18.5:
    index = 0
elif bmi < 25:
    index = 1
elif bmi < 30:
    index = 2
elif bmi < 35:
    index = 3
else:
    index = 4

if index != 1:
    print(f"Your BMI is {bmi}, you are {evaluation[index]}.")
else:
    print(f"Your BMI is {bmi}, you have a {evaluation[index]}.")
