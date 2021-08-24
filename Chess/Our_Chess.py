from Chess_pieces import *
from Chess_interfaces import *
from History import *


class GameManager(IManager):

    def __init__(self, board=0):  # для того, что бы можно было перейти в игровой режим из песочницы
        self.history = History()
        self.board = GameBoard()
        if board != 0:
            self.board.set_content(board)

    def main_loop(self, move_counter=0, history_list=[]):
        while None not in self.board.get_king_pos() and len(self.board.get_king_pos()) == 2:
            player_color = 'white' if move_counter % 2 == 0 else 'black'
            history_list.append(move_counter+1)
            if move_counter != 0:
                self.additional_options()
            try:
                pos = input(f'{player_color.capitalize()} chess is playing\nChoose a piece by coordinate: ')
                history_list.append(pos)
                pos = self.board.transform_cor_to_index(pos)
            except ValueError:
                print('You entered incorrect coordinates, please try again\n')
                self.main_loop(move_counter, history_list=[])
            figure = self.board.get_content()[pos[0]][pos[1]]
            if GameManager.check_the_colour(figure, player_color):
                moves = self.possible_moves(figure)
                if not moves:
                    print(f'Choose another piece, please try again\n')
                    self.main_loop(move_counter, history_list=[])
                move_pos = self.select_move(figure, moves)
                self.flow_splitter(figure, pos, move_pos)
                self.show_board()
                history_list.append(figure)
                history_list.append(move_pos)
                self.history.add_record(history_list)
                if figure.not_moved:
                    figure.not_moved = False
                self.main_loop(move_counter + 1, history_list=[])
            else:
                print(f'You have chosen the wrong piece ({figure}), please try again\n')
                self.main_loop(move_counter, history_list=[])
        if move_counter > 0:
            print(f'The game ended in: {move_counter} moves\nWinner: {"white" if move_counter % 2 != 0 else "black"}')
            exit()
        else:
            print('\nNow this board is not ready to play :(\n')

    def flow_splitter(self, figure, pos, move_pos):
        if figure.__str__() == "♚" and move_pos == 'C1' or move_pos == 'G1':
            if move_pos == 'C1':
                figure2_pos = self.board.transform_cor_to_index('A1')
                figure2_move_pos = 'D1'
                figure2 = self.board.get_content()[figure2_pos[0]][figure2_pos[1]]
                self.board.update_fig_position(figure, pos, self.board.transform_cor_to_index(move_pos))
                self.board.update_fig_position(figure2, figure2_pos,
                                               self.board.transform_cor_to_index(figure2_move_pos))
            elif move_pos == 'G1':
                figure2_pos = self.board.transform_cor_to_index('H1')
                figure2_move_pos = 'F1'
                figure2 = self.board.get_content()[figure2_pos[0]][figure2_pos[1]]
                self.board.update_fig_position(figure, pos, self.board.transform_cor_to_index(move_pos))
                self.board.update_fig_position(figure2, figure2_pos,
                                               self.board.transform_cor_to_index(figure2_move_pos))
        elif figure.__str__() == "♔" and move_pos == 'C8' or move_pos == 'G8':
            if move_pos == 'C8':
                figure2_pos = self.board.transform_cor_to_index('A8')
                figure2_move_pos = 'D8'
                figure2 = self.board.get_content()[figure2_pos[0]][figure2_pos[1]]
                self.board.update_fig_position(figure, pos, self.board.transform_cor_to_index(move_pos))
                self.board.update_fig_position(figure2, figure2_pos,
                                               self.board.transform_cor_to_index(figure2_move_pos))
            elif move_pos == 'G8':
                figure2_pos = self.board.transform_cor_to_index('H8')
                figure2_move_pos = 'F8'
                figure2 = self.board.get_content()[figure2_pos[0]][figure2_pos[1]]
                self.board.update_fig_position(figure, pos, self.board.transform_cor_to_index(move_pos))
                self.board.update_fig_position(figure2, figure2_pos,
                                               self.board.transform_cor_to_index(figure2_move_pos))
        else:
            move_pos = self.board.transform_cor_to_index(move_pos)
            if self.board.get_content()[move_pos[0]][move_pos[1]] == '🨄':
                self.board.update_fig_position(figure, pos, move_pos)
            else:
                self.board.delete_fig(move_pos)
                self.board.update_fig_position(figure, pos, move_pos)


class GameBoard(IBoard):
    """Реализация через вложенные списки. Каждый элемент вложенного списка - объект или строка если там нет фигуры"""

    def __init__(self):
        super().__init__()
        t = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)            # список с названиями классов фигур
        self.content[0] = [t[col]((0, col), 'black') for col in range(8)]        # в список попадает генератор,в генератор попадает название класса фигуры и передается цвет и позиция, создаётся только список в виде первой стороки
        self.content[1] = [Pawn((1, col), 'black') for col in range(8)]          # добавляется в список генератор, который создает список  белых пешек
        self.content[6] = [Pawn((6, col), 'white') for col in range(8)]          # добавляется в список генератор, который создает список  черных пешек
        self.content[7] = [t[col]((7, col), 'white') for col in range(8)]  # добавляется в список генератор, который работает аналогично строчке 91
        self.__king_list = [self.content[0][4], self.content[7][3]]

    def set_content(self, content):
        self.content = content
        self.king_search()

    def set_king(self, king):
        if isinstance(king, list):
            self.__king_list = king
        else:
            self.__king_list.append(king)

    def king_search(self):
        self.set_king([])
        for i in self.content:
            for j in i:
                if isinstance(j, King):
                    self.set_king(j)

    def get_king_pos(self):
        try:
            kings = [self.__king_list[0].get_pos(), self.__king_list[1].get_pos()]
            return kings
        except:
            return []


if __name__ == '__main__':

    def choose_option():
        chose = input('Press "1" to start the game\nPress "2" to create the sandbox\nPress "3" to exit:\n')
        if chose == '1':
            GM = GameManager()
            GM.show_board()
            GM.main_loop()
        elif chose == '2':
            import SandBox
            SBM = SandBox.SandBox_Manager()
            SBM.main_loop()
        elif chose == '3':
            exit()
        else:
            print('Try again')
            choose_option()

    choose_option()
