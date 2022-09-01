import random
import os


def move_horizontal(row):
    # TODO make @staticmethod
    added = False
    for i, el in enumerate(row):
        dest = i
        if el == 0 or i == 0:
            continue
        for j in range(i, -1, -1):
            if row[j] == 0:
                dest = j
        row[dest] = el
        if dest != i:
            row[i] = 0
        if added:
            added = False
            continue
        if dest == 0:
            continue
        if row[dest - 1] == row[dest]:
            row[dest - 1] *= 2
            row[dest] = 0
            added = True
    return row


def clear_console():
    os.system("cls")


class Game2048:
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
        # TODO add colors to the output
        for row in self.board:
            for column in row:
                print(column, end=" ")
            print()
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
        while self.possible_move():
            y_coordinate = random.randint(0, self.size - 1)
            x_coordinate = random.randint(0, self.size - 1)
            if self.board[y_coordinate][x_coordinate] == 0:
                self.board[y_coordinate][x_coordinate] = el
                break

    def get_actual_score(self):
        self.score = max(max(el) for el in self.board)

    def get_input(self):
        while True:
            move = input()
            match move:
                case "w":
                    self.move_up()
                    clear_console()
                    self.print_board()
                case "s":
                    self.move_down()
                    clear_console()
                    self.print_board()
                case "a":
                    self.move_left()
                    clear_console()
                    self.print_board()
                case "d":
                    self.move_right()
                    clear_console()
                    self.print_board()
                case "ex":
                    break
                case __:
                    pass

    def move_up(self):
        added = [False for i in range(self.size)]
        for i, row in enumerate(self.board):
            if i == 0:
                continue
            for j, el in enumerate(row):
                dest = i
                if el == 0:
                    continue
                for k in range(i, -1, -1):
                    if self.board[k][j] == 0:
                        dest = k
                if dest != i:
                    self.board[dest][j] = el
                    self.board[i][j] = 0
                if added[j]:
                    added[j] = False
                    continue
                if dest == 0:
                    continue
                if self.board[dest - 1][j] == self.board[dest][j]:
                    self.board[dest - 1][j] *= 2
                    self.board[dest][j] = 0
                    added[j] = True
        self.add_element()

    def move_down(self):
        self.board.reverse()
        self.move_up()
        self.board.reverse()
        self.add_element()

    def move_right(self):
        for k, row in enumerate(self.board):
            row.reverse()
            move_horizontal(row)
            row.reverse()
            self.board[k] = row
        self.add_element()

    def move_left(self):
        for k, row in enumerate(self.board):
            move_horizontal(row)
            self.board[k] = row
        self.add_element()


test = Game2048()
for x in range(4):
    test.add_element()

test.print_board()
# print("dupa")
# clear_console()
# os.system("cls")

test.get_input()





