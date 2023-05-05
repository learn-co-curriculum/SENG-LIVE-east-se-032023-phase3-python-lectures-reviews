

# 1. ✅ Demonstrate First Class Functions
    # Create functions to be used as callbacks 
some_function = lambda : print( "I'm a anon function saved to a variable!" )


    # Create a higher-order function that will take a callback as an argument
def takes_function_and_runs_it ( a_function ) :
    a_function()


# 2. ✅ Create a higher-order function that returns a function
def has_an_inner_function () :
    def inner_function () :
        return "I'm an inner function!"
    return inner_function
    


# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
def outer_function ( a_function ) :
    def inner_function ( ) :
        print( "Hey, I'm an inner function!" )
        a_function()
    return inner_function


# Demo examples of the decorator with and without pie syntax '@'

    # Without pie syntax 
outer_function( some_function )()

run_functions = outer_function( some_function )
run_functions()


    # With pie syntax
@outer_function
def another_function () :
    print( "See, I happen automatically cause I get passed into outer_function using a decorator" )
    # this is what the decorator is doing => outer_function( another_function )()
