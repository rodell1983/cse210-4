from game.casting.actor import Actor

class Rock(Actor):
    """
    A worthless rock that causes damage to the player if struck by it.
    
    The responsibility of a Rock is to reduce the players score by the set amount upon contact.
    
    Attributes:
        _value (int): Points lost upon contact.
    """
    def __init__(self):
        """Constructs a new Rock."""
        super().__init__()
        self._value = -10

    def get_value(self):
        """Gets the rock's point value.
        
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
