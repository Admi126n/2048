import random
import os
import copy
import platform


def clear_console():
    """
    Clears console
    :return: None
    """
    operating_sys = platform.system()
    match operating_sys:
        case "Windows":
            os.system("cls")
        case "Linux" | "Darwin":
            os.system("clear")


"""
colors_codes = {
    "2": "\033[91m",
    "4": "\033[3;91m",
    "8": "\033[93m",
    "16": "\033[3;93m",
    "32": "\033[92m",
    "64": "\033[3;92m",
    "128": "\033[96m",
    "256": "\033[3;96m",
    "512": "\033[94m",
    "1024": "\033[3;94m",
    "2048": "\033[95m",
    "ABOVE": "\033[3;95m",
    # "END": "\033[0m"
}"""
colors_codes = {
    "2": "\033[2;38;2;255;0;0m",
    "4": "\033[2;38;2;255;128;0m",
    "8": "\033[2;38;2;255;255;0m",
    "16": "\033[2;38;2;128;255;0m",
    "32": "\033[2;38;2;0;255;0m",
    "64": "\033[2;38;2;0;255;128m",
    "128": "\033[2;38;2;0;255;255m",
    "256": "\033[2;38;2;0;128;255m",
    "512": "\033[2;38;2;0;0;255m",
    "1024": "\033[2;38;2;128;0;255m",
    "2048": "\033[2;38;2;255;0;255m",
    "ABOVE": "\033[2;38;2;255;0;128m",
    "END": "\033[0m"
}


class Game2048:
    possible_el = [2, 4]
    el_probability = [0.9, 0.1]
    board = []
    score = 0
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
        clear_console()
        self.get_actual_score()
        print(f"Score: {self.score}")
        col_width = max(len(str(el)) for row in self.board for el in row) + 1
        for row in self.board:
            output = ""
            for el in row:
                if el == 0:
                    output += "_".ljust(col_width)
                else:
                    output += self.return_color(el, col_width)
            print(output)
        print()

    @staticmethod
    def return_color(el, col_width):
        """
        Returns string with element with expected color and column width
        :param el: (int) element from board
        :param col_width: (int) expected column width
        :return: (string)
        """
        if el <= 2028:
            output = colors_codes.get(str(el))
        else:
            output = colors_codes.get("ABOVE")
        return output + str(el).ljust(col_width) + colors_codes.get("END")

    def empty_fields(self):
        """
        Func to check if board have any empty field
        :return: True if any field equals 0, False otherwise
        """
        return any(0 in el for el in self.board)

    def possible_move(self):
        """
        :return: True if there is possible move, False otherwise
        """
        if self.empty_fields():  # check if there are any zeros
            return True
        for row in self.board:  # check if there is horizontal move possible
            for i in range(self.size - 1):
                if row[i] == row[i + 1]:
                    return True
        for i in range(self.size - 1):  # check if there is vertical move possible
            for j in range(self.size):
                if self.board[i][j] == self.board[i + 1][j]:
                    return True
        return False

    def add_element(self):
        """
        Adds element to board if there is any empty field
        :return: None
        """
        el = random.choices(self.possible_el, self.el_probability)[0]
        while self.empty_fields():
            y_coordinate = random.randint(0, self.size - 1)
            x_coordinate = random.randint(0, self.size - 1)
            if self.board[y_coordinate][x_coordinate] == 0:
                self.board[y_coordinate][x_coordinate] = el
                break

    def get_actual_score(self):
        """
        Reset score variable and then adds all elements in board
        :return: None
        """
        self.score = 0
        for row in self.board:
            for el in row:
                self.score += el

    def read_size(self):
        """
        Reads input from user and set size variable
        :return: None
        """
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
        while self.possible_move():
            board_copy = copy.deepcopy(self.board)
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
                    self.print_board()
                    print("Exit")
                    break
                case __:
                    self.print_board()
                    continue
            if self.board != board_copy:
                self.add_element()
        else:
            self.print_board()
            print("Game over!")

    def move_up(self):
        added = [False for _ in range(self.size)]
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

    @staticmethod
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

    def move_right(self):
        for k, row in enumerate(self.board):
            row.reverse()
            self.move_horizontal(row)
            row.reverse()
            self.board[k] = row

    def move_left(self):
        for k, row in enumerate(self.board):
            self.move_horizontal(row)
            self.board[k] = row


if __name__ == "__main__":
    clear_console()
    game = Game2048()
    game.make_move()
