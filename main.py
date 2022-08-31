import random
import os


def move_horizontal(row):
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


# def move_vertical():
#     pass


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
        while True and self.possible_move():
            y_coordinate = random.randint(0, self.size - 1)
            x_coordinate = random.randint(0, self.size - 1)
            if self.board[y_coordinate][x_coordinate] == 0:
                self.board[y_coordinate][x_coordinate] = el
                break

    def get_actual_score(self):
        self.score = max(max(el) for el in self.board)

    def move_right(self):
        for k, row in enumerate(self.board):
            row.reverse()
            move_horizontal(row)
            row.reverse()
            self.board[k] = row

    def move_left(self):
        for k, row in enumerate(self.board):
            move_horizontal(row)
            self.board[k] = row

    def move_up(self):
        pass

    def move_down(self):
        pass


def clear_console():
    os.system("cls")


def move_vertical(tab):
    for i, row in enumerate(tab):
        if i == 0:
            continue
        for j, el in enumerate(row):
            dest = i
            if el == 0:
                continue
            for k in range(i, -1, -1):
                if tab[k][j] == 0:
                    dest = k
            if dest != i:
                tab[dest][j] = el
                tab[i][j] = 0
            # if dest == 0:
            #     continue
            # if tab[dest - 1][j] == tab[dest][j]:
            #     tab[dest - 1][j] *= 2
            #     tab[dest][j] = 0


def print_tab(tab):
    for row in tab:
        print(row)


# test = [[1, 2], [3, 4], [5, 6], [7, 8]]
test = [[0, 1], [2, 3], [4, 0], [0, 5]]
game_board = [[2, 2], [2, 2], [4, 0], [2, 2]]

# print_tab(test)
# move_vertical(test)
# print()
# print_tab(test)

# print()

print_tab(game_board)
move_vertical(game_board)
print()
print_tab(game_board)