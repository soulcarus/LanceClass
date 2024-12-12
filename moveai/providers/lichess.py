from moveai.provider import Provider

class LichessProvider(Provider):

    def connect_to_provider(self):
        return 'Conectado ao Lichess'
    
    def classify_chess_move(self):
        return f'previsão de movimento: {1}'
    
    def classify_chess_game(self):
        return f'previsão de sequencia de movimentos: {1, 2, 3, 4, 5}'