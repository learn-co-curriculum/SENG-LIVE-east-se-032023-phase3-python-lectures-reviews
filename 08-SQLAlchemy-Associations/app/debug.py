from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker

from models import (Base, Owner, Pet, Handler, Job)
import ipdb

if __name__ == '__main__':

    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    #3✅ One to Many

    #Getting an owners pets
    #Use session.query and first to grab the first owner
    print("grab the first owner:")
    firstOwner = session.query(Owner)[0]
    print(firstOwner)

    #use session.query and filter_by to get the owners pets from Pet
    print("get the owners pets from Pet:")
    owners_pets = session.query(Pet).filter_by(owner_id = firstOwner.id).all()

    #print out your owners pets
    print(owners_pets)

    #Getting a pets owner
    #Use session.query and first to grab the first pet
    first_pet = session.query(Pet).first()
    print("first pet:")
    print(first_pet)
    
    #Use session.query and filter_by to get the owner associated with this pet
    first_pets_owner = session.query(Owner).filter_by(id = first_pet.owner_id).first()
    print(first_pets_owner)

    print("heres my list of pets")
    print(first_pets_owner.pets)

    #4✅ Head back to models to build out a Many to Many 
#--------------------------------------------

#6.✅ Many to Many 
    #Use session.query and .first to get the first handler
    
    #Use session.query and the .filter_by to grab the jobs
    
    #Print the jobs
 
    #Use the handler_jobs to query pets for the associated pet to each job.

    #Optional breakpoint for debugging
    ipdb.set_trace()