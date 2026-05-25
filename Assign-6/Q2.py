import random

player_score = 0
computer_score = 0

choices = ["stone", "paper", "scissors"]
menu_choices = {
    "1": "stone",
    "2": "paper",
    "3": "scissors",
}

while True:
    print("\n--- Stone Paper Scissors Game ---")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    try:
        choice = input("Enter your choice: ").strip().lower()
    except EOFError:
        print("\nNo input received. Exiting game.")
        break

    choice = menu_choices.get(choice, choice)

    if choice == "4" or choice == "exit":
        print("\nGame Over!")
        print("Final Score:")
        print("Player:", player_score)
        print("Computer:", computer_score)
        break

    if choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("\nYou chose:", choice)
    print("Computer chose:", computer)

    if choice == computer:
        print("It's a Draw!")

    elif (
        (choice == "stone" and computer == "scissors") or
        (choice == "paper" and computer == "stone") or
        (choice == "scissors" and computer == "paper")
    ):
        print("You Win!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore:")
    print("Player:", player_score)
    print("Computer:", computer_score)