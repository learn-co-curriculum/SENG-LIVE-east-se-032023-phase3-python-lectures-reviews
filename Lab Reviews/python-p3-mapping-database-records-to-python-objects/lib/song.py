import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:

    all = []

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS songs
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
    
    @classmethod
    def find_or_create_by ( cls, name, album ) :
        songs = CURSOR.execute( "select * from songs where album like '{}' and name like '{}'".format( album, name ) ).fetchall()
        if songs :
            raise Exception( "Data already exists in table." )
        else :
            song = Song(name, album)
            song.save()
            return song

    # new code goes here!
    @classmethod
    def new_from_db ( cls, row ) :
        song = cls( row[1], row[2] )
        song.id = row[0]
        return song
    
    @classmethod
    def get_all ( cls ) :
        songs = CURSOR.execute( 'select * from songs' ).fetchall()
        cls.all = [ cls.new_from_db( song ) for song in songs ]
        return [ song.__dict__ for song in cls.all ]
    
    @classmethod
    def find_by_name ( cls, name ) :
        songs = CURSOR.execute( "select * from songs where name like '{}'".format( name ) ).fetchall()
        if songs :
            return [ cls.new_from_db( song ).__dict__ for song in songs ]
        else : cls.could_not_find_songs()
    
    @classmethod
    def find_by_album ( cls, album ) :
        songs = CURSOR.execute( "select * from songs where album like '{}'".format( album ) ).fetchall()
        if songs :
            return [ cls.new_from_db( song ).__dict__ for song in songs ]
        else : cls.could_not_find_songs()

    @classmethod
    def could_not_find_songs ( cls ) :
        raise Exception( 'Could not find any songs that match that criteria. Sorry, try again.' )

    
    @classmethod
    def find_by_id ( cls, id ) :
        if not type( id ) == int :
            raise TypeError( 'Id must be a integer.' )
        song = CURSOR.execute( 'select * from songs where id = {}'.format( id ) ).fetchone()
        if song :
            song = cls.new_from_db( song )
            print( song.__dict__ )
            return song
        else : raise Exception( "Could not find song with that id." )

    
    @classmethod
    def delete ( cls, id ) :
        cls.find_by_id( id )
        CURSOR.execute( f'delete from songs where id = { id }' )

    @classmethod
    def update ( cls, id, name, album ) :
        song = cls.find_by_id( id )
        sql = f"update songs set name = '{ name }', album = '{ album }' where id = { id }"
        CURSOR.execute( sql )
        updated_song = cls.find_by_id( id )

    @classmethod
    def find_by_name_or_album ( cls, word ) :
        songs = CURSOR.execute( "select * from songs where album like '{}' or name like '{}'".format( word, word ) ).fetchall()
        if songs :
            return [ cls.new_from_db( song ).__dict__ for song in songs ]
        else : cls.could_not_find_songs()

