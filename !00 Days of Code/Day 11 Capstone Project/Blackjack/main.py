from art import logo
from random import choice
from os import system

suit = [['Ace', 1], ('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8),
        ('Nine', 9), ('Ten', 10), ('Jack', 10), ('Queen', 10), ('King', 10)]


def blackjack():
    """
    Docstring: This function is the main body of the code. Calling it means we are starting a new blackjack game with a
    fresh deck of cards. All the main code is within this function like creating a deck of cards with the help of global
    variable suit. After the deck has been created, we have the nested function chooser that picks out a card from the
    deck of cards and also removes it so that cards keep decreasing after they have been picked out. In case all the
    cards have been picked out, the player is notified and can choose to whether or not they wish to start a new game of
    blackjack.
    """
    heart_suit = suit.copy()
    diamond_suit = suit.copy()
    club_suit = suit.copy()
    spade_suit = suit.copy()

    deck = [("Hearts", heart_suit), ("Diamond", diamond_suit), ("Club", club_suit), ("Spade", spade_suit)]

    def chooser(turn='player', number_of_times=1):
        """
        Docstring: Function that randomly picks cards from the deck, adds them to either player cards or computer cards
        based on the argument passed while calling the function.
        """
        nonlocal deck, player_cards, computer_cards, current_deck
        # The following loop runs as many times as the number provided in the parameters of the function chooser().
        # Although it can only take two possible entries that are either 1 or 2. If it's one, that means that either the
        # player or computer is picking another card or if its 2 then that means it's the start of a new turn and the
        # computer is just picking the staring cards of Dealer and Player.
        for i in range(number_of_times):
            # In the following lines, first a deck is chosen and then a card is chosen from the previously chosen deck
            chosen_deck = choice(deck)
            chosen_card = choice(chosen_deck[1])
            # Removes the card from the randomly chosen suit
            deck[deck.index(chosen_deck)][1].remove(chosen_card)

            card = f"{chosen_card[0]} of {chosen_deck[0]}"

            # Here, following if block checks whether a suit of cards is empty, if it is then that suit is removed from
            # the deck. In case all the suits have been removed from the deck, that means that the deck is empty and
            # the variable current_deck is assigned the value of 'n'.
            if len(chosen_deck[1]) == 0:
                deck.remove(chosen_deck)
                if len(deck) == 0:
                    current_deck = 'n'

            if turn == 'player':

                if chosen_card[0] == "Ace":
                    value_of_ace = int(input(f"One of the randomly picked card is {card}. You can either choose its "
                                             f"value to be 1 or 11. Enter the value(1 or 11) = "))
                    if value_of_ace not in [1, 11]:
                        print("Error! Entry out of expected value. Hence '1' will be assigned to be the value")
                        chosen_card[1] = 1
                    else:
                        if value_of_ace == 1:
                            chosen_card[1] = 1
                        else:
                            chosen_card[1] = 11

                player_cards['Cards'].append(f"{chosen_card[0]} of {chosen_deck[0]}")
                player_cards['Value'].append(chosen_card[1])
                if number_of_times == 1:
                    print(f"The card that has been picked so far are: {player_cards['Cards']}")
                    print(f"Their accumulated values is: {sum(player_cards['Value'])}")

            else:
                if chosen_card[0] == "Ace":
                    if sum(computer_cards['Value']) + 11 < 21:
                        chosen_card[1] = 11
                computer_cards['Cards'].append(f"{chosen_card[0]} of {chosen_deck[0]}")
                computer_cards['Value'].append(chosen_card[1])

    def winner_checker():
        """
        Docstring: This function checks who won based on the cumulative value of both computer's and player's cards.
        """
        if sum(computer_cards['Value']) == 21 and sum(player_cards['Value']) == 21:
            print("Dealer and Player both have a blackjack. It's a DrAw!!")
            return
        elif sum(computer_cards['Value']) == 21:
            print("Dealer has a Blackjack. Dealer wIns!!")
            return
        elif sum(player_cards['Value']) == 21:
            print("Player has a Blackjack. Player wIns!!")
            return

        if sum(computer_cards['Value']) > 21 and sum(player_cards['Value']) > 21:
            print("Dealer and Player both Busts. Its a draw.")
            return
        elif sum(computer_cards['Value']) > 21:
            print("Dealer Busts. Player wInS!!")
            return
        elif sum(player_cards['Value']) > 21:
            print("Player Busts. Dealer WInS!!")
            return

        if sum(player_cards['Value']) - sum(computer_cards['Value']) > 0:
            print("Player Wins")
        elif sum(player_cards['Value']) - sum(computer_cards['Value']) == 0:
            print("Its a draw")
        else:
            print("Dealer Wins!!")

    def printer():
        print(f"Player's Cards = {player_cards['Cards']} and their value is {sum(player_cards['Value'])}")
        print(f"Computer's first card = {computer_cards['Cards'][0]} and its value is {computer_cards['Value'][0]}")

    current_deck = 'y'

    while current_deck == 'y':
        system('cls')
        print(logo)
        player_cards = {"Cards": [], "Value": []}
        computer_cards = {"Cards": [], "Value": []}
        if current_deck == 'y':
            chooser(number_of_times=2)
        if current_deck == 'y':
            chooser(turn='n', number_of_times=2)
        if sum(computer_cards["Value"]) < 17:
            if current_deck == 'y':
                chooser('n')
        printer()
        player_choice = "y"
        while player_choice == "y":
            if current_deck == 'n':
                break
            player_choice = (input("Type 'y' to get another card, Type 'n' to pass: ").lower())
            if player_choice == 'y':
                if current_deck == "y":
                    chooser()
                    if sum(player_cards['Value']) > 21:
                        player_choice = 'n'
        print(f"Player's final hand: {player_cards['Cards']} and their value: {sum(player_cards['Value'])}")
        print(f"Dealer's final hand: {computer_cards['Cards']} and their value: {sum(computer_cards['Value'])}")
        winner_checker()
        if len(deck) == 1 and len(deck[0][1]) < 4:
            current_deck = 'n'
        if current_deck == 'n':
            print("\nNot enough cards to choose from for the next turn.\n\nThank you for playing.")
            return
        current_deck = input("Still wanna keep going with the remaining deck. Choose 'y' or 'n': ").lower()


keep_going = 'y'
while keep_going == "y":
    blackjack()
    keep_going = input("Want to play another game of Blackjack. Type 'y' or 'n' :").lower()
