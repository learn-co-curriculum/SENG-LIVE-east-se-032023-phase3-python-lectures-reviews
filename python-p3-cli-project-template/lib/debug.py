from classes.appointments import Appointments
from classes.doctors import Doctors
from classes.patients import Patients

from faker import Faker

faker = Faker()

Patients.create_table()
Doctors.create_table()
Appointments.create_tale()

for n in range( 0, 5 ) :
    Patients.create( faker.first_name(), faker.last_name(), '06/01/1909' )

for n in range( 0, 5 ) :
    Doctors.create( faker.first_name(), faker.last_name(), faker.email() )


Appointments.create( 1, 1, '07/24/2023' )
Appointments.create( 1, 2, '07/12/2023' )
Appointments.create( 1, 5, '07/12/2023' )
Appointments.create( 2, 2, '07/13/2023' )
Appointments.create( 3, 5, '07/02/2023' )

import ipdb; ipdb.set_trace()