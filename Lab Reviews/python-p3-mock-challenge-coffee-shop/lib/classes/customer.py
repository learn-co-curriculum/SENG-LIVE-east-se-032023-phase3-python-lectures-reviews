class Customer:

    all = []

    def __init__(self, name):
        self._name = None
        self.set_name( name )

        Customer.all.append( self )
        
    def orders(self):
        return [ order for order in Order.all if order.customer is self ]
    
    def coffees(self):
        ordered_coffees = [ order.coffee for order in self.orders() ]
        unique_coffees = set( ordered_coffees )
        return list( unique_coffees )
    
    def create_order ( self, coffee, price ) :
        Order( self, coffee, price )

    def get_name ( self ) :
        return self._name
    
    def set_name ( self, name ) :
        if type( name ) is str and len( name ) in range( 1, 16 ) :
            self._name = name
        else : 
            raise Exception( "Name must be a string between 1 and 15 characters long." )

    name = property( get_name, set_name )

from classes.order import Order
from classes.coffee import Coffee