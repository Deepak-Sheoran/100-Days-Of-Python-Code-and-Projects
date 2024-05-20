# Instructions
# 💪 This is a difficult challenge! 💪
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2-digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is *z*."
# e.g.
#
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."
#
# These functions will help you:
# lower() count()

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? = ")
name2 = input("What is their name? = ")
name1 = name1.lower()
name2 = name2.lower()
first_score = (name1 + name2).count("t") + (name1 + name2).count("r") + (name1 + name2).count("u") + (
            name1 + name2).count("e")
second_score = (name1 + name2).count("l") + (name1 + name2).count("o") + (name1 + name2).count("v") + (
            name1 + name2).count("e")
score = int(str(first_score) + str(second_score))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score or score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
