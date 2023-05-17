#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

np1 = NationalPark( 'Yellowstone' )
np2 = NationalPark( 'Grand Canyon' )
np3 = NationalPark( 'Stone Mountain' )
np4 = NationalPark( 'Kennesaw Mountain' )

v1 = Visitor( 'Princeton' )
v2 = Visitor( 'Selena' )
v3 = Visitor( 'Cole' )
v4 = Visitor( 'Gabby' )
v5 = Visitor( 'Warren' )
v6 = Visitor( 'Sarah' )

t7 = Trip( v5, np1, '02/15/2025', '02/18/2025' )
t1 = Trip( v1, np3, '07/23/2023', '07/23/2023' )
t2 = Trip( v2, np2, '08/23/2024', '09/14/2024' )
t3 = Trip( v1, np4, '10/01/2023', '10/03/2023' )
t4 = Trip( v4, np1, '05/19/2023', '05/23/2023' )
t5 = Trip( v5, np1, '11/15/2024', '11/18/2024' )
t6 = Trip( v1, np4, '10/10/2023', '10/11/2023' )

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    ipdb.set_trace()
