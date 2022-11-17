from random import randint
# On creer la surface de morpion
tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]

# On creer une fonction qui renvoi la surface de morpion
def showTable(tableGame):
    print("\n--------------")
    for row in tableGame :
        for item in row:
            print(item, end="  ")
        print()
    print("--------------\n")

# On creer une fonction qui verifie que le coup d'un joueur est valide
def caseFilled(board, posx, posy):
    if board[posx][posy] == '-':
        return False
    else:
        return True

#######################

# On creer une fonction qui renvoie si un joueur gagne
def is_player_win(board, player):
    win = None

    n = len(board)

    # on verifie les lignes
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    # on verifie la colonnes
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # on verifie les diagonales
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

# On verifie si la surface de morpion est pleine 
def is_board_filled(board):
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True
#######################
# On demmarre la partie de morpion
startGame = input("Voulez-vous jouer ? oui ou non : \n")
if startGame == "oui":
    continuer = True
    playerOne = input("Joueur X choisissez votre pseudo : \n")
    playerTwo = input("Joueur O choisissez votre pseudo : \n")
elif startGame == "non":
    print("\nTant pis, à une prochaine  \n")
    continuer = False
else:
    startGame = input("Voulez-vous jouer ? oui ou non : \n")
    if startGame == "oui":
        continuer = True
        playerOne = input("Joueur X choisissez votre pseudo : \n")
        playerTwo = input("Joueur O choisissez votre pseudo : \n")
    elif startGame == "non":
        print("\nTant pis, à une prochaine \n")
        continuer = False
    else:
        startGame = input("Voulez-vous jouer ? oui ou non : \n")
        if startGame == "oui":
            continuer = True
            playerOne = input("Joueur X choisissez votre pseudo : \n")
            playerTwo = input("Joueur O choisissez votre pseudo : \n")
        elif startGame == "non":
            print("\nTant pis, à une prochaine  \n")
            continuer = False

#tant que la variable continuer est egale a vrai alors envoyer le programme du morpion
while continuer == True :
    
    playerOneShoot = "X"
    playerTwoShoot = "O"
    playerStart = randint(1, 2)
    
    if playerStart == 1:
    
        playerTurn = playerOne
        playerShoot = playerOneShoot
    else:
        
        playerTurn = playerTwo
        playerShoot = playerTwoShoot
    
    correctShoot = False
    playerWin = False 
    
    showTable(tableGame)
    while playerWin == False:
        while correctShoot == False :
            print("Au Tour de " + playerTurn + "\n")
            choiceX = int(input("Choisissez la ligne à modifier ( 0 = Ligne 1 ; 1 = Ligne 2 ; 2 = Ligne 3) : \n"))
            choiceY = int(input("Choisissez la colonne à modifier ( 0 = Colonne 1 ; 1 = Colonne 2 ; 2 = Colonne 3) : \n"))
            if caseFilled(tableGame, choiceX, choiceY) != True:
                tableGame[choiceX][choiceY] = playerShoot
                correctShoot = True 
        showTable(tableGame)

        if is_player_win(tableGame, playerShoot):
            print("Le joueur " + playerTurn +  " à gagné la partie ! :) ")
            break
        
        if is_board_filled(tableGame):
            print("Egalité ! :/")
            break

        if playerShoot == playerOneShoot:
            playerShoot = playerTwoShoot
            playerTurn = playerTwo
        else : 
            playerShoot = playerOneShoot
            playerTurn = playerOne

        correctShoot = False
    
    #on creer une variable otherGame qui va permettre au joueurs de pouvoir rejouer ou non
    otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
    if otherGame == "oui":
        print("C'est reparti !")
        tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
        continuer = True
    elif otherGame == "non":
        print("Au bientôt !")
        continuer = False
    
    else:
        otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
        if otherGame == "oui":
            print("C'est reparti !")
            tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
            continuer = True

        elif otherGame == "non":
            print("Au bientôt !")
            continuer = False

        else:
            otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
            if otherGame == "oui":
                print("C'est reparti !")
                tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
                continuer = True

            elif otherGame == "non":
                print("Au bientôt !")
                continuer = False


         

