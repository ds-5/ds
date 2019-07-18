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
def make_pizza( size, *toppings ):
    """Summarize the pizza we are about to make."""
    print( '\nMaking a ' + str( size ) + '-inch pizza with the following toppings:' )
    for topping in toppings:
           print( '- ' + topping )

if example_print_flag:
           print( '\nFunction [7/7]' )
           import pizza as p
           p.make_pizza( 16, 'pepperoni' )
           p.make_pizza( 12, 'mushrooms', 'green peppers', 'extra cheese' )

# Class Code [1/7]

class Dog():
    """A simple attempt to model a dog."""
    def __init__( self, name, age ):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit( self ):
        """Simulate a dog sitting in response to a command."""
        print( self.name.title() + ' is now sitting.' )
    def roll_over( self ):
        """Simulate rolling over in response to a command."""
        print( self.name.title() + ' rolled over!' )

if example_print_flag:
    print( '\nClass Code [1/7]' )    
    my_dog = Dog( 'willie', 6 )
    your_dog = Dog( 'lucy', 3 )
    print( "My dog's name is " + my_dog.name.title() + '.' )
    print( 'My dog is ' + str( my_dog.age ) + ' years old.' )
    my_dog.sit()

    print( "\nMy dog's name is " + your_dog.name.title() + '.' )
    print( 'My dog is ' + str( your_dog.age ) + ' years old.' )
    your_dog.sit()
    
# Class Code [2/7]

# make car.py file with below Car class in same folder.
"""A class that can be used to represent a car."""
class Car():
    """A simple attempt to represent a car."""
    def __init__( self, manufacturer, model, year ):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name( self ):
        """Return a neatly formatted descriptive name."""
        long_name = str( self.year ) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    def read_odometer( self ):
        """Print a statement showing the car's mileage."""
        print( "This car has " + str( self.odometer_reading ) + ' miles on it.' )
    def update_odometer( self, mileage ):
        """
        Set the odometor reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print( 'You can\' roll back an odometer' )
    def increment_odometer( self, miles ):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

 # Class Code [3/7]  

if example_print_flag:
    print( '\nClass Code [3/7]' )
    my_used_car = Car( 'subaru', 'outback', 2013 )
    print( my_used_car.get_descriptive_name() )
    my_used_car.update_odometer( 23500 )
    my_used_car.read_odometer()
    my_used_car.increment_odometer( 100 )
    my_used_car.read_odometer()

# Class Code [4/7]

"""A set of classes that can be used to represent electric cars."""

from car import Car
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__( self, battery_size = 60 ):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery( self ):
        """Print a statement describing the battery size."""
        print( 'This car has a ' + str( self.battery_size ) + '-kWh battery.' )
    def get_range( self ):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
        message = 'This car can go approximately ' + str( range )
        message += ' miles on a full charge.'
        print( message )

# Make electric_car.py file with below ElectricCar class in same folder.
from car import Car
from battery import Battery

class ElectricCar( Car ):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__( self, manufacturer, model, year ):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__( manufacturer, model, year )
        self.battery = Battery()

# Class Code [5/7]

if example_print_flag:
    print( '\nClass Code [5/7]' )
    my_tesla = ElectricCar( 'tesla', 'model s', 2016 )
    print( my_tesla.get_descriptive_name() )
    my_tesla.battery.describe_battery()

# Class Code [6/7]

from car import Car
from electric_car import ElectricCar

if example_print_flag:
    print( '\nClass Code [6/7]' )
    my_new_car = Car( 'audi', 'a4', 2015 )
    print( my_new_car.get_descriptive_name() )
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    my_beetle = Car( 'volkswagen', 'beetle', 2015 )
    print( my_beetle.get_descriptive_name() )
    my_tesla = ElectricCar( 'tesla', 'roadster', 2015 )
    print( my_tesla.get_descriptive_name() )

# Class Code [7/7]

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages[ 'jen' ] = 'python'
favorite_languages[ 'sarah' ] = 'c'
favorite_languages[ 'edward' ] = 'ruby'
favorite_languages[ 'phil' ] = 'python'

if example_print_flag:
    print( '\nClass Code [7/7]' )
    for name, language in favorite_languages.items():
        print( name.title() + '\'s favorite language is ' + language.title() + '.' )
                    
    









    
    

