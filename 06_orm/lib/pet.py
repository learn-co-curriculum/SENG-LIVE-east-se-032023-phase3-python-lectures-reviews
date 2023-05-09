# Stretch Goal: Include Association with Owner

# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# Stretch Goal
# owner_id: INTEGER

import sqlite3

CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()


class Pet:
    

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__ ( self, name, species, breed, temperament, id=None ) :
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    def print_db_items ( pet ) :
        print( f"Id: { pet[0] }, Name: { pet[1] }, Species: { pet[2] }, Temperament: { pet[3] }, Breed: { pet[4] }" )

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table ( cls ) :
        sql = """
            CREATE TABLE IF NOT EXISTS pets(
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                temperament TEXT,
                breed TEXT
            );
        """
        CURSOR.execute( sql )

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table ( cls ) :
        sql = "drop table if exists pets"
        CURSOR.execute( sql )

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save ( self ) :
        sql = f"""
            insert into pets ( name, breed, species, temperament ) values ( ?, ?, ?, ? )
        """
        CURSOR.execute( sql, ( self.name, self.breed, self.species, self.temperament ) )

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create ( cls, name, species, breed, temperament ) :
        new_pet = Pet( name, species, breed, temperament )
        new_pet.save()
        cls.new_from_db()

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def new_from_db ( cls ) :
        pet = CURSOR.execute('SELECT * FROM pets ORDER BY ID DESC LIMIT 1').fetchone()
        cls.print_db_items( pet )
        # for pet in pets:
        #     cls.print_db_items( pet )


    # ✅ 7. Add "all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def all ( cls ) :
        pets = CURSOR.execute( 'select * from pets' ).fetchall()
        for pet in pets :
            cls.print_db_items( pet )
        return pets

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
    @classmethod
    def find_by_name ( cls, name ) :
        sql = f"select * from pets where name like '{ name }'"
        pets = CURSOR.execute( sql ).fetchall()
        if pets :
            return pets
        # If No "pet" Found, return "None"
        else : return "None"
    

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB
    @classmethod
    def find_by_id ( cls, id ) :
        sql = f"select * from pets where id = { id }"
        pets = CURSOR.execute( sql ).fetchall()
        if pets :
            return pets
        # If No "pet" Found, return "None"
        else : 
            return "None"


    # ✅ 10. Add "find_or_create_by" Class Method to:
    @classmethod
    def find_or_create_by ( cls, name, species, breed, temperament ) :
        
        #  Find and Retrieve "pet" Instance w/ All Attributes
        sql = "select * from pets where name = '{}' and species = '{}' and breed = '{}' and temperament = '{}'".format( name, species, breed, temperament )
        pets = CURSOR.execute( sql ).fetchall()

        if pets :
            return "Pet already exists. Can't create new pet."
        # If No "pet" Found, Create New "pet" Instance w/ All Attributes
        else :
            cls.create( name, species, breed, temperament )

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes
    @classmethod
    def update ( cls, id, name, species, breed, temperament ) :
        pet = cls.find_by_id( id )
        if type( pet ) is not str :
            sql = f"update pets set name = '{ name }', species = '{ species }', breed = '{ breed }', temperament = '{ temperament }' where id = { id }"
            CURSOR.execute( sql )
            pet = cls.find_by_id( id )
            return pet
        else : return "Can't find pet with id {}".format( id )

