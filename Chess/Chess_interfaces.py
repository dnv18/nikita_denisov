from abc import ABC, abstractmethod


class IFigure(ABC):  # Абстрактный класс играющий роль интерфейса для фигур от него наследуются все фигуры

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __init__(self, pos,
                 color):  # При создании любой фигуры передаем ей в конструктор кортеж с координатами и цвет фигуры
        self.colour = color
        self.position = pos
        self.not_moved = True

    def get_pos(self):
        return self.position

    def set_pos(self, cor):  # cor - кортеж с координатами, если фигура уходит с доски - cor == None
        self.position = cor

    def get_colour(self):
        return self.colour


class IBoard(ABC):

    def __init__(self):
        self.content = [['🨄' for _ in range(8)] for _ in range(8)]
        self.__capturing_white_fig = []
        self.__capturing_black_fig = []

    def get_content(self):
        return self.content

    def get_capturing_white_fig(self):
        w_f = self.__capturing_white_fig
        return w_f

    def set_capturing_white_fig(self, figure):
        self.__capturing_white_fig.append(figure.__str__())

    def get_capturing_black_fig(self):
        b_f = self.__capturing_black_fig
        return b_f

    def set_capturing_black_fig(self, figure):
        self.__capturing_black_fig.append(figure.__str__())

    def update_fig_position(self, figure, coordinates, move_pos):  # Изменение положения фигур на доске
        self.get_content()[move_pos[0]][move_pos[1]] = figure
        self.get_content()[coordinates[0]][coordinates[1]] = '🨄'
        figure.set_pos(move_pos)  # задание новой координаты перемещенной фигуры

    def delete_fig(self, fig_pos):

        if self.get_content()[fig_pos[0]][fig_pos[1]].get_colour() == 'white':
            self.set_capturing_white_fig(self.get_content()[fig_pos[0]][fig_pos[1]])
        else:
            self.set_capturing_black_fig(self.get_content()[fig_pos[0]][fig_pos[1]])
        self.get_content()[fig_pos[0]][fig_pos[1]].set_pos = None
        self.get_content()[fig_pos[0]][fig_pos[1]] = '🨄'

    @staticmethod
    def transform_index_to_cor(pos):  # можно переделать, чтобы обрабатывался сразу список координат
        """Возвращает строку с координатами доски"""
        x = abs(int(pos[0]) - 8)
        y = chr(pos[1] + 65)
        return f'{y}{x}'

    @staticmethod
    def transform_cor_to_index(coordinate):
        """Возвращает кортеж с индексом коррдинаты доски в двумерном списке"""
        try:  # ввод координаты в формате A1
            x = abs(int(coordinate[1]) - 8)
            y = ord(coordinate[0].upper()) - 65
        except ValueError:  # ввод координаты в формате 1A
            x = abs(int(coordinate[0]) - 8)
            y = ord(coordinate[1].upper()) - 65
        if 0 <= x <= 7 and 0 <= y <= 7:  # на случай, если цифра и буква вне координат доски
            return x, y
        else:
            raise ValueError


class IManager(ABC):

    @abstractmethod
    def __init__(self):
        self.board = IBoard()
        self.history = IHistory()

    @abstractmethod
    def main_loop(self, move_counter=0):
        pass

    @abstractmethod
    def flow_splitter(self, figure, pos, move_pos):
        pass

    def show_board(self):
        print(' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', sep='\t\t')
        for i in range(8):
            print(abs(i - 8), end='\t\t')
            for j in range(8):
                print(self.board.get_content()[i][j], end='\t\t')
            print(abs(i - 8))
        print(' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', sep='\t\t')
        if self.board.get_capturing_black_fig():
            print(f'Captured black figures: {", ".join(self.board.get_capturing_black_fig())}')
        if self.board.get_capturing_white_fig():
            print(f'Captured white figures: {", ".join(self.board.get_capturing_white_fig())}')

    def possible_moves(self, figure):
        possible_moves = figure.get_moves()
        corrected_moves = [self.board.transform_index_to_cor(i) for i in self.filter_move(possible_moves, figure)]
        if figure.__str__() == "♚":
            if self.castling_long_side(figure) == 'wlt' and self.castling_short_side(figure) == 'wst':
                corrected_moves.append('C1')
                corrected_moves.append('G1')
            elif self.castling_long_side(figure) == 'wlt':
                corrected_moves.append('C1')
            elif self.castling_short_side(figure) == 'wst':
                corrected_moves.append('G1')
        elif figure.__str__() == "♔":
            if self.castling_long_side(figure) == 'blt' and self.castling_short_side(figure) == 'bst':
                corrected_moves.append('C8')
                corrected_moves.append('G8')
            elif self.castling_long_side(figure) == 'blt':
                corrected_moves.append('C8')
            elif self.castling_short_side(figure) == 'bst':
                corrected_moves.append('G8')
        return corrected_moves

    def castling_short_side(self, figure):
        # white
        if figure.__str__() == "♚":
            if figure.not_moved:  # не проверяется двигалась ли ладья
                if self.board.get_content()[6][0] == '🨄' and self.board.get_content()[5][0] == '🨄':
                        # and not self.cell_in_danger(self.board.get_content()[6][0],
                        #                             'white')
                        # and not self.cell_in_danger(self.board.get_content()[5][0],
                        #                             'white')):
                    return 'wst'

        # black
        elif figure.__str__() == "♔":
            if figure.not_moved:  # не проверяется двигалась ли ладья
                if self.board.get_content()[6][7] == '🨄' and self.board.get_content()[5][7] == '🨄':
                        # and not self.cell_in_danger(self.board.get_content()[6][7],
                        #                             'black')
                        # and not self.cell_in_danger(self.board.get_content()[5][7],
                        #                             'black')):
                    return 'bst'

    def castling_long_side(self, figure):
        # white
        if figure.__str__() == "♚":
            if figure.not_moved:  # не проверяется двигалась ли ладья
                if self.board.get_content()[2][0] == '🨄' and self.board.get_content()[3][0] == '🨄':
                        # and not self.cell_in_danger(self.board.get_content()[2][0],
                        #                             'white')
                        # and not self.cell_in_danger(self.board.get_content()[3][0],
                        #                             'white')):
                    return 'wlt'
        # black
        elif figure.__str__() == "♔":
            if figure.not_moved:  # не проверяется двигалась ли ладья
                if self.board.get_content()[2][7] == '🨄' and self.board.get_content()[3][7] == '🨄':
                        # and not self.cell_in_danger(self.board.get_content()[2][7],
                        #                             'black')
                        # and not self.cell_in_danger(self.board.get_content()[3][7],
                        #                             'black')):
                    return 'blt'

    def select_move(self, figure, moves):
        print(f'List of possible moves for {figure}:\n{moves}')
        move = input('Select move by coordinate: ')
        if move.upper() in moves:
            return move
        else:
            print('There is no such option\n')
            return self.select_move(figure, moves)

    def filter_occupied_cells(self, list_of_moves, figure):
        corrected_list = list(filter(lambda m: False if self.board.get_content()[m[0]][m[1]] != '🨄'
                                                        and figure.get_colour() == self.board.get_content()[m[0]][
                                                            m[1]].get_colour() else True, list_of_moves))
        return corrected_list

    def filter_move(self, list_of_moves, figure):

        if figure.__str__() == '♝' or figure.__str__() == "♗":
            corrected_list = self.bishop_filter(list_of_moves, figure)

        elif figure.__str__() == '♜' or figure.__str__() == "♖":
            corrected_list = self.rook_filter(list_of_moves, figure)

        elif figure.__str__() == '♚' or figure.__str__() == "♔":
            corrected_list = self.king_filter(list_of_moves, figure)

        elif figure.__str__() == '♛' or figure.__str__() == "♕":
            corrected_list = []
            for move in list_of_moves:
                if move[0] == figure.get_pos()[0] or move[1] == figure.get_pos()[1]:
                    corrected_list += self.rook_filter([move], figure)
                else:
                    corrected_list += self.bishop_filter([move], figure)
        elif figure.__str__() == '♟' or figure.__str__() == "♙":
            corrected_list = self.pawn_filter(list_of_moves, figure)
        else:
            corrected_list = self.filter_occupied_cells(list_of_moves, figure)

        corrected_list = sorted(list(set(corrected_list)))
        if figure.get_pos() in corrected_list:
            corrected_list.remove(figure.get_pos())
        return corrected_list

    def rook_filter(self, list_of_moves, figure):
        f_y = y_max = y_min = figure.get_pos()[0]
        f_x = x_max = x_min = figure.get_pos()[1]
        while y_max < 7:
            y_max += 1
            if self.board.get_content()[y_max][f_x] != '🨄':
                if figure.get_colour() == self.board.get_content()[y_max][f_x].get_colour():
                    y_max -= 1
                    break
                else:
                    break

        while y_min > 0:
            y_min -= 1
            if self.board.get_content()[y_min][f_x] != '🨄':
                if figure.get_colour() == self.board.get_content()[y_min][f_x].get_colour():
                    y_min += 1
                    break
                else:
                    break

        while x_min > 0:
            x_min -= 1
            if self.board.get_content()[f_y][x_min] != '🨄':
                if figure.get_colour() == self.board.get_content()[f_y][x_min].get_colour():
                    x_min += 1
                    break
                else:
                    break
        while x_max < 7:
            x_max += 1
            if self.board.get_content()[f_y][x_max] != '🨄':
                if figure.get_colour() == self.board.get_content()[f_y][x_max].get_colour():
                    x_max -= 1
                    break
                else:
                    break

        corrected_list = list(filter(lambda m: True if y_min <= m[0] <= y_max and x_min <= m[1] <= x_max
        else False, list_of_moves))
        return corrected_list

    def bishop_filter(self, list_of_moves, figure):
        y_max = y_min = figure.get_pos()[0]
        x_max = x_min = figure.get_pos()[1]
        while y_max < 7 and x_max < 7:
            y_max += 1
            x_max += 1
            if self.board.get_content()[y_max][x_max] != '🨄':
                if figure.get_colour() == self.board.get_content()[y_max][x_max].get_colour():
                    y_max -= 1
                    x_max -= 1
                    break
                else:
                    break
        new_list = list(filter(lambda m: False if m[0] > y_max and m[1] > x_max else True, list_of_moves))
        while y_min > 0 and x_min > 0:
            y_min -= 1
            x_min -= 1
            if self.board.get_content()[y_min][x_min] != '🨄':
                if figure.get_colour() == self.board.get_content()[y_min][x_min].get_colour():
                    y_min += 1
                    x_min += 1
                    break
                else:
                    break
        new_list1 = list(filter(lambda m: False if m[0] < y_min and m[1] < x_min else True, new_list))
        y_max = y_min = figure.get_pos()[0]
        x_max = x_min = figure.get_pos()[1]
        while y_max < 7 and x_min > 0:
            y_max += 1
            x_min -= 1
            if self.board.get_content()[y_max][x_min] != '🨄':
                if figure.get_colour() == self.board.get_content()[y_max][x_min].get_colour():
                    y_max -= 1
                    x_min += 1
                    break
                else:
                    break
        new_list2 = list(filter(lambda m: False if m[0] > y_max and m[1] < x_min else True, new_list1))
        while y_min > 0 and x_max < 7:
            y_min -= 1
            x_max += 1
            if self.board.get_content()[y_min][x_max] != '🨄':
                if figure.get_colour() == self.board.get_content()[y_min][x_max].get_colour():
                    y_min += 1
                    x_max -= 1
                    break
                else:
                    break
        corrected_list = list(filter(lambda m: False if m[0] < y_min and m[1] > x_max else True, new_list2))

        return corrected_list

    def pawn_filter(self, list_of_moves, figure):
        corrected_list = []
        for move in list_of_moves:
            if move[1] != figure.get_pos()[1]:
                if self.board.get_content()[move[0]][move[1]] != '🨄' and figure.get_colour() != \
                        self.board.get_content()[move[0]][move[1]].get_colour():
                    corrected_list.append(move)
            else:
                if abs(move[0] - figure.get_pos()[0]) == 1 and self.board.get_content()[move[0]][move[1]] == '🨄':
                    corrected_list.append(move)
                else:
                    if figure.get_colour() == 'white':
                        if self.board.get_content()[figure.get_pos()[0] - 1][figure.get_pos()[1]] == '🨄' \
                                and self.board.get_content()[move[0]][move[1]] == '🨄':
                            corrected_list.append(move)
                    else:
                        if self.board.get_content()[figure.get_pos()[0] + 1][figure.get_pos()[1]] == '🨄' \
                                and self.board.get_content()[move[0]][move[1]] == '🨄':
                            corrected_list.append(move)

        return corrected_list

    def king_filter(self, list_of_moves, figure):
        corrected_list = []
        for move in list_of_moves:
            if not self.cell_in_danger(move, figure.get_colour()):
                corrected_list.append(move)

        return self.filter_occupied_cells(corrected_list, figure)

    def additional_options(self):
        chose = input('Press "1" to continue\nPress "2" to show the History\nPress "3" to exit:')
        if chose == '1':
            pass
        elif chose == '2':
            self.history.show_history()
        elif chose == '3':
            exit()
        else:
            print('Try again')
            self.additional_options()

    def cell_in_danger(self, indexes, colour):
        for i in range(len(self.board.get_content())):
            for j in range(len(self.board.get_content()[i])):
                if (self.board.get_content()[i][j] != '🨄'
                        and self.board.get_content()[i][j].__str__() not in '♚♔'
                        and self.board.get_content()[i][j].get_colour() != colour
                        and self.board.transform_index_to_cor(indexes) in self.possible_moves(
                            self.board.get_content()[i][j])):
                    return True
                elif self.board.get_content()[i][j].__str__() in '♚♔' \
                        and self.board.get_content()[i][j].get_colour() != colour:
                    list_of_moves = self.board.get_content()[i][j].get_moves()
                    figure = self.board.get_content()[i][j]
                    if indexes in self.filter_occupied_cells(list_of_moves, figure):
                        return True
        return False

    @staticmethod
    def check_the_colour(figure, player_color):
        return True if figure != '🨄' and figure.get_colour() == player_color else False


class IHistory(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_game_history(self):
        pass

    @abstractmethod
    def add_record(self, history_list):
        pass

    @abstractmethod
    def show_history(self):
        pass
