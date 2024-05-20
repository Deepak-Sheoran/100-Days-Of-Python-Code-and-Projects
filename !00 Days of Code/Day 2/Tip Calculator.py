print("Welcome to the Tip Calculator.")
total_bill = int(input("What is the total bill amount = $ "))
people = int(input("How many people are present among which the bill amount will be split = "))
percentage = int(input("What percentage tip amount you wish to give = "))
tip = (total_bill * percentage / 100) / people
pay = tip + total_bill / people
print(f"Each person should pay = {str(round(pay, 2))}")  # f-string being used for string interpolation
print("Each person should pay = {:.2f}".format(pay))   # .format being used for string interpolation
