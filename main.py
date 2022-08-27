import random
import time
import os
from traceback import print_tb


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

# clear_console()
# plansza = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# plansza = [[2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

x = Gra()
print(x.possible_move())


# plansza = ruch_do_gory(plansza)
# print()

# print_plansza(plansza)

# rozmiar = 4
# tablica = []
# print(tablica)
# for i in range(rozmiar):
#     tablica.append([])
#     for j in range(rozmiar):
#         tablica[i].append(0)
# print(tablica)
"""
for i in range(100):
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    if plansza[y][x] != 0:
        continue
    elif all(y == [2, 2, 2, 2] for y in plansza):
        break

    plansza[y][x] = 2
    print_plansza(plansza)
    ruch = input()
    match ruch:
        case "w":
            # ruch do gory
            for i in range(len(plansza) - 1):
                plansza[i] = plansza[i + 1]
        case "s":
            pass
        case "a":
            pass
        case "d":
            pass
        case __:
            pass

    # time.sleep(1)
    # clear_console()

print_plansza(plansza)
"""

