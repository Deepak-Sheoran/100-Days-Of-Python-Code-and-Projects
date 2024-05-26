from coffee_maker import CoffeeMachine
from os import system
from art import logo

new_machine = CoffeeMachine()
while True:
    system('cls')
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'terminate':
        break

    if choice in ['report', 'espresso', 'latte', 'cappuccino', 'add resource']:
        new_machine.choice = choice
        new_machine.user_choice()
