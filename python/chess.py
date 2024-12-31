class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return 'K' if self.color == 'white' else 'k'

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return 'N' if self.color == 'white' else 'n'

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __str__(self):
        return 'P' if self.color == 'white' else 'p'

class Board:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                if i == 1:
                    row.append(Pawn('black', j, i))
                elif i == 6:
                    row.append(Pawn('white', j, i))
                elif i == 0:
                    if j in [0, 7]:
                        row.append(Rook('black', j, i))
                    elif j in [1, 6]:
                        row.append(Knight('black', j, i))
                    elif j in [2, 5]:
                        row.append(Bishop('black', j, i))
                    elif j == 3:
                        row.append(Queen('black', j, i))
                    elif j == 4:
                        row.append(King('black', j, i))
                elif i == 7:
                    if j in [0, 7]:
                        row.append(Rook('white', j, i))
                    elif j in [1, 6]:
                        row.append(Knight('white', j, i))
                    elif j in [2, 5]:
                        row.append(Bishop('white', j, i))
                    elif j == 3:
                        row.append(Queen('white', j, i))
                    elif j == 4:
                        row.append(King('white', j, i))
                else:
                    row.append(None)
            board.append(row)
        return board

    def print_board(self):
        print('  a b c d e f g h')
        for i in range(8):
            print(i + 1, end=' ')
            for j in range(8):
                if self.board[i][j]:
                    print(self.board[i][j], end=' ')
                else:
                    print('.', end=' ')
            print()

    def move_piece(self, x1, y1, x2, y2):
        if self.board[y1][x1]:
            piece = self.board[y1][x1]
            self.board[y1][x1] = None
            self.board[y2][x2] = piece
            piece.move(x2, y2)

def main():
    board = Board()
    while True:
        board.print_board()
        x1 = ord(input("Enter x coordinate of piece to move (a-h): ")) - 97
        y1 = int(input("Enter y coordinate of piece to move (1-8): ")) - 1
        x2 = ord(input("Enter x coordinate of destination (a-h): ")) - 97
        y2 = int(input("Enter y coordinate of destination (1-8): ")) - 1
        board.move_piece(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
