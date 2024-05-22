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
starting_resources = {"water": 300, "coffee": 100, "milk": 200, "money": 10}
currency = {"quarter": 0.25, "dime": 0.10, "nickle": 0.05, "pennie": 0.01}


# TODO 3. Create a function that will be run to start the coffee machine
def coffee_machine():
    # since the values in resources can change but the starting resources will remain the same
    resources = starting_resources
    required_resources = \
        {
            'espresso': {'water': 50, 'coffee': 18, 'milk': 0, 'money': 1.50},
            'latte': {'water': 200, 'coffee': 24, 'milk': 150, 'money': 2.50},
            'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100, 'money': 3.00}
        }

    #  TODO 4. Within the function create various local function that will either return formatted strings, change
    #   the data stored in the global variables, print report that will make the master of the coffee machine
    #   aware how much resources are available in the machine ,a function that checks whether or not there are enough
    #   resources left in the machine or a function that will update the values of the resources when the master adds
    #   new resources into the machine
    def requirements(drink):
        """
        This function takes the type of drink that has been ordered by the user and checks whether the resources
        available in the coffee machine is enough to make that drink. If there are enough resources available then the
        function returns the amount of money required for that drink, if not then the function returns 0, making the
        program aware of the lack of the resources.
        """
        nonlocal enough_resources  # need to use nonlocal since we might need to change its value depending on the
        # situation
        insufficient_ingredient = []
        for ingredient in resources:
            if ingredient == 'money':
                if len(insufficient_ingredient) == 0:
                    enough_resources = True
                    return required_resources[drink][ingredient]
            elif required_resources[drink][ingredient] > resources[ingredient]:
                insufficient_ingredient.append(ingredient)
                enough_resources = False
        return insufficient_ingredient

    def player_choice(option):
        if option == 'report':
            return (f"Available resources:-\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml"
                    f"\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
        if option in ['espresso', 'latte', 'cappuccino']:
            money = requirements(option)
            if isinstance(money, list):
                return f"There is not enough {', '.join(money)} in the coffee machine to prepare your order."
            else:
                return [f"Your bill for the order of {option} is ${money}.", money]

    def update_resources(drink=None, added_resources=None):
        """
        Function that updates the available resources incase a transaction has been successfully completed. Also,
        possible to update available resources in case the master of the coffee machine wishes to add new resources
        or take out something from the available resources. All in all, this function holds the key to do any kind of
        change to the available resources.
        """
        nonlocal resources
        if drink is not None:
            for type_of_resource in resources:
                if type_of_resource == "money":
                    resources[type_of_resource] += required_resources[drink][type_of_resource]
                else:
                    resources[type_of_resource] -= required_resources[drink][type_of_resource]
        if added_resources is not None:
            for type_of_resource in added_resources:
                resources[type_of_resource] += added_resources[type_of_resource]

    while True:
        enough_resources = False
        transaction_successful = False
        money_required = 0
        system('cls')
        print(logo)
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # The program will keep running unless the master of the coffee machine enters the following command
        if choice == 'terminate':
            return

        if choice == "add resource":
            new_resources = {}
            print("You have chosen to add resource to the machine. Please enter how much you added or removed:")
            for kind_of_resource in resources:
                new_resources[kind_of_resource] = int(input(f"How much {kind_of_resource}"))
            update_resources(None, new_resources)

        if choice in ['report', 'espresso', 'latte', 'cappuccino']:
            output = player_choice(choice)
            # if player_choice function returns only a string, that means for some reason the transaction failed and the
            # reason for the failed transaction is being returned
            if isinstance(output, str):
                print(output)
                input()
            else:
                money_required = output[1]
                print(output[0])
        else:
            continue

        if enough_resources:
            print("This machine is coin operated.")
            given_money = 0
            for type_of_coin in currency:
                no_of_coins = int(input(f"How many {type_of_coin}s?: "))
                given_money += no_of_coins * currency[type_of_coin]
            given_money = round(given_money, 2)
            print(f"Total Money Given = ${given_money}")
            if money_required <= given_money:
                print(f"Here is your change = ${round(given_money - money_required, 2)}")
                print(f"Here is your {choice} Enjoy!")
                transaction_successful = True
            else:
                print(f"Transaction Failed!\nInsufficient money given. "
                      f"You came sort by ${round(money_required - given_money, 2)}"
                      "\nMoney Refunded")
        else:
            pass

        if transaction_successful:
            update_resources(choice)


coffee_machine()
