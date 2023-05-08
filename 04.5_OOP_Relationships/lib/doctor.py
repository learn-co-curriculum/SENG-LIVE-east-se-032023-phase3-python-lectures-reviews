class Doctor () :

    all = []

    def __init__ ( self, name, field ) :
        self.name = name
        self.field = field
        self.all.append( self )

    def appointments ( self ) :
        return [ appointment for appointment in Appointment.all if appointment.doctor == self ]
    
    def patients ( self ) :
        my_patients = [ appointment.patient for appointment in Appointment.all if appointment.doctor == self ]
        my_patients = list( set( my_patients ) )
        return my_patients


from .appointment import *