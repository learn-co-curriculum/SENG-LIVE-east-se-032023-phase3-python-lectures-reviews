# Data Structures Lab

## Learning Goals

- Practice using comprehensions and built-in methods for data structures in
Python.
- Execute and test Python code using the Python shell and `pytest`.

***

## Key Vocab

- **Sequence**: a data structure in which data is stored and accessed in a
specific order.
- **Index**: the location, represented by an integer, of an element in a
sequence.
- **Iterable**: able to be broken down into smaller parts of equal size that
can be processed in turn. You can loop through any iterable object.
- **Slice**: a group of neighboring elements in a sequence.
- **Mutable**: an object that can be changed.
- **Immutable**: an object that cannot be changed. (_Many immutable objects
appear mutable because programmers reuse their names for new objects_.)
- **List**: a mutable data type in Python that can store many types of data.
The most common data structure in Python.
- **Tuple**: an immutable data type in Python that can store many types of
data.
- **Range**: a data type in Python that stores integers in a fixed pattern.
- **String**: an immutable data type in Python that stores unicode characters
in a fixed pattern. Iterable and indexed, just like other sequences.

***

## Instructions

Time to get some practice! Write your code in the `data_structures.py` file in
the `lib/` folder. Run `pytest -x` to check your work. Your goal is to practice
manipulating sequences with the Python tools you've learned about in this
lesson and the lessons before.

In `data_structures.py`, there is a list of dictionaries representing
different spicy foods.

```py
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
```

Practice using loops and Python list comprehensions alongside `list` and `dict`
methods to solve these deliverables.

### `get_names()`

Define a function `get_names()` that takes a list of `spicy_foods` and
**returns a list of strings** with the names of each spicy food.

```py
get_names(spicy_foods)
# => ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
```

### `get_spiciest_foods()`

Define a function `get_spiciest_foods()` that takes a list of `spicy_foods` and
**returns a list of dictionaries** where the heat level of the food is greater
than 5.

```py
get_spiciest_foods(spicy_foods)
# => [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]
```

### `print_spicy_foods()`

Define a function `print_spicy_foods()` that takes a list of `spicy_foods` and
**output to the terminal** each spicy food in the following format using
`print()`: `Buffalo Wings (American) | Heat Level: 🌶🌶🌶`.

HINT: you can use [times (\*) with a string][string times] to produce the
correct number of "🌶" emojis.

For example:

```py
"hello" * 3 == "hellohellohello"
# => True
```

```py
print_spicy_foods(spicy_foods)
# => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# => Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
```

[string times]: https://linuxhint.com/how-do-you-repeat-a-string-n-times-in-python/#:~:text=In%20Python%2C%20we%20utilize%20the,n%20(number)%20of%20times.

### `get_spicy_food_by_cuisine()`

Define a function `get_spicy_food_by_cuisine()` that takes a list of
`spicy_foods` and a string representing a `cuisine`, and **returns a single
dictionary** for the spicy food whose cuisine matches the cuisine being passed
to the method.

```py
get_spicy_food_by_cuisine(spicy_foods, "American")
# => {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}

get_spicy_food_by_cuisine(spicy_foods, "Thai")
# => {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}
```

### `print_spiciest_foods()`

Define a function `print_spiciest_foods()` that takes a list of `spicy_foods`
and **outputs to the terminal** ONLY the spicy foods that have a heat level
greater than 5, in the following format:

`Buffalo Wings (American) | Heat Level: 🌶🌶🌶`.

Try to use functions you've already written to solve this!

```py
print_spiciest_foods(spicy_foods)
# => Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# => Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
```

### `get_average_heat_level()`

Define a function `average_heat_level()` that takes a list of `spicy_foods` and
**returns an integer** representing the average heat level of all the spicy
foods in the array. Recall that to derive the average of a collection, you need
to calculate the total and divide number of elements in the collection.

```py
average_heat_level(spicy_foods)
# => 6
```

### `create_spicy_food()`

Define a function `create_spicy_food()` that takes a list of `spicy_foods` and a
new `spicy_food` and returns the original list with the new `spicy_food` added.

Example:

```py
create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
)

# => [
# =>     {
# =>         "name": "Green Curry",
# =>         "cuisine": "Thai",
# =>         "heat_level": 9,
# =>     },
# =>     {
# =>         "name": "Buffalo Wings",
# =>         "cuisine": "American",
# =>         "heat_level": 3,
# =>     },
# =>     {
# =>         "name": "Mapo Tofu",
# =>         "cuisine": "Sichuan",
# =>         "heat_level": 6,
# =>     },
# =>     {
# =>         'name': 'Griot',
# =>         'cuisine': 'Haitian',
# =>         'heat_level': 10,
# =>     },
# => ]

```

When all of your tests are passing, submit your work using `git`.

***

## Resources

- [Python List/Array Methods - W3Schools](https://www.w3schools.com/python/python_ref_list.asp)
- [Python Dictionary Methods - W3Schools](https://www.w3schools.com/python/python_ref_dictionary.asp)
- [When to Use a List Comprehension in Python - Real Python](https://realpython.com/list-comprehension-python/)
