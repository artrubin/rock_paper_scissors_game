from random import choice, randint
play = 1
while play == 1:
    # randomly assigns values to compute_choice
    computer_choice = choice(["rock", "scissors", "paper"])

    print("Rock...")
    print("Paper...")
    print("Scissors...")

    user_choice = input("Please enter your choice >>").lower()

    if user_choice not in ["rock", "scissors", "paper"]:
        print("Wrong Entry. You can only enter 'rock', 'paper', or 'scissors'")
    else:
        if user_choice == computer_choice:
            print(f"Computer plays '{computer_choice}', it is a tie!!! ")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print(f"Computer plays '{computer_choice}', you won!!!")
            elif computer_choice == "paper":
                print(f"Computer plays '{computer_choice}', you lost!!!")
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print(f"Computer plays '{computer_choice}', you lost!!!")
            elif computer_choice == "rock":
                print(f"Computer plays '{computer_choice}, you won!!!")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print(f"Computer plays '{computer_choice}', you lost!!!")
            elif computer_choice == "paper":
                print(f"Computer plays '{computer_choice}', you won!!!")

    play = int(input("Enter '1' if you would like to play the game, enter 'O' if you would like to stop >>"))

