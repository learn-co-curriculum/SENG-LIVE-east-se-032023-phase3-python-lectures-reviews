#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet class 
from lib.pet import *
from lib.cat import *
from lib.decorator import *

# Instances of the pet classes
fido = Pet('Fido', 3, 'Husky', 'Drama')
spot = Pet(name='Spot', breed='Pitbull', temperament='Sweet', age=1.5)
# rose = Pet('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)
# cookie = Pet('cookie', 1, 'Dachshund', 'hyper', 'cookie.jpg')
princess_grace = Cat('princess grace', 7, 'domestic longhair', 'affectionate', 'gracy.png')



import ipdb; ipdb.set_trace()