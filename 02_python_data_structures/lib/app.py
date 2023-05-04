import ipdb

# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name 
pet_names[0]

#3. ✅ Return all pet names beginning from the 3rd index
pet_names[3:]

#4. ✅ Return all pet names before the 3rd index
pet_names[:3]

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
pet_names[3:7]

# 5.5 ✅ Return last index
pet_names[-1]
pet_names[-2]

#6. ✅ Find the index of a given element
pet_names.index(  'Luke' )

#7. ✅ Reverse the original list
pet_names.reverse()

#8. ✅ Return the frequency of a given element 
numbers = [11,1,3,1,1,1,2,4,9]
numbers.count( 1 )


# Updating Lists
#9. ✅ Change the first element to all uppercase 
pet_names[0].upper()
pet_names[0].lower()
print( 'hello world'.title() )


#10. ✅ Append a new name to the list
numbers.append( 10 )


#11. ✅ Add a new name at a specific index
pet_names.insert( 3, 'Fido' )


#12. ✅ Add two lists together 
[1,2] + [3,4] + [5,6]

#13. ✅ Remove the final element from the list
numbers.pop()

#14. ✅ Remove element by specific index
del numbers[2]
numbers.pop( 5 )

#15. ✅ Remove a specific element 
pet_names.remove( 'Fido' )

#16. ✅ Remove all pet names from the list
pet_names.clear()
pet_names = []



#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable

#17. ✅ Create a Tuple of pet 10 ages 
pet_ages = ( 2, 3, 2, 10, 15 )

#18. ✅ Print the first pet age
pet_ages[0]
pet_ages[-1]
pet_ages[2:]


# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop()
# del pet_ages[2:]


#20. ✅ Attempt to change the first element (should error)
# pet_ages[1] = 4

# Tuple Methods
#21. ✅ Return the frequency of a given element
pet_ages.count( 2 )

#22. ✅ Return the index of a given element 
pet_ages.index( 2 )

#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops
range_of_numbers = range( 0, 10 )

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
numbers = [11,1,3,1,1,1,2,4,9]
numbers_set = set( numbers )


# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'rose','age':11,'breed':'domestic long '}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name='Spot', age=25, breed='boxer')


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
pet_info_rose['name']


#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
pet_info_rose.get( 'name' )
# pet_info_rose['birthday'] will cause a KeyError
pet_info_rose.get( 'birthday' )


# Updating 
#29. ✅ Update the pets age to 12
pet_info_rose['age'] = 12
pet_info_rose['birthday'] = '07/21/2012'


#30. ✅ Update the other pets age to 26


# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
del pet_info_rose['birthday']

#31. ✅ Delete the other pets age using ".pop"
pet_info_rose['birthday'] = '07/21/2012'
pet_info_rose.pop( 'birthday' )

#32. ✅ Delete the last item in the pet dictionary using "popitem()"
pet_info_rose['birthday'] = '07/21/2012'
pet_info_rose.popitem()


# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#33. ✅ Loop through a range of 10 and print every number within the range
for number in range( 1, 10 ) :
    print( number )

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
for number in range( 50, 60, 2 ) :
    print( number )


#35. ✅ Loop through the "pet_info" list and print every dictionary 
for pet in pet_info :
    print( pet )

#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
def print_items ( item_list ) :
    for item in item_list :
        print( item )


#37. ✅ Show off a while loop
    # Talk about why while loops are dangerous
countdown = 0
while countdown < 10 :
    print( countdown )
    countdown += 1

# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

def upper_case_strings ( string ) :
    return string.upper()

[ upper_case_strings( name ) for name in pet_names  ]

# find like
#40. ✅ Use list comprehension to find a pet named spot
[ name for name in pet_names if name == 'Spot' ]


# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
[ pet for pet in pet_info if pet['age'] > 10 ]


#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 

ipdb.set_trace()