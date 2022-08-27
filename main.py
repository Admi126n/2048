import random
import time
import os


def clear_console():
    os.system("cls")

def print_plansza(plansza):
    for y in plansza:
        for x in y:
            print(x, end=" ")
        print()
clear_console()
plansza = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(100):
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    if plansza[y][x] != 0:
        continue
    elif all(y == [2, 2, 2, 2] for y in plansza):
        break

    plansza[y][x] = 2
    print_plansza(plansza)
    time.sleep(1)
    clear_console()

print_plansza(plansza)


