class NationalPark:

    all = []

    def __init__(self, name):
        if type( name ) is str :
            self._name = name
        else :
            raise Exception( 'Name must be a string.' )
        NationalPark.all.append( self )

    @property
    def name ( self ) :
        return self._name
    
    @name.setter
    def name ( self, name ) :
        print( 'Name cannot be changed. Sorry... =(' )


        
    def trips(self):
        return [ trip for trip in Trip.all if trip.national_park is self ]
    
    def visitors(self):
        my_visitors = [ trip.visitor for trip in self.trips() ]
        uniq_visitors = set( my_visitors )
        return list( uniq_visitors )
    
    def total_visits(self):
        return len( self.trips() )
    
    def best_visitor(self):
        my_visitors = [ trip.visitor.name for trip in self.trips() ]
        return max( set( my_visitors ), key = my_visitors.count )



from classes.trip import Trip
from classes.visitor import Visitor