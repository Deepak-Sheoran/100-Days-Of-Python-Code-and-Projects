class CoffeeMachine:
    def __init__(self):
        self.choice = ""
        self.transaction_successful = False
        self.lacking_resources = {'latte': [], 'espresso': [], 'cappuccino': []}
        self.resources = {"water": 300, "coffee": 100, "milk": 200, "money": 10}
        self.required_resources = \
            {
                'espresso': {'water': 50, 'coffee': 18, 'milk': 0, 'money': 1.50},
                'latte': {'water': 200, 'coffee': 24, 'milk': 150, 'money': 2.50},
                'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100, 'money': 3.00}
            }

    def user_choice(self):
        if self.choice in ['latte', 'espresso', 'cappuccino']:
            if self.check_resources():
                self._coin_process()
                if self.transaction_successful:
                    self.transaction_successful = False
                    self.update_resources(True, False)
            else:
                print(
                    f"Apologies, currently due to lack of ingredients(s) such as "
                    f"{', '.join(self.lacking_resources[self.choice])}. Your Order for {self.choice} can't be "
                    f"processed any further!")
                self.lacking_resources[self.choice] = []

        elif self.choice == 'report':
            print(self.report())

        elif self.choice == 'add resource':
            self.update_resources(False, True)

    def report(self):
        return (f"Available resources:-\nWater: {self.resources['water']}ml\nMilk: {self.resources['milk']}ml"
                f"\nCoffee: {self.resources['coffee']}g\nMoney: ${self.resources['money']}")

    def check_resources(self):
        """
        This method is only for the cases when the user asks for a coffee to be made, and so this method checks whether
        there are enough resources available to make that coffee.
        """
        enough_resources = True
        for ingredient in self.resources:
            if ingredient == 'money':
                pass
            elif self.resources[ingredient] < self.required_resources[self.choice][ingredient]:
                enough_resources = False
                self.lacking_resources[self.choice].append(ingredient)
        return enough_resources

    def _coin_process(self):
        """
        This method gets called after the method check_resources has been run, and it has checked that there are indeed
        enough resources available in the machine to make the coffee.
        This method takes the money from the user in form of coins and checks whether the money that's been provided is
        enough to cover the bill.
        Returns nothing but changes the value of the variable 'transaction_successful' according to the situation
        """
        currency = {"quarter": 0.25, "dime": 0.10, "nickle": 0.05, "pennie": 0.01}
        print("This machine is coin operated.")
        given_money = 0
        required_money = self.required_resources[self.choice]['money']
        for type_of_coin in currency:
            no_of_coins = int(input(f"How many {type_of_coin}s?: "))
            given_money += no_of_coins * currency[type_of_coin]
        given_money = round(given_money, 2)
        print(f"Total Money Given = ${given_money}")
        if required_money <= given_money:
            print(f"Here is your change = ${round(given_money - required_money, 2)}")
            print(f"Here is your {self.choice}🍵 Enjoy!")
            input()
            self.transaction_successful = True
        else:
            print(f"Transaction Failed!\nInsufficient money given. "
                  f"You came sort by ${round(required_money - given_money, 2)}"
                  "\nMoney Refunded")
            self.transaction_successful = False

    def update_resources(self, make_drink=False, add_resources=False):
        """
        This method will only be called when the method check_resources have already made sure that there are enough
        resources available for making the drink and after that the method coin_process has made a successful
        transaction for the order.
        OR
        When the owner of the coffee machine wants to manually add or remove
        resources from the coffee machine storage area.
        """
        if make_drink:
            for ingredient in self.resources:
                if ingredient == 'money':
                    self.resources[ingredient] += self.required_resources[self.choice][ingredient]
                else:
                    self.resources[ingredient] -= self.required_resources[self.choice][ingredient]
