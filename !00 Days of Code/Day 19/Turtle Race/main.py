from turtle import Screen
from race import Race

screen = Screen()

choice = 'y'
while choice == 'y':
    race = Race()
    guessed_option = race.guessed_winner
    actual_winner = race.who_won
    result = "right" if actual_winner == guessed_option else "wrong"
    choice = screen.textinput("Result", f"You guessed {result}! Wanna play again(y/n").lower()
