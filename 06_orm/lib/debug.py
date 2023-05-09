#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# sql = """
#     DROP TABLE IF EXISTS pets
#     DROP TABLE IF EXISTS owner
# """

# CURSOR.execute(sql)

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

# Pet.create_table()
Pet.create("spot", "dog", "chihuahua", "feisty" )
Pet.create( 'Fido', 'dog', 'corgi', 'relaxed' )
# spot.save()

import ipdb; ipdb.set_trace()
