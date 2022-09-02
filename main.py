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


class Colors:
    # needed 11 colors
    pass


class Game2048:
    possible_el = [2, 4]
    el_probability = [0.9, 0.1]
    score = 0
    board = []
    size = 0

    def __init__(self):
        self.read_size()
        for row in range(self.size):
            self.board.append([])
            for column in range(self.size):
                self.board[row].append(0)
        for i in range(2):
            self.add_element()

    def print_board(self):
        # TODO add colors to the output
        clear_console()
        col_width = max(len(str(el)) for row in self.board for el in row) + 1
        for row in self.board:
            output = ""
            for el in row:
                output += self.return_color(el)
                output += str(el).replace("0", "_").ljust(col_width)
                output += "\033[0m"
            print(output)
        print()

    @staticmethod
    def return_color(el):
        if el == 2:
            return f"\033[2;38;2;128;255;219m"
        elif el == 4:
            return f"\033[2;38;2;114;239;221m"
        elif el == 8:
            return f"\033[2;38;2;100;223;223m"
        elif el == 16:
            return f"\033[2;38;2;86;207;225m"
        elif el == 32:
            return f"\033[2;38;2;72;191;227m"
        elif el == 64:
            return f"\033[2;38;2;78;168;222m"
        return ""

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

    def read_size(self):
        while True:
            temp = input("Type board size: ")
            try:
                temp = int(temp)
                if temp < 2 or temp > 10:
                    clear_console()
                    print("Type number between 2 and 10!")
                else:
                    self.size = temp
                    return
            except ValueError:
                clear_console()
                print("This is not a number!")

    def make_move(self):
        while True:
            self.print_board()
            move = input()
            match move:
                case "w":
                    self.move_up()
                case "s":
                    self.move_down()
                case "a":
                    self.move_left()
                case "d":
                    self.move_right()
                case "ex":
                    break
                case __:
                    self.print_board()
                    continue
            self.add_element()

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

    def move_down(self):
        self.board.reverse()
        self.move_up()
        self.board.reverse()

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


if __name__ == "__main__":
    clear_console()
    game = Game2048()
    game.make_move()
