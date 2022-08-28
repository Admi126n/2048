# import random
import os


class Gra:
    board = []

    def __init__(self, size=4):
        for row in range(size):
            self.board.append([])
            for column in range(size):
                self.board[row].append(0)

    def print_board(self):
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


# plansza = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
board = [[1, 2, 3, 4],
         [0, 5, 0, 8],
         [11, 0, 6, 10],
         [0, 0, 0, 7]]


# print_board(board)
# print()
# move_up(board)

tablica = [2, 2, 4, 4]
# ruch w lewo
print(f"input:  {tablica}")
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

print(f"output: {tablica}")
