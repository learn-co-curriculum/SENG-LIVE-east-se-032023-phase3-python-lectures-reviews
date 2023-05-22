
# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker
faker = Faker()

from models import (Base, Pet)

if __name__ == '__main__':
    #3.1 ✅ Uncomment bellow to create the engine
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)

    #3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    #3.3 ✅  -- Creating records
        # Create a pet and save it to the data base with session.add and session.commit
    def create_pet ( ) :
        pet = Pet(
            name = faker.first_name(),
            breed = faker.city(),
            species = faker.city_prefix(),
            temperament = faker.last_name(),
            owner_id = faker.random_number()
        )

        #session.add(rose)
        session.add( pet )
        session.commit()
        

        # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
    def create_pets ( ) :
        pet = Pet(
            name = faker.first_name(),
            breed = faker.city(),
            species = faker.city_prefix(),
            temperament = faker.last_name(),
            owner_id = faker.random_number()
        )

        pet2 = Pet(
            name = faker.first_name(),
            breed = faker.city(),
            species = faker.city_prefix(),
            temperament = faker.last_name(),
            owner_id = faker.random_number()
        )

        pet3 = Pet(
            name = faker.first_name(),
            breed = faker.city(),
            species = faker.city_prefix(),
            temperament = faker.last_name(),
            owner_id = faker.random_number()
        )
        #Note: bulk save will not contain the id

        session.bulk_save_objects( [ pet, pet2, pet3 ] )
        session.commit()

        #verify by checking the db 
    #3.4 ✅ Read
        # Get all with session.query
    def all_pets ( ) :
        return session.query( Pet )
    
        # Print the pets 
    def print_pets ( ) :
        [ print( pet ) for pet in all_pets() ]

        #Get all of the pet names and print them with session.query
    def print_pet_names ( ) :
        [ print( name ) for name in session.query( Pet.name ) ]
   
        #Get all the pet names and print them in order with session.query and order_by
    def print_sorted_names ( ) :
        [ print( name ) for name in session.query( Pet.name ).order_by( Pet.owner_id ) ]

        #Get the first pet with session.query and first
    session.query( Pet ).first()


        #Filter pet by temperament with session.query and filter
    pet_with_joyce = session.query( Pet ).filter( Pet.temperament.like( 'joyce' ) )[0]

    #     SELECT pets.id AS pets_id, pets.name AS pets_name, pets.species AS pets_species, pets.breed AS pets_breed, pets.temperament AS pets_temperament, pets.owner_id AS pets_owner_id 
    # FROM pets 
    # WHERE pets.temperament LIKE ?


    #3.5 ✅ Update 
        # Update the pets name and print the updated pet info
  
        # Update all the pets temperament to 'cool' and print the pets 
    session.query( Pet ).filter( Pet.temperament.like( 'joyce' ) ).update({ Pet.owner_id: 100 })

    #3.6 ✅  Delete
        # Delete one item by querying the first pet, deleting it and committing it
    first_pet = session.query( Pet ).first()
    session.delete( first_pet )
    session.commit()

        #delete all the pets with session.query and .delete
    
  

    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()