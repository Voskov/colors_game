import random
import sys


class BoardGame:
    WIDTH = 8
    HEIGHT = 8
    ROUNDS = 21

    def __init__(self):
        self.turn = 0
        self.board = None
        self.move = None
        self.initialize_board()

    def initialize_board(self):
        self.board = [[random.choice(['r', 'g', 'b', 'y']) for _ in range(self.HEIGHT)] for _ in range(self.WIDTH)]

    def take_turn(self):
        move = input(f"{self.turn}/{self.ROUNDS} Moves. Insert color:\n").lower()[0]
        retries = 0
        while not self.valid_move(move):
            retries += 1
            if retries > 3:
                print("Oh, I give up!")
                raise Exception("User is stupid and can't follow simple instructions")
            print("Please type one of these colors: red, green, blue, yellow")
            print("And make sure that you aren't repeating the same color")
            move = input(f"{self.turn}/{self.ROUNDS} Moves. Insert color:\n").lower()[0]
        self.turn += 1
        self.move = move

    def valid_move(self, move):
        return move in ['r', 'g', 'b', 'y'] and move != self.board[0][0]

    def print_board(self):
        for row in self.board:
            print(row)

    def is_won(self):
        # Naive
        for r in range(self.HEIGHT):
            for c in range(self.WIDTH):
                if self.board[c][r] != self.board[0][0]:
                    return

        print("Congratulations! You have beaten the game!")
        sys.exit(0)

    def flip_colors(self):
        before_color = self.board[0][0]
        cells_to_flip = [(0, 0)]
        flipped_cells = set()
        while cells_to_flip:
            flipping_cell = cells_to_flip.pop(0)
            considering_cells = [(flipping_cell[0], flipping_cell[1] + 1), (flipping_cell[0] + 1, flipping_cell[1]),
                                 (flipping_cell[0], flipping_cell[1] - 1), (flipping_cell[0] - 1, flipping_cell[1])]
            for cell in considering_cells:
                if cell in flipped_cells:
                    continue
                if not self.is_cell_on_board(cell):
                    continue
                if not self.board[cell[0]][cell[1]] == before_color:
                    continue
                cells_to_flip.append(cell)
            self.board[flipping_cell[0]][flipping_cell[1]] = self.move
            flipped_cells.add(flipping_cell)

    def is_cell_on_board(self, cell_coords):
        return 0 <= cell_coords[0] < self.WIDTH and 0 <= cell_coords[1] < self.HEIGHT

    def game(self):
        self.print_board()
        while self.turn <= self.ROUNDS:
            self.take_turn()
            self.flip_colors()
            self.print_board()
            self.is_won()

        print("Sorry, you just aren't good enough")


if __name__ == "__main__":
    bg = BoardGame()
    bg.game()
