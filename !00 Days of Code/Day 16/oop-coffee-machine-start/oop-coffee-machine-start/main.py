from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
accountant = MoneyMachine()
while True:
    types_of_coffees = menu.get_items().split("/")[:-1]
    print(f"Types of Coffees Available at this machine = {types_of_coffees}")
    choice = input("Enter your choice = ").lower()

    if choice == 'report':
        machine.report()

    if choice == 'profit':
        print(f"Profit Made = ${accountant.profit}")
        accountant.report()

    elif choice in types_of_coffees:
        drink_requirements = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink_requirements):
            if accountant.make_payment(drink_requirements.cost):
                machine.make_coffee(drink_requirements)
        else:
            print("Not enough resources available!!")

    if choice == 'terminate':
        break
