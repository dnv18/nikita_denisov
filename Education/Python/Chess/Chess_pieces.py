from Chess_interfaces import IFigure


class Pawn(IFigure):
    def get_moves(self):
        my_pos = self.get_pos()
        ans = []
        if self.not_moved:
            if self.colour == 'white':
                t_ans = [(my_pos[0] - 2, my_pos[1]), (my_pos[0] - 1, my_pos[1])]
            else:
                t_ans = [(my_pos[0] + 2, my_pos[1]), (my_pos[0] + 1, my_pos[1])]
        else:
            if self.colour == 'white':
                t_ans = [(my_pos[0] - 1, my_pos[1])]
            else:
                t_ans = [(my_pos[0] + 1, my_pos[1])]
        if self.colour == 'white':
            t_ans.append((my_pos[0] - 1, my_pos[1] - 1))
            t_ans.append((my_pos[0] - 1, my_pos[1] + 1))
        else:
            t_ans.append((my_pos[0] + 1, my_pos[1] - 1))
            t_ans.append((my_pos[0] + 1, my_pos[1] + 1))
        for el in t_ans:
            if 0 <= el[0] <= 7 and 0 <= el[1] <= 7:
                ans.append(el)
        return tuple(ans)

    def __str__(self):
        return f'{"♟" if self.colour=="white" else "♙"}'


class Rook(IFigure):
    def get_moves(self):
        my_pos = self.get_pos()
        board_cell_coordinates = [(i, j) for i in range(8) for j in range(8)]
        possible_moves = ([coordinates for coordinates in board_cell_coordinates if
                           my_pos[0] == coordinates[0] or my_pos[1] == coordinates[1]])

        return possible_moves

    def __str__(self):
        return f'{"♜" if self.colour=="white" else "♖"}'


class Knight(IFigure):
    def get_moves(self):
        my_pos = self.get_pos()
        possible_moves = []
        moves = [(my_pos[0] - 2, my_pos[1] - 1),
                 (my_pos[0] - 2, my_pos[1] + 1),
                 (my_pos[0] + 2, my_pos[1] - 1),
                 (my_pos[0] + 2, my_pos[1] + 1),
                 (my_pos[0] - 1, my_pos[1] - 2),
                 (my_pos[0] - 1, my_pos[1] + 2),
                 (my_pos[0] + 1, my_pos[1] - 2),
                 (my_pos[0] + 1, my_pos[1] + 2)]
        for move in moves:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                possible_moves.append(move)

        return possible_moves

    def __str__(self):
        return f'{"♞" if self.colour=="white" else "♘"}'


class Bishop(IFigure):

    def get_moves(self):
        my_pos = self.get_pos()
        board_cell_coordinates = [(i, j) for i in range(8) for j in range(8)]
        possible_moves = ([coordinates for coordinates in board_cell_coordinates if
                           abs(my_pos[0] - coordinates[0]) == abs(my_pos[1] - coordinates[1])
                           and my_pos[0] != coordinates[0] and my_pos[1] != coordinates[1]])

        return possible_moves

    def __str__(self):
        return f'{"♝" if self.colour=="white" else "♗"}'


class Queen(IFigure):
    def get_moves(self):
        my_pos = self.get_pos()
        board_cell_coordinates = [(i, j) for i in range(8) for j in range(8)]
        possible_moves = ([coordinates for coordinates in board_cell_coordinates if
                           abs(my_pos[0] - coordinates[0]) == abs(my_pos[1] - coordinates[1])
                           or my_pos[0] == coordinates[0] or my_pos[1] == coordinates[1]])

        return possible_moves

    def __str__(self):
        return f'{"♛" if self.colour=="white" else "♕"}'


class King(IFigure):
    def get_moves(self):
        my_pos = self.get_pos()
        board_cell_coordinates = [(i, j) for i in range(8) for j in range(8)]
        possible_moves = ([coordinates for coordinates in board_cell_coordinates if
                           abs(my_pos[0] - coordinates[0]) <= 1 and abs(my_pos[1] - coordinates[1]) <= 1])

        return possible_moves

    def __str__(self):
        return f'{"♚" if self.colour=="white" else "♔"}'
