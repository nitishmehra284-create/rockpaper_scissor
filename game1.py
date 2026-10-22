

import random

choices = ["rock", "paper", "scissor"]

while True:
    user = input("\nEnter Rock, Paper, Scissor or Exit: ").lower()

    if user == "exit":
        print("Thanks for playing! 👋")
        break

    if user not in choices:
        print("Invalid choice! Try again 🥵")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Draw 🤝")

    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("You Win 🎉")

    else:
        print("Computer Wins 🎊")
