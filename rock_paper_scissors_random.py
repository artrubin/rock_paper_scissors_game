from random import choice, randint
user_wins = 0
computer_wins = 0
score = 3

while user_wins < score and computer_wins < score:
    computer_choice = choice(["rock", "scissors", "paper"])
    print(f"User Score: {user_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    user_choice = input("Please enter your choice >> ").lower()
    if user_choice == "quit" or user_choice == "q":
        break
    if user_choice not in ["rock", "scissors", "paper"]:
        print("Wrong Entry. You can only enter 'rock', 'paper', or 'scissors'")
    else:
        if user_choice == computer_choice:
            print(f"Computer plays '{computer_choice}', it is a tie!!! ")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print(f"Computer plays '{computer_choice}', you won this round!!!")
                user_wins += 1
            elif computer_choice == "paper":
                print(f"Computer plays '{computer_choice}', you lost this round!!!")
                computer_wins += 1
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print(f"Computer plays '{computer_choice}', you lost round!!!")
                computer_wins += 1
            elif computer_choice == "rock":
                print(f"Computer plays '{computer_choice}, you won this round!!!")
                user_wins += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print(f"Computer plays '{computer_choice}', you lost this round!!!")
                computer_wins += 1
            elif computer_choice == "paper":
                print(f"Computer plays '{computer_choice}', you won this round!!!")
                user_wins += 1
if user_wins > computer_wins:
    print("CONGRATULATION, YOU WON THE GAME!!!")
elif user_wins == computer_wins:
    print ("IT'S A TIE...)
else:
    print("OH NO :( THE COMPUTER WON THE GAME ...")

