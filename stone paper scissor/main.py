from game_logic import computer_choice, winner
from display import show
from score import update, show_score

print("Stone Paper Scissors Game")

while True:
    user = input("Enter stone/paper/scissors or exit: ")

    if user == "exit":
        break

    comp = computer_choice()
    result = winner(user, comp)

    show(user, comp, result)
    update(result)
    show_score()