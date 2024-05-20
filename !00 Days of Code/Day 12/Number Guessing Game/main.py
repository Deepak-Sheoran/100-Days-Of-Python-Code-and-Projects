from art import logo
from os import system
from random import randint

attempts = {"easy": 10, "normal": 8, "hard": 5}


def number_guessing_game():
    system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("The computer has picked a number between 1 and 100.")
    choice = input("Choose a difficulty. Type 'easy', 'normal' or 'hard': ").lower()
    number = randint(1, 100)  # Here both numbers are included
    if choice in attempts:
        number_of_attempts = attempts[choice]

        def answer_checker():
            won = False
            nonlocal number_of_attempts  # Because we need to change this value not just use it
            # print(f"Answer = {number}")
            while number_of_attempts != 0 and won is False:
                print(f"You have {number_of_attempts} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))
                if guess == number:
                    print(f"You got it! The answer was {number}")
                    won = True
                    number_of_attempts -= 1
                elif guess > number:
                    if guess - number > 10:
                        print("Too High.\nGuess Again")
                        number_of_attempts -= 1
                    else:
                        print("High.\nGuess Again")
                        number_of_attempts -= 1
                else:
                    if number - guess > 10:
                        print("Too Low.\nGuess Again")
                        number_of_attempts -= 1
                    else:
                        print("Low.\nGuess Again")
                        number_of_attempts -= 1
            if won:
                print("Congratulation on winning.")
                if number_of_attempts != 0:
                    print(f"You still had {number_of_attempts} attempts remaining.")

        answer_checker()


number_guessing_game()
