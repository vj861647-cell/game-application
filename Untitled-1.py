# -----------------------------------------------------------
# ROCK, PAPER, SCISSOR GAME APPLICATION
# Developed in Python
# -----------------------------------------------------------

import random
import time

# Function to display game menu
def show_menu():
    print("\n===============================")
    print("   ROCK - PAPER - SCISSOR GAME ")
    print("===============================")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("4. Exit the Game")
    print("===============================\n")

# Function to get computer choice
def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

# Function to get user choice
def get_user_choice():
    while True:
        try:
            user_input = int(input("Enter your choice (1/2/3/4): "))
            if user_input == 1:
                return "rock"
            elif user_input == 2:
                return "paper"
            elif user_input == 3:
                return "scissor"
            elif user_input == 4:
                return "exit"
            else:
                print("Invalid choice! Please choose between 1 to 4.")
        except ValueError:
            print("Please enter only numbers.")

# Function to determine winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"

    if (user == "rock" and computer == "scissor") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissor" and computer == "paper"):
        return "win"
    else:
        return "lose"

# Function to display results
def show_result(user, computer, result):
    print("\n---------------------------------")
    print(f"Your Choice     : {user.capitalize()}")
    print(f"Computer Choice : {computer.capitalize()}")
    print("---------------------------------")

    if result == "win":
        print("Result: 🟢 You WON this round!")
    elif result == "lose":
        print("Result: 🔴 You LOST this round!")
    else:
        print("Result: 🟡 It's a TIE!")
    print("---------------------------------\n")


# MAIN GAME LOOP
def start_game():
    user_score = 0
    computer_score = 0
    tie_score = 0

    print("\nWelcome to Rock, Paper, Scissor Game!")
    time.sleep(1)

    while True:
        show_menu()
        user_choice = get_user_choice()

        if user_choice == "exit":
            print("\nExiting the game...")
            time.sleep(1)
            break

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        # Update scores
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        else:
            tie_score += 1

        show_result(user_choice, computer_choice, result)

        # Show score
        print("Current Score:")
        print(f" You     : {user_score}")
        print(f" Computer: {computer_score}")
        print(f" Ties    : {tie_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            break

    print("\nFINAL SCORE")
    print("---------------------------")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Total Ties     : {tie_score}")
    print("---------------------------")

    if user_score > computer_score:
        print("🎉 Congratulations! You WON the game!")
    elif user_score < computer_score:
        print("😞 You LOST the game. Try again!")
    else:
        print("🤝 The game ended in a TIE.")

    print("\nThank you for playing!\n")


# START THE GAME
start_game()
