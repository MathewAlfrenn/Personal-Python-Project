import random
import time
#############################################################

def begin():
    '''
    ()->None
    print a welcome message
    '''
    print("You will now begin the adventure rpg game : Your Journey !")
######
def attend_le_joueur_debut():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Press Enter to begin ")
    except SyntaxError:
         pass

######

def checks_the_choice():
    a=("Please select your option \n 1.Start your journey \n 2.Credit \n 3.Exit \n ")
    while True:
        x=input(a)
        x=str(x)
        if x.isnumeric() ==True:
            x=int(x)
            if x>0 and x<4:
                return x
######        
def credit(a):
    while a == 2:
        print("Mathew Al-Frenn \n")
        a=checks_the_choice()
######
def Exit(a):
    if a == 3:
        exit()

######    
def character_creation():
    global name
    name = input("Enter the name of your character")
#####
def character_age():
    global age
    age= input("Enter the age of your character")
    while age.isnumeric == False:
        age= input("Enter the age of your character")
    age=int(age)
        
def young():
    print("it seems that you are too young, you should wait some time and then when you are old enough come back to me")
    time. sleep(5)
    exit()
    
def old():
    print("Your quite old, perhaps too old to be doing dangerus adventures like this one will be")
    time. sleep(5)
    exit()

#######

def welcome():
    print("Hello", name, ",are you ready to start your epic adventure?")

######!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def main():
    attend_le_joueur_debut()
    a=checks_the_choice()
    Exit(a)
    credit(a)
    
    begin()
    character_creation()
    character_age()
    welcome()
    if age<18:
        young()
    if age>65:
        old()
        
        


##################   
main()
##################
