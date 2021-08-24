from Chess_interfaces import IHistory


class History(IHistory):

    def __init__(self):
        self.__game_history = dict()

    def get_game_history(self):
        return self.__game_history

    def add_record(self, history_list):
        self.get_game_history()[history_list[0]] = (history_list[1], history_list[2], history_list[3])

    def show_history(self):
        for k, v in self.get_game_history().items():
            print(f'move № {k} {v[1]} on {v[0]}...{v[2]}')

