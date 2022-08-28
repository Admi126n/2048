import random
import os
# TODO make branches


class Gra:
    possible_el = [2, 4]
    el_probability = [0.9, 0.1]
    score = 0
    board = []
    size = 0

    def __init__(self, size=4):
        self.size = size
        for row in range(size):
            self.board.append([])
            for column in range(size):
                self.board[row].append(0)

    def print_board(self):
        # TODO add formatting to print board pretty good even if there are longer numbers
        for row in self.board:
            for column in row:
                print(column, end=" ")
            print()

    def possible_move(self):
        # TODO there are possible moves even if all fields contains value so this condition is not enough
        """
        Func to check if any move is possible
        :return: True if any field equals 0, False otherwise
        """
        return any(0 in el for el in self.board)

    def add_element(self):
        el = random.choices(self.possible_el, self.el_probability)[0]
        while True:
            y_coordinate = random.randint(0, self.size - 1)
            x_coordinate = random.randint(0, self.size - 1)
            if self.board[y_coordinate][x_coordinate] == 0:
                self.board[y_coordinate][x_coordinate] = el
                break

    def get_actual_score(self):
        self.score = max(max(el) for el in self.board)

    def move_left(self):
        dodano = False
        for row in self.board:
            for i, el in enumerate(row):
                dest = i
                if i == 0:
                    continue
                for j in range(i, -1, -1):
                    if row[j] == 0:
                        dest = j
                row[dest] = el
                if dest != i:
                    row[i] = 0

                if dodano:
                    dodano = False
                    continue
                if row[dest - 1] == row[dest]:
                    row[dest - 1] *= 2
                    row[dest] = 0
                    dodano = True

def clear_console():
    os.system("cls")


def print_board(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print()


def move_up(board):
    for i, row in enumerate(board):
        if i == 0:
            continue
        dest_row = 0
        for j, el in enumerate(row):
            for k in range(i, -1, -1):
                if board[k][j] == 0:
                    dest_row = k
        print(dest_row, end=" ")
    return board

"""
# plansza = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
board = [[1, 2, 3, 4],
         [0, 5, 0, 8],
         [11, 0, 6, 10],
         [0, 0, 0, 7]]

def ruch_w_lewo(tablica):
    dodano = False
    for i, el in enumerate(tablica):
        dest = i
        if i == 0:
            continue
        for j in range(i, -1, -1):
            if tablica[j] == 0:
                dest = j
        tablica[dest] = el
        if dest != i:
            tablica[i] = 0

        if dodano:
            dodano = False
            continue
        if tablica[dest - 1] == tablica[dest]:
            tablica[dest - 1] *= 2
            tablica[dest] = 0
            dodano = True

tablica = [2, 2, 2, 2]
# ruch w lewo
print(f"input:   {tablica}")
ruch_w_lewo(tablica)
print(f"output:  {tablica}")
ruch_w_lewo(tablica)
print(f"output2: {tablica}")
"""
x = Gra()
for i in range(10):
    x.add_element()
    print()
x.print_board()
x.move_left()
print()
x.print_board()
