class Result:

    all = []

    def __init__(self, player, game, score):
        self._player = None
        self._game = None
        self._score = None
        self.set_game( game )
        self.set_player( player )
        self.set_score( score )
        self.all.append( self )

    def get_score ( self ) :
        return self._score
    
    def set_score ( self, score ) :
        if type( score ) is int and 1 <= score <= 5000 :
            self._score = score
        else : 
            raise Exception( 'Score must be an integer between 1 and 5000.' )
        
    def get_game ( self ) :
        return self._game
    
    def set_game ( self, game ) :
        if type( game ) is Game :
            self._game = game
        else : raise Exception( 'Game must be a Game instance' )

    def get_player ( self ) :
        return self._player
    
    def set_player ( self, player ) :
        if type( player ) is Player :
            self._player = player
        else : raise Exception( 'Player must be a Player instance' )

    score = property( get_score, set_score )
    game = property( get_game, set_game )
    player = property( get_player, set_player )

from .game import *
from .player import *
