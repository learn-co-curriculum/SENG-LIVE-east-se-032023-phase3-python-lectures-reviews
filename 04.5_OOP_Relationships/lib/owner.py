class Owner ( ) :

    all = []

    def __init__ ( self, first_name, last_name ) :
        self.first_name = first_name
        self.last_name = last_name
        self.all.append( self )

    def pets ( self ) :
        my_pets = [ po.pet for po in Pet_Owners.all if po.owner == self ]
        return my_pets


from .pet import *
from .pet_owners import *