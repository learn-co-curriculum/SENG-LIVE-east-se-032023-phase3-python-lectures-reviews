class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append( self )


    @property
    def name ( self ) :
        return self._name
    
    @name.setter
    def name ( self, name ) :
        if type( name ) is str and len( name ) in range( 1, 16 ) : 
            # 1 <= len( name ) <= 15
            self._name = name
        else :
            raise Exception( 'Name must be a string and between 1 and 15 characters long.' )
        
    def trips(self):
        return [ trip for trip in Trip.all if trip.visitor is self ]
    
    def national_parks(self):
        my_parks_visited = [ trip.national_park for trip in self.trips() ]
        uniq_parks_visited = set( my_parks_visited )
        return list( uniq_parks_visited )


from classes.national_park import NationalPark
from classes.trip import Trip