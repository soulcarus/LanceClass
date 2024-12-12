from abc import ABC, abstractmethod

class Provider(ABC):

    @abstractmethod
    def connect_to_provider(self):
        pass

    @abstractmethod
    def classify_chess_move(self):
        pass

    @abstractmethod
    def classify_chess_game(self):
        pass

class AbstractProvider:

    def __init__(self, provider: Provider):
        self.provider = provider

    def connect(self):
        return self.provider.connect_to_provider()
    
    def classify_move(self):
        return self.provider.classify_chess_move()
    
    def classify_game(self):
        return self.provider.classify_chess_game()
