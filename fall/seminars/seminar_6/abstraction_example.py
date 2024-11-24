from abc import ABC, abstractmethod


# пример для игры tic-tac-toe
class Player(ABC):
    @abstractmethod
    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def make_move(self, board):
        move = int(input("Введите номер клетки: "))
        return move

class AIPlayer(Player):
    # def make_move(self, board):
    #     return 0
    pass

ai_player = AIPlayer()


