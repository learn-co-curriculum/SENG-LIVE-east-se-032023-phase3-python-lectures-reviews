class Coffee:

    all = []

    def __init__(self, name):
        if type( name ) is str :
            self._name = name
        else :
            raise Exception( "Name must be a string." )

        Coffee.all.append( self )
        
    def orders(self):
        return [ order for order in Order.all if order.coffee is self ]
    
    def customers(self):
        return list( set( [ order.customer for order in self.orders() ] ) )
    
    def num_orders(self):
        return len( self.orders() )
    
    def average_price(self):
        return mean( [ order.price for order in self.orders() ] )

    def get_name ( self ) :
        return self._name
    
    def set_name ( self, name=None ) :
        raise Exception( "Name can't be changed after creation." )

    name = property( get_name, set_name )


from classes.order import Order
from classes.customer import Customer
from statistics import mean