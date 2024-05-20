from random import randint

print("Welcome to the Bank Roulette! Lets find the Sucker that will be paying for our your meal today.")
names = input("Enter the names of the people at the table. Don't forget to insert a comma and space after the comma.\n")
names = names.split(", ")

rand = randint(0, len(names) - 1)
print(f"{names[rand]} is going to buy the meal today!")
