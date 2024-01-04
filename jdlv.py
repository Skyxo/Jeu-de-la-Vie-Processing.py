#  coding: utf-8
# Algorithmes et fonctions utiles pour le programme

def produit_matriciel(A, B): # Produit matriciel entre les matrices A et B
    lgAi = len(A)
    lgAj = len(A[0])
    lgBi = len(B)
    lgBj = len(B[0])

    if lgAj != lgBi:
        return False

    lg = lgAj
    M = []

    for i in range(lgAi):
        M.append([])

        for j in range(lgBj):            
            M[i].append(sum([A[i][k]*B[k][j] for k in range(lg)]))

    return M[0][0], M[1][0]

def createTableau(n, p): # Création d'une grille vide
    tb_ = []
    for i in range(n+2*p):
        tb_.append([])
        for o in range(n+2*p):
            tb_[i].append(0)

    return tb_

def actualize(liste, n, p): # Algorithme d'actualisation n°1
    
    lg = len(liste)
    compteur = 0
    liste2 = createTableau(n, p)

    # On parcours la grille en regardant les voisins de chacunes cellules
    for y in range(lg):

        for x in range(lg):
            
            if y == 0 and x == 0:                   # cote en haut a gauche

                if liste[y][x+1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                            
            elif y == 0 and x == lg-1:              # cote en haut a droite

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1
                            
            elif y == lg-1 and x == 0:              # cote en bas a gauche

                if liste[y][x+1]:
                    compteur += 1

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1
                            
            elif y == lg-1 and x == lg-1:           # cote en bas a droite

                if liste[y][x-1]:
                    compteur += 1

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1
                        
            elif y == 0 and 1 <= x <= lg-1:         # ligne du haut

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1   
            
            elif 1 <= y <= lg-1 and x == 0:         # colonne de gauche

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1  
                
            elif y == lg-1 and 1 <= x <= lg-1:      # ligne du bas

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1

                if liste[y][x-1]:
                    compteur += 1  
                    
            elif 1 <= y <= lg-1 and x == lg-1:      # colonne de droite

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1  
                
            else:                                   # tous les autres

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1
        
            if liste[y][x]:                          # application des règles

                if compteur >= 2 and compteur <= 3:
                    liste2[y][x] = 1

                else:
                    liste2[y][x] = 0

            elif compteur == 3:
                liste2[y][x] = 1
            compteur = 0

    return liste2

def getNeighbors(tab, y, x): # Recherche des cellules voisines de la cellule ayant pour coordonnées (x,y)
    neighbors = 0
            
    for i in range(-1, 2):
        for o in range(-1, 2):
            
            neighbors+=tab[y+i][x+o] if i!=0 or o!=0 else 0
                    
    return neighbors

def actualize_bis(liste, n, p): # Algorithme d'actualisation n°2
    
    lg = len(liste)
    compteur = 0
    liste2 = createTableau(n, p)

    for y in range(2, lg-2):
        for x in range(2, lg-2):
            
            compteur = getNeighbors(liste, y, x)
                                
            if liste[y][x]: # application des règles
        
                if compteur == 2 or compteur == 3:
                    liste2[y][x] = 1
        
            elif compteur == 3:
                liste2[y][x] = 1
        
            compteur = 0

    return liste2

def exportTab(tableau): # Exportation de la grille dans le fichier export.txt
    export = open("export.txt", "w")
    
    export.write('[')
    for i in range(len(tableau)):
        export.write('[')
        for o in range(len(tableau[i])):
            if o == len(tableau[i])-1:
                export.write(str(tableau[i][o]))
            else:
                export.write(str(tableau[i][o])+',')
        if i == len(tableau)-1:
            export.write(']')
        else:
            export.write('],\n')
    
    export.write(']')
    export.close()

def compteur(tab): # Compte les cellules en vie dans l'environnement
    count = 0
    lg = len(tab)
    for i in range(lg):
        for o in range(lg):
            count += tab[i][o]
            
    return count

def convertisseur(initial_, initial_point):
    
    list_ = []
    
    for y in range(len(initial_)):
        for x in range(len(initial_[y])):
            if initial_[y][x]:
                list_.append([x-initial_point[0], y-initial_point[1]])
            
    print("[")    
    for i in range(len(list_)):
        if i != len(list_)-1:
            print("[{}, {}],".format(list_[i][0], list_[i][1]))
        else:
            print("[{}, {}]]".format(list_[i][0], list_[i][1]))
