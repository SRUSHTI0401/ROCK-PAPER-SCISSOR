import random

def get_computer_choice():
    choices = [1, -1, 0]
    return random.choice(choices)

def get_choice_string(choice):
    return {1: "rock", -1: "paper", 0: "scissors"}[choice]

def get_choice_value(choice):
    return {"r": 1, "p": -1, "s": 0}[choice]

def determine_winner(user_value, computer_value):
    if user_value == computer_value:
        return "It's a tie!"
    elif (user_value == 1 and computer_value == -1) or \
         (user_value == -1 and computer_value == 0) or \
         (user_value == 0 and computer_value == 1):
        return "Computer wins!"
    else:
        return "You win!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Computer choice
        computer = get_computer_choice()

        # User choice
        print("1. r=rock\n2. p=paper\n3. s=scissors")
        y_choice = input("Enter your choice ('r', 'p', 's'): ").strip().lower()

        # Check if the user choice is valid
        if y_choice not in {"r", "p", "s"}:
            print("Invalid choice. Please choose 'r', 'p', or 's'.")
            continue

        y_value = get_choice_value(y_choice)  # Get the numerical representation of the user's choice
        you = get_choice_string(y_value)  # Get the string representation of the user's choice
        com = get_choice_string(computer)  # Get the string representation of the computer's choice

        print(f"Your choice is {you}\nComputer choice is {com}")

        # Determine the winner
        result = determine_winner(y_value, computer)
        print(result)

        # Ask if the user wants to play another round
        play_again = input("If you want to play another round, enter 'yes'. To quit, enter 'no': ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
play_game()
