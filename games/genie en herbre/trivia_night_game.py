#0 question
#1-4 answers
#5 category
#6 difficulty


# 3 lives then loses

import random


def ask_question(q,p):
    print("Category :",q[5])
    print("Difficulty :", q[6])
    print(q[0])
    for i in range(1,5):
        print(str(i)+"."+q[p[i-1]])


def read_answer_raw():
    try:
        ans=int(input("Answer (1,2,3 or 4) : "))
        return ans
    except:
        print("Error. The answer must be an integer.")

def read_answer():
    ans=read_answer_raw()
    while ans not in [1,2,3,4]:
        print("Invalide input, try again")
        ans=read_answer_raw()
    return ans
###################################
def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass






#######################

#main
def play_game():
    score = 0
    lives = 3
    while lives > 0:
        q = random.choice(questions)
        p = [1, 2, 3, 4]
        random.shuffle(p)
        for i in range(1, 5):
            if p[i-1] == 1:
                rep = i
        ask_question(q, p)
        ans = read_answer()
        if p[ans-1] == 1:
            print("Correct")
            print("\n" * 3)
            score += int(q[6])
        else:
            print("Incorrect")
            print(f"The correct answer was {rep}. {q[p[rep-1]]}")
            print("\n" * 3)
            lives -= 1

    if lives == 0:
        print("You lost. You had", score, "points.")




# If you want to play as the presenter, after a normal game, type genie()
# and you will see the questions and their answers.
def genie():

    while True:
        q=random.choice(questions)
        p=[1,2,3,4]
        random.shuffle(p)
        for i in range(1,5):
            if p[i-1]==1:
                rep=(i)
        ask_question(q,p)
        print(f"the good answer was {rep}. {q[p[rep-1]]}")
        attend_le_joueur()
        print("  ")
        print("  ")
        print("  ")

def display_credits():
    print("Quiz Game by Mathew Al-Frenn")
    print("Thanks for playing!")
    attend_le_joueur()


def main_menu():
    while True:
        print("")
        print("Welcome to the Quiz Game!")
        print("1. Play")
        print("2. Presenter Mode")
        print("3. Credits")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("")
            play_game()
        elif choice == "2":
            print("")
            genie()
        elif choice == "3":
            print("")
            display_credits()
        elif choice == "4":
            print("")
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

            
# Load questions from file
questions = []
with open("quiz.csv") as file:
    lines = file.read().splitlines()

for line in lines:
    question = line.split("\t")
    questions.append(question)
# Run the main menu
main_menu()
