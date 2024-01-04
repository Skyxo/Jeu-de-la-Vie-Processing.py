import jdlv
import data
import time
import copy
add_library('controlP5')

tab_width, tab_height, width, height = 800, 800, 1100, 800

# Setup du programme
def setup():
    noStroke()
    size(width, height)
    
    # Boutons de paramètres
    cp5 = ControlP5(this)
    cp5.addButton('Start/Stop')\
       .setPosition(tab_width, 50)\
       .setSize(80,40)\
       .onClick(Pause)
       
    cp5.addButton('Reset')\
       .setPosition(tab_width, 90)\
       .setSize(80,40)\
       .onClick(Reset)
       
    cp5.addButton('+')\
       .setPosition(tab_width+80, 50)\
       .setSize(80,40)\
       .onClick(Zoom)
       
    cp5.addButton('-')\
       .setPosition(tab_width+80, 90)\
       .setSize(80,40)\
       .onClick(Dezoom)
       
    cp5.addButton('>>>')\
       .setPosition(tab_width+160, 50)\
       .setSize(80,40)\
       .onClick(Next)
       
    cp5.addButton('<<<')\
       .setPosition(tab_width+160, 90)\
       .setSize(80,40)\
       .onClick(Previous)
       
    cp5.addButton('+90')\
       .setPosition(tab_width, 170)\
       .setSize(80,40)\
       .setValue(1)\
       .onClick(Rotate)
    
    cp5.addButton('-90')\
       .setPosition(tab_width+80, 170)\
       .setSize(80,40)\
       .setValue(-1)\
       .onClick(Rotate)
       
    cp5.addButton('Sym X')\
       .setPosition(tab_width, 210)\
       .setSize(80,40)\
       .setValue(0)\
       .onClick(Symetrie)
       
    cp5.addButton('Sym Y')\
       .setPosition(tab_width+80, 210)\
       .setSize(80,40)\
       .setValue(1)\
       .onClick(Symetrie)
       
    # Boutons pour placer les figures
    p = 0
    m = 0
    for i in range(len(data.placing)):
        cp5.addButton(data.placing_names[i])\
        .setPosition(tab_width+80*m, 330+40*p)\
        .setSize(80,40)\
        .setValue(i)\
        .onClick(Placing)
        
        if i%3 == 0:
            p+=1
            
        m = m+1 if i%3 else 0
        
    # Boutons de paramètres
    cp5.addButton('Get Figure')\
       .setPosition(width-240, height-40)\
       .setSize(80,40)\
       .onClick(GetFigure)   
    
    cp5.addButton('Cellules')\
       .setPosition(width-160, height-40)\
       .setSize(80,40)\
       .onClick(Count)   
       
    cp5.addButton('Export')\
       .setPosition(width-80, height-40)\
       .setSize(80,40)\
       .onClick(Export)
        
# Variables 
p = 5                                 # Taille du débordement de la grille
n = 10                                # Taille initiale de la grille
tableau = jdlv.createTableau(n, p)    # Définition du tableau
tab_data = [copy.copy(tableau)] # Définition des sauvegardes
periode = 0                           # Initialisation de la période
pause = True                          # Pause
placing = [[0, 0]]                    # Placement des figures
zoomspeed = 5                         # Vitesse du zoom
coord_fig = (0, 0)

# Dessin du programme
def draw():
    global tableau, n, p, pause, placing, periode, tab_data
    
    background(0)
    
    # Texte
    fill(255)
    textAlign(LEFT)
    text("Periode : {}".format(periode), tab_width, 20)
    text("Cellules en vie : {}".format(jdlv.compteur(tableau)), tab_width, 35)
    text("Coordonees figure : {}".format(coord_fig), width-240, height-45)
    textAlign(RIGHT)
    text("Zoom : {}".format(n), width, 20)

    # Affichage de la grille
    fill(255)
    for i in range(n):
        for o in range(n):
            if tableau[i+p][o+p]:
                rect(o*tab_width/n, i*tab_height/n, tab_width/n, tab_height/n)
            
    # Affichage des formes sous le curseur
    textAlign(LEFT)
    fill(105)
    for i in range(n):
        for o in range(n):
           if mouseX >= o*tab_width/n\
               and mouseX < o*tab_width/n+tab_width/n\
               and mouseY >= i*tab_height/n\
               and mouseY < i*tab_height/n+tab_height/n:
             
                for coord in placing:
                    rect((coord[0]+o)*tab_width/n, (coord[1]+i)*tab_height/n, tab_width/n, tab_height/n)
                
                fill(255)
                text("(x, y) = ({}, {})".format(o+p, i+p), 10, 20)
    
    # Contrôle de la souris                
    if not pause or keyPressed and keyCode == RIGHT:
        Next(keyPressed)
        
    if keyPressed and keyCode == LEFT and periode > 0:
        Previous(keyPressed)
        
# Maintient de la souris et placement des figures
def mouseDragged():
    global tableau, periode, tab_data
 
    for i in range(n):
        for o in range(n):
            if mouseX >= o*tab_width/n\
                 and mouseX < o*tab_width/n+tab_width/n\
                 and mouseY >= i*tab_height/n\
                 and mouseY < i*tab_height/n+tab_height/n:
                    
                    # Placement de la figure sélectionnée
                    for coord in placing:
                        try:
                            if mouseButton == LEFT and not tableau[coord[1]+i+p][coord[0]+o+p]:
                                tableau[coord[1]+i+p][coord[0]+o+p] = 1
                            elif mouseButton == RIGHT and tableau[coord[1]+i+p][coord[0]+o+p]:    
                                tableau[coord[1]+i+p][coord[0]+o+p] = 0
                        except:
                            pass
    
    # Effacement des tableaux sauvegardés après placement d'une nouvelle figure

    tab_data[-1] = tableau
    tab_data = tab_data[0:periode+1]
    
    
# Clique de la souris et placement des figures
def mouseClicked():
    global coord_fig
    
    if mouseX >= 0\
        and mouseX < tab_width\
        and mouseY >= 0\
        and mouseY < tab_height:
        if mouseButton == CENTER:
            coord_fig = getMouseCord()
            print("Les coordonnées du centre de votre figure sont : {}".format(coord_fig))
        else:
            mouseDragged()
        
def getMouseCord():
    
    for i in range(n):
        for o in range(n):
           if mouseX >= o*tab_width/n\
               and mouseX < o*tab_width/n+tab_width/n\
               and mouseY >= i*tab_height/n\
               and mouseY < i*tab_height/n+tab_height/n:
                
                return (o+p, i+p)
    
# Affiche la grille dans la console
def afficheConsole(tab):
    
    for i in range(p, n-p):
        print(tab[i])
        
    print("\n")
    
    for i in range(len(tab)):
        print(tab[i])
    
# Pause
def Pause(event):
    global pause
    pause = False if pause else True
    
# Nettoyage de la grille et des paramètres
def Reset(event):
    global tableau, n, periode, pause, p, tab_data
    
    tableau = jdlv.createTableau(n, p)
    tab_data = [tableau]
    pause = True
    periode = 0
    
# Dezoom de la grille
def Dezoom(event):
    global tableau, n, pause, zoomspeed
    
    n+=zoomspeed*2
        
    for i in range(len(tableau)):
        for o in range(zoomspeed):
            tableau[i].append(0)
            tableau[i].insert(0, 0)
        
    for i in range(zoomspeed):
        tableau.insert(0, [0 for o in range(n+zoomspeed*2)])
        tableau.append([0 for o in range(n+zoomspeed*2)])
    
# Zoom dans la grille
def Zoom(event):
    global tableau, n, pause, zoomspeed
    if n-zoomspeed*2 > 0:
        n-=zoomspeed*2
    
        del tableau[0:zoomspeed]
        del tableau[-zoomspeed-1:-1]
    
        for i in range(n):
            del tableau[i][0:zoomspeed]
            del tableau[i][-zoomspeed-1:-1]
    else:
        pass
    
# Passage à la période suivante
def Next(event):
    global tableau, periode, n, p, tab_data
    
    periode+=1
    try:
        tableau = tab_data[periode]
    except:
        tableau = jdlv.actualize(tableau, n, p)
        tab_data.append(tableau)

# Période précédente
def Previous(event):
    global tableau, periode, pause, tab_data
    
    pause = True
    if periode-1 >= 0:
        periode-=1
        tableau = tab_data[periode]
    
# Choix de la figure à placer
def Placing(event):
    global placing
    value = int(event.getController().getValue())
    placing = data.placing[value]
    
# Exportation du tableau dans le fichier export.txt
def Export(event):
    global tableau
    try:
        jdlv.exportTab(tableau)    
        print('Structure exportee avec succes dans le fichier "export.txt" !')
    except:
        print("Erreur lors de l'exportation du tableau")

# Comptage des cellules vivantes dans l'environnement
def Count(event):

    global tableau, n
    
    print("Le nombre de cellules en vie est de {} cellules.".format(jdlv.compteur(tableau)))

# Transformation par symetrie axiale de la figure
def Symetrie(event):
    global placing
    
    value = int(event.getController().getValue())
    
    for i in range(len(placing)):
        placing[i][0], placing[i][1] = (-1)**value*placing[i][0], (-1)**(value+1)*placing[i][1]
    
# Transformation par rotation de la figure
def Rotate(event):
    global placing
    
    value = int(event.getController().getValue())
    
    r90 = [[0, -1*value],
           [1*value, 0]]
    
    for i in range(len(placing)):
        placing[i][0], placing[i][1] = jdlv.produit_matriciel(r90, [[placing[i][0]], [placing[i][1]]])
        
def GetFigure(event):
    global coord_fig
    
    jdlv.convertisseur(tableau, coord_fig)
