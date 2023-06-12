import arcade
from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.MyProfile import MyProfile
from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.CreateMaze import CreateMaze
from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.GeneralMazes import GeneralMazes
from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.MazesIPlayed import MazesIPlayed
from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.PlayLevels import PlayLevels
from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.SigninSignup import SignInSignUp

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100


class MainMenuButtons:
    def __init__(self, x, y, image_path, on_button_press, window):
        self.x = x - (BUTTON_WIDTH / 2)
        self.y = y - (BUTTON_HEIGHT / 2)
        self.sprite = arcade.Sprite(image_path, scale=0.15, center_x=(self.x + (BUTTON_WIDTH / 2)),
                                    center_y=(self.y + (BUTTON_HEIGHT / 2)))

        self.on_button_press = on_button_press
        self.window = window

    def draw(self):
        self.sprite.draw()

    def check_hover(self, x, y):
        return (
                self.x <= x <= self.x + BUTTON_WIDTH
                and self.y <= y <= self.y + BUTTON_HEIGHT
        )

    def on_press(self):
        self.on_button_press(self.window)

    @staticmethod
    def on_create_maze_button_press(window):
        from ..assets.SharedData import SharedData
        if SharedData.signed_in_flag:
            create_maze = CreateMaze()
            window.show_view(create_maze)
        else:
            sign_in_sign_up = SignInSignUp()
            sign_in_sign_up.run()

    @staticmethod
    def on_general_mazes_button_press(window):
        from ..assets.SharedData import SharedData
        if SharedData.signed_in_flag:
            general_mazes = GeneralMazes()
            window.show_view(general_mazes)
        else:
            sign_in_sign_up = SignInSignUp()
            sign_in_sign_up.run()

    @staticmethod
    def on_mazes_i_played_button_press(window):
        from ..assets.SharedData import SharedData
        if SharedData.signed_in_flag:
            mazes_i_played = MazesIPlayed()
            window.show_view(mazes_i_played)
        else:
            sign_in_sign_up = SignInSignUp()
            sign_in_sign_up.run()

    @staticmethod
    def on_my_profile_button_press(window):
        from ..assets.SharedData import SharedData
        if SharedData.signed_in_flag:
            my_profile = MyProfile()
            window.show_view(my_profile)
        else:
            sign_in_sign_up = SignInSignUp()
            sign_in_sign_up.run()

    @staticmethod
    def on_play_levels_button_press(window):
        from ..assets.SharedData import SharedData
        if SharedData.signed_in_flag:
            from ..database.IsPlayed import is_played
            is_played()
            play_levels = PlayLevels()
            window.show_view(play_levels)
        else:
            sign_in_sign_up = SignInSignUp()
            sign_in_sign_up.run()
