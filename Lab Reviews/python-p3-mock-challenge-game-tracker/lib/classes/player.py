class Player:

    all = []

    def __init__(self, username):
        self._username = None
        self.set_username( username )
        self.all.append( self )
        
    def results(self, new_result=None):
        return [ result for result in Result.all if result.player is self ]
    
    def games_played(self, new_game=None):
        my_results = self.results()
        return [ result.game for result in my_results ]
        # return [ result.game for result in self.results() ]
    
    def played_game(self, game):
        return game in self.games_played()
    
    def num_times_played(self, game):
        return len( [ result for result in self.results() if result.game is game ] )
    
    @classmethod
    def highest_scored(cls, game):
        
        players_scores = [ {'player': player.username, 'avg score': game.average_score( player ) } for player in game.players() ]
        
        players_scores.sort( key = lambda player: player['avg score' ] )
        
        highest_score = players_scores[-1]['avg score']
        return highest_score
        
    def get_username ( self ) :
        return self._username
    
    def set_username ( self, username ) :
        if type( username ) is str and 2 <= len( username ) <= 16 :
            # len( username ) in range( 2, 17 )
            self._username = username
        else : raise Exception( 'Username must be a string between 2 and 16 characters long.' )


    username = property( get_username, set_username )
        
from .result import Result
from .game import Game
from statistics import mean