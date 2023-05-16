from . import CONN, CURSOR

class Patients () :
    

    def __init__ ( self, first_name, last_name, dob, id = None ) :
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.id = id

    @property
    def first_name ( self ) :
        return self._first_name
    
    @first_name.setter
    def first_name ( self, name ) :
        if type( name ) is str and len( name ) > 0 :
            self._first_name = name
        else :
            raise Exception( 'First name must be a string and greater than 0 characters.' )
        
    @property
    def last_name ( self ) :
        return self._last_name
    
    @last_name.setter
    def last_name ( self, name ) :
        if type( name ) is str and len( name ) > 0 :
            self._last_name = name
        else :
            raise Exception( 'Last name must be a string and greater than 0 characters.' )
        
    @property
    def dob ( self ) :
        return self._dob
    
    @dob.setter
    def dob ( self, date ) :
        if type( date ) is str and 0 < len( date ) <= 10 :
            self._dob = date
        else :
            raise Exception( 'Date of Birth must be a string and greater than 0 and less than 10 characters long.' )
        
    @classmethod
    def create_table ( cls ) :
        CURSOR.execute( """
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                dob TEXT
            )
        """
        )
        print( "Table creation attempted. Please check your console to verify." )

    @classmethod    
    def create ( cls, first_name, last_name, dob ) :
        patient = Patients( first_name, last_name, dob )
        CURSOR.execute(f"""
                INSERT INTO patients ( first_name, last_name, dob )
                VALUES ( '{ patient.first_name }', '{ patient.last_name }', '{ patient.dob }' )
            """
        )
        new_patient_id = CURSOR.execute( 'SELECT last_insert_rowid() FROM patients' ).fetchone()[0]
        return cls.find_by_id( new_patient_id )


    @classmethod
    def find_by_id ( cls, id ) :
        if type( id ) is int and id > 0 :
            sql = f"SELECT * FROM patients WHERE id = { id }"
            new_patient = CURSOR.execute( sql ).fetchone()
            if new_patient :
                return cls.db_into_instance( new_patient )
            else :
                raise Exception( 'Could not find Patient with that ID.' )
        else :
            raise Exception( 'ID entered must be a integer greater than 0.' )
        
    @classmethod
    def find_by_name ( cls, name ) :
        if type( name ) is str and len( name ) > 0 :
            sql = f"SELECT * FROM patients WHERE first_name LIKE '{ name }' OR last_name LIKE '{ name }'"
            patients = CURSOR.execute( sql ).fetchall()
            if patients :
                return [ cls.db_into_instance( patient ) for patient in patients ]
            else :
                raise Exception( "Could not find any patients with that name." )
        else :
            raise Exception( 'Name must be a string and greater than 0 characters.' )
        

    @classmethod
    def all ( cls ) :
        sql = "SELECT * FROM patients"
        
        patients = CURSOR.execute( sql ).fetchall()
        return [ cls.db_into_instance( patient ) for patient in patients ]
        
    
    @classmethod
    def db_into_instance ( cls, patient ) :
        return Patients( patient[1], patient[2], patient[3], patient[0] )
    

    def doctors ( self ) :
        sql = f"""
            SELECT doctors.last_name from doctors
            JOIN appointments
            ON appointments.doctor_id = doctors.id
            JOIN patients
            ON appointments.patient_id = patients.id
            WHERE patients.id = { self.id }
        """
        my_doctors = CURSOR.execute( sql ).fetchall()
        return my_doctors
    
    def make_appointment ( self, doctor, date ) :
        if type( doctor ) is Doctors:
            new_app = Appointments.create( doctor.id, self.id, date )
            return new_app


from .appointments import Appointments
from .doctors import Doctors