class Pet () :

    all = []
    
    def __init__ ( self, name, breed ) :
        self.name = name
        self.breed = breed
        self.all.append( self )
    
    def owners ( self ) :
        my_owners = [ po.owner for po in Pet_Owners.all if po.pet == self ]
        return my_owners

from .owner import *
from .pet_owners import *