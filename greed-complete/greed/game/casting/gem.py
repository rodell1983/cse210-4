from game.casting.actor import Actor


class Gem(Actor):
    """
    A precious stone of great worth.
    
    The responsibility of a Gem is to increase the players score in the game.
    
    Attributes:
        _value (int): Points earned upon collection.
    """

    def __init__(self):
        super().__init__()
        self._value = 5

    def get_value(self):
        """Gets the gem's point value.
        
        Returns:
            integer: The point value.
        """
        return self._value

    def set_value(self, value):
        """updates the value to the given one.
        
        Args:
            value (int): The given points.
        """
        self._value = value