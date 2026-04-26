def show(user, comp, result):
    print("You:", user)
    print("Computer:", comp)

    if result == "tie":
        print("Tie")
    elif result == "user":
        print("You win")
    else:
        print("Computer wins")