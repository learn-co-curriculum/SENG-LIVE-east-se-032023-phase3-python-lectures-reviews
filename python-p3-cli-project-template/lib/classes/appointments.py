from . import CONN, CURSOR

class Appointments () :
    

    def __init__ ( self, doctor_id, patient_id, date, id = None ) :
        self.doctor_id =  doctor_id
        self.patient_id = patient_id
        self.date = date
        self.id = id

    @property
    def date ( self ) :
        return self._date
    
    @date.setter
    def date ( self, date ) :
        if type( date ) is str and 0 < len( date ) <= 10 :
            self._date = date
        else :
            raise Exception( 'Date must be a string and greater than 0 and less than 10 characters long.' )
        

    @classmethod
    def create_tale ( cls ) :
        CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    doctor_id INTEGER,
                    patient_id INTEGER,
                        FOREIGN KEY ( doctor_id ) REFERENCES doctors ( id ),
                        FOREIGN KEY ( patient_id ) REFERENCES patients ( id )
                )
            """
        )
        
    @classmethod
    def create ( cls, doctor_id, patient_id, date ) :
        new_apmt = Appointments( doctor_id, patient_id, date )
        if new_apmt :
            sql = f"""
                INSERT INTO appointments ( doctor_id, patient_id, date )
                VALUES ( { new_apmt.doctor_id }, { new_apmt.patient_id }, '{ new_apmt.date }' )
            """
            CURSOR.execute( sql )
            app_id = CURSOR.execute( 'SELECT last_insert_rowid() FROM appointments' ).fetchone()[0]
            new_app = CURSOR.execute( f'SELECT * FROM appointments WHERE id = { app_id }' ).fetchone()
            return new_app
        else :
            raise Exception( 'Could not create appointment. Check data and try again.' )
        

    @classmethod
    def all ( cls ) :
        sql = "SELECT * FROM appointments"
        
        apps = CURSOR.execute( sql ).fetchall()
        return apps

