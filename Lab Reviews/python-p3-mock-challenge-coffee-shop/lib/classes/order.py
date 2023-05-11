class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self._customer = None
        self.set_customer( customer )

        self._coffee = None
        self.set_coffee( coffee )
        
        self._price = None
        self.set_price( price )

        Order.all.append( self )


    def get_price ( self ) :
        return self._price
    
    def set_price ( self, price ) :
        if type( price ) is int and price in range( 1, 11 ) :
            self._price = price
        else :
            raise Exception( "Price must be a number between 1 and 10." )
        
    def get_customer ( self ) :
        return self._customer
    
    def set_customer ( self, customer ) :
        if type( customer ) is Customer :
            self._customer = customer
        else :
            raise Exception( "Customer must be an instance of the Customer class." )
        
    def get_coffee ( self ) :
        return self._coffee
    
    def set_coffee ( self, coffee ) :
        if type( coffee ) is Coffee :
            self._coffee = coffee
        else :
            raise Exception( "Coffee must be an instance of the Coffee class." )
        

    price = property( get_price, set_price )
    customer = property( get_customer, set_customer )
    coffee = property( get_coffee, set_coffee )

from .customer import Customer
from .coffee import Coffee

