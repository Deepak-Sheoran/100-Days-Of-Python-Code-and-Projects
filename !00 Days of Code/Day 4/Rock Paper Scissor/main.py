from logos import rock, paper, scissors
from random import randint

logo = [rock, paper, scissors]
choice = int(input("What do you choose. Type 0 for rock, 1 for paper and 2 for scissors = "))
if choice in [0, 1, 2]:
    print(f"You have thrown :- \n{logo[choice]}")
rand = randint(0, 2)
print(f"Computer throws at the same time\n{logo[rand]}")
if choice < 0 or choice > 2:
    print("You have inserted a wrong input. You lose by default.")
elif choice == rand:
    print("Its a draw")
elif choice - rand == 1 or choice - rand == -2:
    print("You Win!!")
else:
    print("You Lose!!")
