# Functions [1/7]

example_print_flag = True

def greet_user(username):
    """Display a simple greeting"""
    print( 'Hello, ' + username.title() + '!' )

def describe_pet( pet_name, animal_type = 'dog' ):
    """Display information about a pet."""
    print( '\nI have a ' + animal_type + '.' )
    print( 'My ' + animal_type + "'s name is " + pet_name.title() + '.' )

if example_print_flag:
    print( '\n#Function[1/7]' )
    greet_user( 'jesse' )
    describe_pet( 'willie' )
    describe_pet( pet_name = 'willie' )
    describe_pet( 'harry', 'hamster' )
    describe_pet( pet_name = 'harry', animal_type = 'hamster' )
    describe_pet( animal_type = 'hamster', pet_name = 'harry' )

# Functions [2/7]

def get_formatted_name( first_name, last_name, middle_name = '' ):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

if example_print_flag:
    print( '\n#Function[2/7]' )
    musician = get_formatted_name( 'jimi', 'hendrix' )
    print(musician)
    musician = get_formatted_name( 'john', 'hooker', 'lee' )
    print(musician)

# Functions [3/7]

def build_person( first_name, last_name, age = '' ):
    """Return a dictionary of information about a person."""
    person = { 'first':first_name, 'last':last_name }
    if age:
        person['age'] = age
    return person

def greet_users( names ):
    """ Print a simple greeting to each user in the list."""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

if example_print_flag:
    print( '\nFunction [3/7]' )
    musician = build_person( 'jimi', 'hendrix', age = 27 )
    print( musician )
    usernames = [ 'hannah', 'ty', 'margot' ]
    greet_users( usernames )

# Function [4/7]

def print_models( unprinted_designs, completed_models ):
    """
    Simulate printng each design, until there ar none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print( 'Printing model: ' + current_design )
        completed_models.append( current_design )

def show_completed_models( completed_models ):
        """Show all the models that were printed."""
        print( '\nThe following models have beddn printed: ')
        for completed_model in completed_models:
            print(completed_model)

if example_print_flag:
    print( '\nFunction [4/7]' )    
    unprinted_designs = [ 'iphone case', 'robot pendant', 'dodecahedron' ]
    completed_models = []
    print_models( unprinted_designs, completed_models)
    show_completed_models( completed_models)

# Function [5/7]

def make_pizza( size, *toppings ):
    """Summarize the pizza we are about to make."""
    print( '\nMaking a ' + str(size) + '-inch pizza with the following toppings:' )
    for topping in toppings:
        print( '- ' + topping)

if example_print_flag:
    print( '\nFunction [5/7]' )
    make_pizza( 16, 'pepperoni' )
    make_pizza( 12, 'mushrooms', 'green peppers', 'extra cheese' )

# Function [6/7]

def build_profile( first, last, **user_info ):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile[ 'first_name' ] = first
    profile[ 'last_name' ] = last
    for key, value in user_info.items():
        profile[ key ] = value
    return profile

if example_print_flag:
    print( '\nFunction [6/7]' )
    user_profile = build_profile( 'albert', 'einstein', location = 'princeton', field = 'physics' )
    print( user_profile )

# Function [7/7]

# make pizza.py in same folder
# def make_pizza( size, *toppings ):
#    """Summarize the pizza we are about to make."""
#    print( '\nMaking a ' + str( size ) + '-inch pizza with the following toppings:' )
#    for topping in toppings:
#           print( '- ' + topping )

if example_print_flag:
           print( '\nFunction [7/7]' )
           import pizza as p
           p.make_pizza( 16, 'pepperoni' )
           p.make_pizza( 12, 'mushrooms', 'green peppers', 'extra cheese' )















    
    

