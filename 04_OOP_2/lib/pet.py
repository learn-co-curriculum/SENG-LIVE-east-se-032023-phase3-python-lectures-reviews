#!/usr/bin/env python3
# Class Attributes and Methods 

class Pet:

    # 1✅. Create a class variable to track all pet instances that have been created
    total_pets = 0


    def __init__(self, name, age, breed, temperament, image_url=''):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        Pet.increase_pets()
 
    
    # 2✅. Create a class method increase_pets that will increment total_pets
        # replace Pet.total_pets += 1 in __init__ with increase_pets()
    @classmethod
    def increase_pets ( cls ) :
        cls.total_pets += 1
        

    def print_self ( self ) :
        print( self )

    def print_pet_details( self ) :
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        ''')




