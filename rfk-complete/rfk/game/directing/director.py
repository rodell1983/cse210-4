import pyray
import random

from game.shared.point import Point

# from game.shared.color import Color

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 100


    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)
        actors = cast.get_all_actors()
        for actor in actors:
            if actor.get_group() == "gems" or actor.get_group() == "rocks":
                actors_velocity = Point(0, 1)
                actor.set_velocity(actors_velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        all_actors = cast.get_all_actors()

        banner.set_text(str(self._score))
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)


        for actor in all_actors:
            if actor.get_group() == "gems" or actor.get_group() == "rocks":
                actor.move_next(max_x, max_y)
                if robot.get_position().equals(actor.get_position()):
                    cast.remove_actor(actor.get_group(), actor)
                    self._score += actor.get_value()


    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        # print(actors)
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    #     for i in range(self.list_size):
    #         pyray.draw_text('*', self.gem_list[i][0], self.gem_list[i][1], 30, (255, 255, 255))
    #         self.gem_list[i][1] += 4
    #         if self.gem_list[i][1] > 600:
    #             y = random.randrange(-50, -10)
    #             self.gem_list[i][1] = y
    #             x = random.randrange(0, 900)
    #             self.gem_list[i][0] = x

    #     for i in range(self.list_size):
    #         pyray.draw_text('o', self.rock_list[i][0], self.rock_list[i][1], 30, (255, 255, 255))
    #         self.rock_list[i][1] += 4
    #         if self.rock_list[i][1] > 600:
    #             y = random.randrange(-50, -10)
    #             self.rock_list[i][1] = y
    #             x = random.randrange(0, 900)
    #             self.rock_list[i][0] = x

    # def populate_lists(self):
    #     for i in range(self.list_size):
    #         rock_x = random.randrange(0, 900)
    #         rock_y = random.randrange(-600, 50)
    #         snow_x = random.randrange(0, 900)
    #         snow_y = random.randrange(-600, 50)
    #         self.rock_list.append([rock_x, rock_y])
    #         self.gem_list.append([snow_x, snow_y])