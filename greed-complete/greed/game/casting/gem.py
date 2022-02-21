from game.casting.actor import Actor


class Gem(Actor):

    def __init__(self):
        super().__init__()
        self._value = 5

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value