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
