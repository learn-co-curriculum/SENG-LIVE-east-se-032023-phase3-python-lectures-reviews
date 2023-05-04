# { "Basket": "ball" } Lab

## Learning Goals

- Practice iterating over nested dictionaries

***

## Key Vocab

- **Interpreter**: a program that executes other programs. Python programs
require the Python interpreter to be installed on your computer so that they
can be run.
- **Python Shell**: an interactive interpreter that can be accessed from the
command line.
- **Data Type**: a specific kind of data. The Python interpreter uses these
types to determine which actions can be performed on different data items.
- **Exception**: a type of error that can be predicted and handled without
causing a program to crash.
- **Code Block**: a collection of code that is interpreted together. Python
groups code blocks by indentation level.
- **Function**: a named code block that performs a sequence of actions when it
is called.
- **Scope**: the area in your program where a specific variable can be called.

***

## Instructions

Welcome to {"Basket": "ball"}! In this lab, you will be implementing functions
to work with a nested data structure. There's a function `game_dict()` that has
been provided to you in this lab that will return a nested dictionary, which
you'll be working with as you write methods to solve the deliverables below.

We also strongly recommend that you read the **_entire_** README before you
start coding. We're going to show some tips and tricks that make the coding a
lot easier... but only if you read through to the end.

Code your solution in `basket_ball.py` following the steps below. Keep
`game_dict()` as is, using the other functions to access information.

This lab is the largest and most complex yet, so set aside some time for this
one. Remember all the tricks you learned from working with objects in JavaScript
— even though the syntax here is a bit different, the same problem solving
techniques are just as important.

***

## Some Tips for Completing this Lab

To get started, ensure you can read data out of the nested data structure with
simple, basic `[]` calls.

You can confirm this by starting the Python shell from this lesson's main
directory and importing the functions from `basket_ball.py`:

```console
>>> from lib.basket_ball import *
```

From here, you can interact with the `game_dict()` function. Calling
`game_dict()['home']['team_name']`, for example, should return `"Cleveland
Cavaliers"`. This is because `game_dict()` returns a dictionary — we can chain
`[]` calls on the dictionary it returns. As you're building your functions, use
the shell to help you figure out how to access the information inside the
dictionary returned by `game_dict()`. You can test the functions you're building
from the Python shell as well.

Write helper functions with descriptive names so it's easier to work with the
data. For example, you can create a function called `get_all_players()` that
gets the players of both the home and away teams.

Be flexible. Work from what you have to where you want to go. Or, work backward.
Or, make a midpoint between what you have and what you need to have.

## Building the Functions

Let's take a look at the specification for the first deliverable:

- Build a function, `num_points_per_game()` that takes in an argument of a player's
  name and returns the number of points per game for that player.

Some questions to consider:

- Where in the dictionary will you find a player's `points_per_game`? What are
  the steps you need to complete to iterate down to that level?
- How can you check and see if a player's name matches the name that has been
  passed into the method as an argument?
- What does the function's return value need to be?
- Is there a helper function you can write to break down the process into
  smaller chunks and avoid repetitive code?

You may want to start by having `num_points_per_game()` return the entire
`game_dict()` dictionary. You can then add code one step at a time, getting
closer to the needed information in each step, until you get it working.

As you complete this lab, try to follow this general process: find a failing
test, build a "skeleton function," iterate on the code, get success, and move
on. This is the way software is "grown" in the real world.

## Deliverables

### `num_points_per_game()`

Build a function, `num_points_per_game()` that takes in an argument of a
player's name and returns the number of points per game for that player.

### `player_age()`

Build a function, `player_age()`, that takes in an argument of a player's name
and returns that player's age.

### `team_colors()`

Build a function, `team_colors()`, that takes in an argument of the team name
and returns a `list` of that team's colors.

### `team_names()`

Build a function, `team_names()`, that operates on the dictionary to return a
`list` of the team names.

### `player_numbers()`

Build a function, `player_numbers()`, that takes in an argument of a team name
and returns a `list` of the jersey numbers for that team.

### `player_stats()`

Build a function, `player_stats()`, that takes in an argument of a player's name
and returns a dictionary of that player's stats.

- Check out the following example of the expected return value of the
  `player_stats()` function:

  ```py
  player_stats("Darius Garland")
  # => {
  #      "name": "Darius Garland",
  #      "number": 10,
  #      "position": "Point Guard",
  #      "points_per_game": 21.7,
  #      "rebounds_per_game": 3.3,
  #      "assists_per_game": 8.6,
  #      "steals_per_game": 1.3,
  #      "blocks_per_game": 0.1,
  #      "career_points": 3142,
  #      "age": 22,
  #      "height_inches": 73,
  #      "shoe_brand": "Nike",
  #    }
  ```

### CHALLENGE: `average_rebounds_by_shoe_brand()`

Build a function, `average_rebounds_by_shoe_brand()`, that will calculate the
average number of rebounds for players who wear a particular shoe brand. The
function should print out a message for each brand using the following format:

```console
"<Brand>": average_rebounds
```

The average should be printed as a float with two decimal places.

Building this function will offer several challenges. You'll want to break it
down into steps. Here is one possible approach:

First, create a dictionary that will keep track of the shoe brands along with a
list of the numbers of rebounds for all the players who wear that brand of shoe.
An entry in the dictionary may look something like this:

```py
{ "Nike": [5.0, 8.1, 4.7] }
```

**Hint**: As you iterate through the players in `game_dict()`, you will need to
check whether the player's shoe brand is already in the dictionary. If it isn't,
you will add the brand as a key, and a list containing the current player's
rebounds as the value. If it is already present, you will simply add the
rebounds to the array.

Next, iterate through the dictionary you've created to calculate the average
rebounds for each brand. The average is the sum of all the values divided by the
number of values. For example, using the example above, the average is:

```text
(5.0 + 8.1 + 4.7)/3 = 5.93
```

**Hint**: You may want to use Google to help you with this step.

Finally, print the results to the screen.

### Additional Practice

The ability to manipulate and access data from nested data structures is an
important skill. If you'd like some more practice, try writing functions to
return answers to the following questions:

1. Which player has the most career points?
2. Are there any jersey numbers that are worn by players on both teams?
3. Which player has the longest name?

Or come up with some ideas of your own!

***

## Conclusion

This is a new frontier for you! You are now using powerful tools of Python to
access data from a nested data structure to produce insights. You've made huge
strides in becoming a really solid developer in the procedural programming
paradigm. This is a huge moment. Celebrate it!

Believe it or not, the code that put rockets in space and humankind on the Moon
were only slight variations on this style of programming. You've learned
something really powerful!

***

## Resources

- [Python Docs: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [How to access nested data in Python](https://towardsdatascience.com/how-to-access-nested-data-in-python-d65efa53ade4)
