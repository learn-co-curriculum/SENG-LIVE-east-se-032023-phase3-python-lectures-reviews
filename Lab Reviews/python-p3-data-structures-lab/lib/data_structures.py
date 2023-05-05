import ipdb
import statistics

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):

    # using a for loop
    # names = []
    # for food in spicy_foods :
    #     names.append( food['name'] )
    # return names

    # using a map function and turning the return value into a list
    # return list( map( lambda food : food['name'], spicy_foods ) )
    
    # using a list comprehension
    return [ food['name'] for food in spicy_foods ]


def get_spiciest_foods(spicy_foods):
    # spiciest_foods = []
    # for food in spicy_foods :
    #     if food['heat_level'] > 5 :
    #         spiciest_foods.append( food )
    # return spiciest_foods

    return [ food for food in spicy_foods if food['heat_level'] > 5 ]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods :
        print( f"{ food['name'] } ({ food['cuisine'] }) | Heat Level: { '🌶' * food['heat_level'] }" )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods :
        if food['cuisine'] == cuisine :
            return food


def print_spiciest_foods(spicy_foods):
    # spiciest_foods = get_spiciest_foods( spicy_foods )
    # print_spicy_foods( spiciest_foods )

    print_spicy_foods( get_spiciest_foods( spicy_foods ) )


def get_average_heat_level(spicy_foods):
    # return mean( [ food['heat_level'] for food in spicy_foods ] )

    total_heat_level = 0
    for food in spicy_foods :
        total_heat_level += food['heat_level']
    return round( total_heat_level / len( spicy_foods ) )


def create_spicy_food(spicy_foods, spicy_food):
    # add_new_spicy_food = [ *spicy_foods ]
    # print( add_new_spicy_food )
    # add_new_spicy_food.append( spicy_food )
    # return add_new_spicy_food

    spicy_foods.append( spicy_food )
    return spicy_foods


# ipdb.set_trace()