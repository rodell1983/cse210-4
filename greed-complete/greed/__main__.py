import random

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

from game.casting.gem import Gem
from game.casting.rock import Rock

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ROCKS = 200
DEFAULT_GEMS = 200


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the robot
    x = int(420)
    y = int(585)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    robot.set_group("robots")
    cast.add_actor("robots", robot)

    def generate_ranges(main_class, default_amount, text, group):
        """Generating a given number of instances from a given class"""
        for _ in range(default_amount):

            x = random.randint(1, COLS - 1)
            y = random.randint(1, 6)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            actor = main_class()
            actor.set_text(text)
            actor.set_font_size(FONT_SIZE)
            actor.set_color(color)
            actor.set_position(position)
            actor.set_group(group)
            cast.add_actor(actor.get_group(), actor)

    # start the game
    generate_ranges(Gem, DEFAULT_GEMS, '*', 'gems')
    generate_ranges(Rock, DEFAULT_ROCKS, 'o', 'rocks')
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE, True)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()