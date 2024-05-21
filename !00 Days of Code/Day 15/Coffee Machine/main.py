"""
About the program "Coffee Machine"
This program allows the user to choose a type of coffee from three options. The coffee will then be prepared ny the
machine and given to the user but while making the coffee, the program will deduct the amount of various resources
used from the data it has since during the preparation of the coffee these resources will be used. Now, before the
coffee is given to the user, the program will check what it costs and demand money and take it from the user.
"""
# TODO 1. import the required packages and files
from art import logo
from os import system

# TODO 2. create various variables that will keep records like initial resources available, currency and their value
starting_resources = {"money": 0, "water": 300, "coffee": 100, "milk": 200}
currency = {"penny": 0.01, "nickle": 0.05, "dime": 0.10, "quarter": 0.25}


# TODO 3. Create a function that will be run to start the coffee machine
def coffee_machine():
    resources = starting_resources  # since the values in resources can change but the starting resources will remain

    #                                 the same

    #  TODO 4. Within the function create various local function that will either return formatted strings, change
    #   the data stored in the global variables, print report that will make the master of the coffee machine
    #   aware how much resources are available in the machine ,a function that checks whether or not there are enough
    #   resources left in the machine or a function that will update the values of the resources when the master adds
    #   new resources into the machine
    def report():
        return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}"

    keep_running = True
    while keep_running:
        system('cls')
        print(logo)
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            print(report())
            continue
        keep_running = False


coffee_machine()
