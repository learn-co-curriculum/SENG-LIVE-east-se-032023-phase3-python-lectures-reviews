from . import CONN, CURSOR

class Doctors () :
    

    def __init__ ( self, first_name, last_name, medical_field, id = None ) :
        self.first_name = first_name
        self.last_name = last_name
        self.medical_field = medical_field
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
    def medical_field ( self ) :
        return self._medical_field
    
    @medical_field.setter
    def medical_field( self, field ) :
        if type( field ) is str and len( field ) > 0 :
            self._medical_field = field
        else :
            raise Exception( 'Medical field must be a string and greater than 0 characters.' )
        
    @classmethod
    def create_table ( cls ) :
        CURSOR.execute( """
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                medical_field TEXT
            )
        """
        )
        print( "Table creation attempted. Please check your console to verify." )

    @classmethod    
    def create ( cls, first_name, last_name, medical_field ) :
        doctor = Doctors( first_name, last_name, medical_field )
        CURSOR.execute(f"""
                INSERT INTO doctors ( first_name, last_name, medical_field )
                VALUES ( '{ doctor.first_name }', '{ doctor.last_name }', '{ doctor.medical_field }' )
            """
        )
        new_doctor_id = CURSOR.execute( 'SELECT last_insert_rowid() FROM doctors' ).fetchone()[0]
        return cls.find_by_id( new_doctor_id )
    

    @classmethod
    def all ( cls ) :
        sql = "SELECT * FROM doctors"
        
        doctors = CURSOR.execute( sql ).fetchall()
        return [ cls.db_into_instance( doctor ) for doctor in doctors ]
        
    
    @classmethod
    def db_into_instance ( cls, doctor ) :
        return Doctors( doctor[1], doctor[2], doctor[3], doctor[0] )
    
    @classmethod
    def find_by_id ( cls, id ) :
        if type( id ) is int and id > 0 :
            sql = f"SELECT * FROM doctors WHERE id = { id }"
            new_doctor = CURSOR.execute( sql ).fetchone()
            if new_doctor :
                return cls.db_into_instance( new_doctor )
            else :
                raise Exception( 'Could not find Doctor with that ID.' )
        else :
            raise Exception( 'ID entered must be a integer greater than 0.' )
        
    def patients ( self ) :
        sql = f"""
            SELECT patients.first_name, patients.last_name from patients
            JOIN appointments
            ON appointments.patient_id = patients.id
            JOIN doctors
            ON appointments.doctor_id = doctors.id
            WHERE doctors.id = { self.id }
        """
        my_patients = CURSOR.execute( sql ).fetchall()
        return my_patients