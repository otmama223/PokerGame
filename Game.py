
import Deck
import Player

class Game:
    def __init__(self, nb_players = 2, player_names= ["Player 1", "Player 2"]):
        self.nb_players = nb_players
        self.players = [Player(name) for name in player_names]
        self.deck = Deck()
        self.deck.shuffle()
        self.pot = 0
        self.tableCards = []
    def start(self):
        for i in range(2):
            for player in self.players:
                player.hand = self.deck.deal_card()

    def asignBB(self):
        pass

    def asignSB(self):
        pass

    def preflop(self):
        pass

    def flop(self):
        pass

    def turn(self):
        pass

    def river(self):
        pass

    def showdown(self):
        pass