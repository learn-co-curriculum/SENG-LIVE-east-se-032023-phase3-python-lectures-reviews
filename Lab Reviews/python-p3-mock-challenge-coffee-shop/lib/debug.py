#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    cu1 = Customer( 'Princeton' )
    cu2 = Customer( 'Sarah' )
    cu3 = Customer( 'Nicholas' )
    cu4 = Customer( 'Melissa' )

    cf1 = Coffee( 'Latte' )
    cf2 = Coffee( 'Americano' )
    cf3 = Coffee( 'Mocha' )
    cf4 = Coffee( 'Cappucino' )
    cf5 = Coffee( 'Expresso' )

    o1 = Order( cu1, cf1, 5 )
    o2 = Order( cu3, cf5, 2 )
    o3 = Order( cu2, cf3, 6 )
    o4 = Order( cu4, cf1, 5 )
    o5 = Order( cu1, cf1, 5 )
    o6 = Order( cu1, cf1, 6 )
    o7 = Order( cu1, cf4, 7 )


    ipdb.set_trace()
