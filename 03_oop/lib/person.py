from typing import Any
import ipdb

    # Demonstrate classes 
    # 1. ✅ Create a Person class
    # 2. ✅ Instantiate a few person instances 
        # Compare the person instances to demonstrate they are not the same object

class Person :
    

    # 3. ✅ Demonstrate __init__ 
        # Add arguments to instances  
        # use dot notation to access their attributes 
        # update attributes with new values 

    def __init__( self, first_name, last_name, ssn) :
        # Demonstrate the self keyword 
        self.first_name = first_name
        self.last_name = last_name
        self.__ssn = ssn


        
    # 4.✅ Demonstrate instance methods by creating a greeting function that will print a message
        #     Review the self keyword 
        #     Invoke the greeting on an instance 
    def greeting ( self ) :
        print( f"Hi there, I'm { self.first_name }! ^_^" )
        print( self )

    def print_full_name ( self ) :
        print( f"{ self.first_name } { self.last_name }" )


    # Demonstrate getters and setters
    def get_ssn ( self ) :
        return str( self.__ssn )[-4:]
    
    def set_ssn ( self, ssn ) :
        print( "You can't change that!" )

    def get_birthdate ( self ) :
        return self._birthdate
    
    def set_birthdate ( self, birthdate ) :
        self._birthdate = birthdate
    

    # Demonstrate object properties
    ssn = property( get_ssn, set_ssn )

    birthdate = property( get_birthdate, set_birthdate )
