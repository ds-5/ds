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
