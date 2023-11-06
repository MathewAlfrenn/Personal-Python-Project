# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]


    
             
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     index=0

     while index < len(p):
         if index%2 ==0:
             autre.append(p[index])
             index = index+1
         else:
             donneur.append(p[index])
             index= index+1

     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    index=0
    sousindex=1
    while index <len(l)-1:
        while sousindex<len(l) and index <len(l)-1:
            if l[index][0]==l[sousindex][0]:
                l.remove(l[sousindex])
                l.remove(l[index])
                break
            sousindex=sousindex+1

        else:
            index= index+1
        sousindex = index+1
    resultat=l
#l=(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
# probleme : quand j enelve le 10, le 2 devient position 0 mais la je regarde avec la position 1, car index augmente de 1, donc faire que si le if a lieu de NE PAS augmenter l index
# aussi je dois utuliser resultat
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    index=0
    while index <len(p)-1:
        print(p[index],end=" ")
        index= index+1
    print(p[len(p)-1])

    

def entrez_position_valide(n):
    
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     n=str(n)
     a=("J'ai"+" "+ n +" " +"cartes. Si 1 est la position de ma première carte et"+" " +n +" " +"la position de ma dernière carte, laquelle de mes cartes voulez-vous? SVP entrer un entier de 1 à "+" " + n +" " +":")
     n=int(n)
     x=(input(a))
     x=int(x)
     type(x)
     while x<1 or x>n:
         n= str(n)
         x=input(("Vérifier que votre valeur est bien comprise entre 1 et"+ " " +n +":"))
         x=int(x)
         n=int(n)
         
     return x



     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     print("*********************************************************")
     while len(humain) !=0 or len(donneur) !=0:
         if len(humain)==0:
             print("J'ai terminé toutes les cartes.")
             print("Félicitations! Vous, Humain, vous avez gagné.")
             break
         
         print("Votre tour.")
         print("Votre main est:")
         affiche_cartes(humain)
         z=entrez_position_valide(len(donneur))
         if z ==1:
             print("Vous avez demandé ma 1ère carte")
         else:
             z=str(z)
             print("Vous avec demandé ma"+" "+z+"ème carte.")
             z=int(z)
         print("La voilà. C'est un", donneur[z-1])
         print("Avec",donneur[z-1]," ajouté, votre main est:")
         humain.append(donneur[z-1])
         donneur.remove(donneur[z-1])
         affiche_cartes(humain)
         print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
         elimine_paires(humain)
         affiche_cartes(humain)
         attend_le_joueur()
         if len(humain)==0:
             print("J'ai terminé toutes les cartes.")
             print("Félicitations! Vous, Humain, vous avez gagné.")
             break
         if len(donneur) ==0:
             print("J'ai terminé toutes les cartes.")
             print("Vous avez perdu ! Moi, Robot, jai gagné.")
             break
         if len(humain)==0:
             print("J'ai terminé toutes les cartes.")
             print("Félicitations! Vous, Humain, vous avez gagné.")
             break
         print("*********************************************************")
         print("Mon tour.")
         c=random.randint(1, len(humain))
         if c ==1:
             print("J'ai pris votre 1ère carte")
         else:
             c=str(c)
             print("J'ai pris votre"+" "+c+"ème carte.")
             c=int(c)
         donneur.append(humain[c-1])
         humain.remove(humain[c-1])
         elimine_paires(donneur)
         attend_le_joueur()
         if len(donneur) ==0:
             print("J'ai terminé toutes les cartes.")
             print("Vous avez perdu ! Moi, Robot, jai gagné.")
             break
         print("*********************************************************")
         

         
         


    

	 
# programme principale
joue()

