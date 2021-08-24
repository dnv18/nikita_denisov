from Chess_interfaces import *
from Chess_pieces import *


class SandBox_GameBoard(IBoard):

    def __init__(self):
        super().__init__()
        self.king_list = []
        #  в списке прописан класс для создания фигуры, цвет фигуры и счетчик доступных для постановки на доску фигур
        self.set_of_pieces = {'1': {'1': [Pawn, 'white', 'Pawn', 8], '2': [Pawn, 'black', 'Pawn', 8]},
                              '2': {'1': [Rook, 'white', 'Rook', 2], '2': [Rook, 'black Rook', 2]},
                              '3': {'1': [Knight, 'white', 'Knight', 2], '2': [Knight, 'black', 'Knight', 2]},
                              '4': {'1': [Bishop, 'white', 'Bishop', 2], '2': [Bishop, 'black', 'Bishop', 2]},
                              '5': {'1': [Queen, 'white', 'Queen', 1], '2': [Queen, 'black', 'Queen', 1]},
                              '6': {'1': [King, 'white', 'King', 1], '2': [King, 'black', 'King', 1]}}

    def get_set_of_pieces(self):
        return self.set_of_pieces

    def set_set_of_pieces(self, new_set):
        self.set_of_pieces = new_set

    def show_available_set_of_pieces(self):  # отображает перед каждым ходом список доступных для выбора фиггур
        print()
        for key, value in self.set_of_pieces.items():
            for k, v in value.items():
                print(f'{key}{k} - {v[1].capitalize()} {v[2]} ({v[-1]} left)'.ljust(40), end=' ')
            print()

    def update_set_of_pieces(self, fig_pos):  # возвращает +1 к счетчику фигуры, если ее удаляют с доски
        colour = self.get_content()[fig_pos[0]][fig_pos[1]].get_colour()
        type_f = type(self.get_content()[fig_pos[0]][fig_pos[1]])
        for key, value in self.set_of_pieces.items():
            for k, v in value.items():
                if v[0] == type_f and colour == v[1]:
                    v[-1] += 1
                    break

    def set_fig_on_board(self, index, figure):  # ставим созданную фигурку на доску
        self.content[index[0]][index[1]] = figure

    def delete_fig(self, fig_pos):                                  # удаляем с доски ранее созданную фигурку
        fig_index = self.transform_cor_to_index(fig_pos)            # индекс фигуры, которую удаляем
        if self.get_content()[fig_index[0]][fig_index[1]] != '🨄':   # проверяем, есть ли п этому индексу вообще фигура
            self.update_set_of_pieces(fig_index)                    # исправляем счетчик вигуры (+1 к доступным фигурам)
            self.get_content()[fig_index[0]][fig_index[1]].set_pos = None
            #  ??? del self.get_content()[fig_pos[0]][fig_pos[1]]
            self.get_content()[fig_index[0]][fig_index[1]] = '🨄'
        else:
            print(f'There are no piece at coordinate {fig_pos}')

    def update_fig_position(self, figure, coordinates, move_pos=0):   # Изменение положения фигур на доске
        self.get_content()[coordinates[0]][coordinates[1]] = figure
        if move_pos != 0:
            self.get_content()[move_pos[0]][move_pos[1]] = '🨄'
            figure.set_pos(move_pos)


class SandBox_Manager(IManager):

    def __init__(self):
        self.board = SandBox_GameBoard()
        self.history = []

    def create_pieces(self, piece, pos):
        """
        :param piece: a user-entered value indicating the chess piece to be created
        :param pos: the coordinates of the chess piece before converted to index
        :return: returns the created chess piece or re-starts the main loop if no one is available
        """
        pos = self.board.transform_cor_to_index(pos)
        set_of_pieces = self.board.get_set_of_pieces()      # получаем словарь self.set_of_pieces из self.board
        x, y = piece[0], piece[1]                           # x - ключ для первого словаря, y - ключ для словаря, который лежит по ключу x
        # проверяем счетчик выбранной фигуры (т.е можно ли еще поставить такую фигуру на доску)) и свободно ли положение
        if self.check_piece_counter(x, y) and self.check_board(pos):
            params = set_of_pieces[x][y]                    # получаем список по ключам x и y, например [Pawn, 'white', 'Pawn', 8]
            piece = params[0](pos, params[1])               # создаем заданную фигуру
            set_of_pieces[x][y][-1] -= 1                    # отмечаем в словаре, что стало на одну меньше доступных фигур
            self.board.set_set_of_pieces(set_of_pieces)     # "загружаем" новое значение словаря с измененным счетчиком
            self.board.update_fig_position(piece, pos)
            return piece
        else:
            print('Problems, you have problems :(')
            self.main_loop()

    def flow_splitter(self, figure, pos, move_pos):
        ...

    def check_piece_counter(self, x, y):
        """
        :param x: dictionary key for self.set_of_pieces from self.board
        :param y: dictionary key for x in self.set_of_pieces from self.board
        :return: False no available peace or True if there is a chess piece available
        """
        return False if self.board.get_set_of_pieces()[x][y][-1] == 0 else True

    def check_board(self, pos):
        return False if self.board.get_content()[pos[0]][pos[1]] != '🨄' else True

    def main_loop(self, move_counter=0):
        while True:
            self.show_board()
            self.board.show_available_set_of_pieces()
            press = input('\nPress "1" to start the game\nPress "2" to delete piece\nPress "3" to exit\nOr set piece and position (numb pos):\n')
            if press == '1':
                import Our_Chess
                GM = Our_Chess.GameManager(self.board.get_content())
                GM.show_board()
                GM.main_loop()
            elif press == '2':
                coord = input('enter coord for delete')
                self.board.delete_fig(coord)
            elif press == '3':
                exit()
            else:
                try:
                    try:
                        figure, pos = press.split()
                        self.create_pieces(figure, pos)  # размещение фигуры на доске
                    except:
                        pos, figure = press.split()
                        self.create_pieces(figure, pos)  # размещение фигуры на доске
                except:
                    print('Something go wrong, try one more time:(')
                    self.main_loop()


if __name__ == '__main__':

    c = SandBox_Manager()
    c.main_loop()
