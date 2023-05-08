class Patient () :

    all = []

    def __init__( self, name ) :
        self.name = name
        self.all.append( self )

    def appointments ( self ) :
        return [ appointment for appointment in Appointment.all if appointment.patient == self ]
    
    def doctors ( self ) :
        return [ appointment.doctor for appointment in Appointment.all if appointment.patient == self ]


from .appointment import *