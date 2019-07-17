#17-A-1. Animal and Dog

class Animal:
    def __init__(self):
        print("Animal created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
    def whoAmI(self):
        print("Dog")
    def bark(self):
        print("Woof!")
d = Dog()
d.whoAmI()
d.eat()
d.bark()

#17-A-2.Circle
class Circle():
    pi = 3.141592
    def __init__(self):
        self.radius = 0
    def area(self):
        return self.pi * (self.radius ** 2)
    def setRadius(self, r):
        self.radius = r
    def getRadius(self):
        return self.radius
c = Circle()
c.setRadius(5)
print(c.getRadius())
print(c.area())

#17-A-3. Shape and Others
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self, text):
        self.description = text
    def authorName(self, text):
        self.author = text
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

#17-A-3-1
rectangle = Shape(100,45)
print(rectangle.area()) #4500
print(rectangle.perimeter()) #290
rectangle.describe("A wide rectangle, more than twice\
    as wide as it is tall")
rectangle.scaleSize(0.5)
print(rectangle.area()) #1125.0

#17-A-3-2
class Square(Shape):
    ''

class DoubleSquare(Shape):
    def area(self):
        return 2 * self.x * self.y
    def perimeter(self):
        return 4 * self.x + 2 * self.y

#17-A-3-3
class InsideDoubleSquare(Square):
    def area(self):
        return 0.25 * self.x * self.y
    def perimeter(self):
        return self.x + self.y

#17-B-1. Functions[1/7]
def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('jesse')

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#17-B-2. Functions[2/7]
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#17-B-3. Functions[3/7]
def build_person(first_name, last_name, age=''):
    person={'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#17-B-4
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nFollowing models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#17-B-5
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#17-B-6. Functions[6/7]
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

#17-B-7. Functinos[7/7]
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#17-B-8. Class Code[1/7]
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

#17-B-9. Class Code[2/7]
class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

#17-B. Class Code[3/7]

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


#17-B. Class Code[4/7]
from car import Car

class Battery():
    def __init__(self, battery_size=60):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size = 85:
            range = 185
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


#17-B. Class Code[6/7]
from car import Car
my_new_car = Car('audi', 'a4', 2015)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

from car import Car
from electric_car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2015)
print(my_tesla.get_descriptive_name())


#17-B. Class Code[7/7]
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
