
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append( self )

    @property
    def visitor ( self ) :
        return self._visitor
    
    @visitor.setter
    def visitor ( self, visitor ) :
        if type( visitor ) is Visitor :
            self._visitor = visitor
        else :
            raise Exception( 'Visitor must be an instance of the Visitor class.' )
        
    @property
    def national_park ( self ) :
        return self._national_park
    
    @national_park.setter
    def national_park ( self, np ) :
        if type( np ) is NationalPark :
            self._national_park = np
        else :
            raise Exception( 'Park must be an instance of the National Park class.' )


from .visitor import Visitor
from .national_park import NationalPark
