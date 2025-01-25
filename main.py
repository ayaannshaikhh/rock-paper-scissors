import random

def determine_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_input = input("Enter your choice (rock, paper, scissors): ")
    while user_input not in choices:
        print("Not a valid answer, please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ")
    return user_input

def determine_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors"):
        return "User wins!"
    elif (user == "scissors" and computer == "paper"):
        return "User wins!"
    elif (user == "paper" and computer == "rock"):
        return "User win!"
    else:
        return "Computer wins!"
        
def rock_paper_scissors():
    print("Rock paper scissors! Play against your computer!")
    user_choice = determine_user_choice()
    computer_choice = determine_computer_choice()

    print(f"User picked: {user_choice}")
    print(f"Computer picked: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    rock_paper_scissors()