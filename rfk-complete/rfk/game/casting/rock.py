from game.casting.actor import Actor

class rock(Actor):
    def __init__(self):
        super().__init__()
        self._value = -10

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value