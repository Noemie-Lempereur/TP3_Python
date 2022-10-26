from maze import *
import turtle


class clTurtle:

    def __init__(self, largeurCarte, hauteurCarte, tailleCarre):
        self.__largeurcarte = largeurCarte
        self.__hauteurCarte = hauteurCarte
        self.__tailleCarre = tailleCarre
        turtle.setup(self.__hauteurCarte, self.__largeurcarte)
        turtle.title("Labyrinthe")
        turtle.speed(0)
        turtle.tracer(0)

    def __dessinerCarre(self, debutX, debutY, couleur):
        turtle.hideturtle()
        turtle.up()
        turtle.goto(debutX, debutY)
        turtle.fillcolor(couleur)
        turtle.begin_fill()
        turtle.down()
        for i in range(0, 4):
            turtle.forward(self.__tailleCarre)
            turtle.left(90)
        turtle.up()
        turtle.end_fill()

    def dessinerCarte(self, maze):
        for x in range(0, maze.obtenirHauteur()):
            for y in range(0, maze.obtenirLargeur()):
                if maze.obtenirChiffreCase(x, y) == 0:
                    self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                         -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre,
                                         "black")
                if maze.obtenirChiffreCase(x, y) == 1:
                    self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                         -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre,
                                         "green")
                if maze.obtenirChiffreCase(x, y) == 2:
                    self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                         -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre, "blue")
                if maze.obtenirChiffreCase(x, y) == 3:
                    self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                         -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre, "red")

    def parcourirCarte(self, maze):
        global x, y
        for xac in range(maze.obtenirLargeur()):
            for yac in range(maze.obtenirHauteur()):
                if maze.obtenirChiffreCase(xac, yac) == 1:  # pour obtenir les coordonnées de départ
                    x = xac
                    y = yac

        tabChemin = []
        while maze.obtenirChiffreCase(x, y) != 3:  # tant qu'on n'est pas à l'arrivée
            if (y - 1) > 0 and maze.obtenirChiffreCase(x, y - 1) == 2 or maze.obtenirChiffreCase(x, y - 1) == 3:
                tabChemin.append([x, y])
                maze.placerChiffreCase(x, y, -1)
                y = y - 1
                self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                     -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre, "purple")
            elif (x + 1) < maze.obtenirLargeur() and maze.obtenirChiffreCase(x + 1, y) == 2 or maze.obtenirChiffreCase(
                    x + 1, y) == 3:
                tabChemin.append([x, y])
                maze.placerChiffreCase(x, y, -1)
                x = x + 1
                self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                     -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre, "purple")
            elif (y + 1) < maze.obtenirLargeur() and maze.obtenirChiffreCase(x,
                                                                             y + 1) == 2 or maze.obtenirChiffreCase(
                x, y + 1) == 3:
                tabChemin.append([x, y])
                maze.placerChiffreCase(x, y, -1)
                y = y + 1
                self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                     -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre, "purple")
            elif (x - 1) > 0 and maze.obtenirChiffreCase(x - 1, y) == 2 or maze.obtenirChiffreCase(x - 1, y) == 3:
                tabChemin.append([x, y])
                maze.placerChiffreCase(x, y, -1)
                x = x - 1
                self.__dessinerCarre(y * self.__tailleCarre - self.__largeurcarte / 2,
                                     -x * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre, "purple")
            else:
                maze.placerChiffreCase(x, y, -1)
                tabCheminFini = tabChemin.pop()
                x = tabCheminFini[0]
                y = tabCheminFini[1]

        tabChemin.append([x, y])
        for i in tabChemin:
            self.__dessinerCarre(i[1] * self.__tailleCarre - self.__largeurcarte / 2,
                                 -i[0] * self.__tailleCarre + self.__hauteurCarte / 2 - self.__tailleCarre,
                                 "yellow")  # affichage du bon chemin

    def quitterAvecClick(self):
        turtle.exitonclick()
