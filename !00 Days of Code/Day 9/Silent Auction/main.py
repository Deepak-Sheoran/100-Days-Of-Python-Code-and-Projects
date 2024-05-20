from art import logo
from os import system


details = {}


def game():
    max_bid = 0
    winner = ""
    bidder_details = taking_inputs()
    for bidder in bidder_details:
        if bidder_details[bidder] > max_bid:
            winner = bidder
            max_bid = bidder_details[bidder]
    print(f"The winner of the bid is {winner} with a bid of {max_bid}")
    choice = input("Wanna use this software again? Type 'yes' or 'no' = ").lower()
    if choice == 'yes':
        details.clear()
        game()


def taking_inputs():
    system('cls')
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name = ")
    bid = float(input("What's your bid = $"))
    details[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no' = ").lower()
    if choice == 'yes':
        taking_inputs()
        return details


game()
