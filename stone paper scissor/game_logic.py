import time

def computer_choice():
    choices = ["stone", "paper", "scissors"]
    return choices[int(time.time()) % 3]

def winner(user, comp):
    if user == comp:
        return "tie"
    elif user == "stone" and comp == "scissors":
        return "user"
    elif user == "paper" and comp == "stone":
        return "user"
    elif user == "scissors" and comp == "paper":
        return "user"
    else:
        return "computer"