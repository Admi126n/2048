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
        dest_row = 0
        for j, el in enumerate(row):
            for k in range(i, -1, -1):
                if board[k][j] == 0:
                    dest_row = k
        print(dest_row)
    return board


# plansza = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
board = [[1, 2, 3, 4],
         [0, 5, 0, 8],
         [0, 0, 6, 10],
         [0, 0, 0, 7]]


print_board(board)
move_up(board)


"""
for i in range(100):
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    if plansza[y][x] != 0:
        continue
    elif all(y == [2, 2, 2, 2] for y in plansza):
        break
"""

