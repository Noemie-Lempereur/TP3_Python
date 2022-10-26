class Maze:

    def __init__(self, fichier):
        self.__tableau = []
        file = open(fichier, "r")
        lines = file.readlines()
        for i in lines:
            tableau2 = []
            for j in i:
                if j != '\n':
                    tableau2.append(int(j))
            self.__tableau.append(tableau2)
        self.__hauteurTableau = len(self.__tableau)
        self.__largeurTableau = len(self.__tableau[0])

    def obtenirChiffreCase(self, x, y):
        return self.__tableau[x][y]

    def obtenirLargeur(self):
        return self.__largeurTableau

    def obtenirHauteur(self):
        return self.__hauteurTableau

    def placerChiffreCase(self, x, y, valeur):
        self.__tableau[x][y] = valeur
