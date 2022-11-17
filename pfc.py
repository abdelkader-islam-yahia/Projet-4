#debut
from random import randint

jeu = ["pierre","feuille", "ciseaux"] 
jouer = input("Veut-tu jouer au Pierre Feuille Ciseaux \n>")
nom=""
nomCpu=""

if jouer == "oui":
    continuer = True 
    nom = input("Entrez votre pseudo : \n")
    nomCpu = input("Entrez le pseudo du Cpu : \n")

    
if jouer == "non":
    continuer = False


scoreCpu = 0
scoreJoueur = 0

while continuer == True:
     
    if jouer == "oui": 
        cpu = jeu[randint(0,2)]
        joueur = input("pierre, feuille ou ciseaux \n>")
        if joueur == "ciseaux":
            if cpu == "pierre":
                scoreCpu += 1
                print( nomCpu + " is winner")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
            elif cpu == "feuille":
                scoreJoueur += 1
                print("You win GG") 
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
            else:
                print("it's draw, retry")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
        elif joueur == "feuille":
            if cpu == "pierre":
                scoreJoueur += 1
                print("You win GG")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
            elif cpu == "feuille":
                print("it's a draw, retry")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
            else:
                scoreCpu += 1
                print( nomCpu + " is winner")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
        elif joueur == "pierre":
            if cpu == "pierre":
                print("it's a draw, retry")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
            elif cpu == "feuille":
                scoreCpu += 1
                print( nomCpu + " is winner")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")
            else:
                scoreJoueur += 1
                print("You win, GG")
                print("-----------------------\n" + nom + " : " + str(scoreJoueur) + " | "   +joueur +"\n"+ "" + nomCpu + " : " + str(scoreCpu) + " | " +cpu + "\n-----------------------")


        if scoreJoueur == 3:
            print("GG jeune padawan, tu a gagner contre ce maudit bot")
            print(nom + " : " + str(scoreJoueur)  +"\n"+ "" + nomCpu + " : " + str(scoreCpu) )
        
            jouer = input("Voulez-vous rejouer ?\n")
            if joueur == "oui":
                continuer = True
                scoreCpu = 0
                scoreJoueur = 0
            elif joueur == "non" : 
                print("Bye Bye")
                continuer = False
                

        elif scoreCpu == 3:
            print("Passe le bonjour depuis la tombe de la honte, un bot restera un bot ")
            print(nom + " : " + str(scoreJoueur)  +"\n"+ "" + nomCpu + " : " + str(scoreCpu))
        
            jouer = input("Voulez-vous rejouer ? \n")
            if jouer == "oui":
                continuer = True
                scoreCpu = 0
                scoreJoueur = 0
            
            elif jouer == "non" : 
                print("Bye Bye")
                continuer = False
                

    
    elif jouer == "non":
        continuer = False
    
    
        
#fin


