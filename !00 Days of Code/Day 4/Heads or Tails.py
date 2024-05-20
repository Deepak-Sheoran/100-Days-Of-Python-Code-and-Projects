import random

print("Welcome to the game of Heads or Tails!!")
guess = input("Guess whether the flipped coin is heads or tails = ").lower()
rand = random.randint(0, 1)
choices = ["heads", "tails"]
if guess == choices[rand]:
    print("Bingo!! You were right.")
else:
    print("Boo Boo!! You guessed wrong.")
