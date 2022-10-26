import turtle
from classTurtle import *

from maze import *

if __name__ == '__main__':
    test = Maze("Maze.txt")
    testTurtle = clTurtle(700, 700, 5)
    testTurtle.dessinerCarte(test)
    testTurtle.parcourirCarte(test)
    testTurtle.quitterAvecClick()
