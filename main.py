import random
import os


class Gra:
    plansza = []

    def __init__(self, rozmiar=4):
        for row in range(rozmiar):
            self.plansza.append([])
            for column in range(rozmiar):
                self.plansza[row].append(0)

    def print_plansza(self):
        for row in self.plansza:
            for column in row:
                print(column, end=" ")
            print()

    def possible_move(self):
        # TODO there are possible moves even if all fields contains value so this condition is not enough
        """
        Func to check if any move is possible
        :return: True if any field equals 0, False otherwise
        """
        return any(0 in el for el in self.plansza)

def clear_console():
    os.system("cls")

def ruch_do_gory(plansza):
    for i in range(len(plansza) - 1):
        for j in range(len(plansza[i])):
            if plansza[i + 1][j] != 0:
                plansza[i][j] = plansza[i + 1][j]
        # plansza[i] = plansza[i + 1]
    return plansza

# plansza = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
plansza = [[0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

"""
for i in range(100):
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    if plansza[y][x] != 0:
        continue
    elif all(y == [2, 2, 2, 2] for y in plansza):
        break
"""

