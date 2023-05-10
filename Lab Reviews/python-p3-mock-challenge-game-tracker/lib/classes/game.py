class Game:

    all = []

    def __init__(self, title):
        self._title = None
        if type( title ) is str and len( title ) > 0 :
            self._title = title
        else :
            raise Exception( 'Title must be a string and greater than 0 characters' )
        self.all.append( self )
        
    def results(self, new_result=None):
        return [ result for result in Result.all if result.game is self ]
    
    def players(self, new_player=None):
        if type( new_player ) is Player :
            Result( new_player, self, 1 )
        return [ result.player for result in self.results() ]
    
    def average_score(self, player):
        player_results = player.results()
        my_scores = [ result.score for result in player_results if result.game is self ]
        return mean( my_scores )

    def get_title ( self ) :
        return self._title
    
    def set_title ( self, title ) :
        print( "Game title can't be changed." )

    title = property( get_title, set_title )

from .result import Result
from .player import Player
from statistics import mean