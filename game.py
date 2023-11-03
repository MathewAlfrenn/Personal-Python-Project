import random


def welcome():
    '''
    ()->None
    print a welcome message
    '''
    print("Welcome to the adventure rpg game : Your Journey !")

def attend_le_joueur_debut():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Press Enter to begin ")
    except SyntaxError:
         pass

    '''
def enter_choice():
    a=("Please select your option \n 1.Start your journey \n 2.Credit \n 3.Exit \n ")
    x=(input(a))
    
    while x.isnumeric() ==False:
        x=(input(a))
    while x.isnumeric() == True:
        x=int(x)
        if x>1 and x<4:
            return x
        else:
            x=str(x)
            x=(input(a))

    
    return x
    '''

def checks_type_int():
    a=("Please select your option \n 1.Start your journey \n 2.Credit \n 3.Exit \n ")
    while True:
        x=input(a)
        x=str(x)
        if x.isnumeric() ==True:
            x=int(x)
            if x>0 and x<4:
                return x
        



def main():
    attend_le_joueur_debut
    checks_type_int()
    welcome()
    welcome()


    
main()
