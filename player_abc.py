from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.player_id = None # linked to the playing order 0,1
        self.player_icon = None
        self.player_moves = set()
    
    @abstractmethod
    def set_player_id(self, ID):
        pass

    @abstractmethod
    def set_player_icon(self, icon: str):
        pass
    
    @abstractmethod
    def check_if_won(self):
        pass

    @abstractmethod
    def make_move(self):
        pass