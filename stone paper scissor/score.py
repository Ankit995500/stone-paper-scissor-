user_score = 0
comp_score = 0

def update(result):
    global user_score, comp_score
    if result == "user":
        user_score += 1
    elif result == "computer":
        comp_score += 1

def show_score():
    print("Score -> You:", user_score, "| Computer:", comp_score)