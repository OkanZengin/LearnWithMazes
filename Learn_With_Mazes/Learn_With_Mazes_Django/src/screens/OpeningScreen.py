import time
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
OPENING_SCREEN_DURATION = 0.5
OPENING_SCREEN_IMAGE = "images/background.jpg"


class OpeningScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.opening_time = None

    def on_show(self):
        self.opening_time = time.monotonic()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      arcade.load_texture(OPENING_SCREEN_IMAGE))

    def on_update(self, delta_time):
        if time.monotonic() - self.opening_time >= OPENING_SCREEN_DURATION:
            from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.MainMenu import MainMenu
            main_menu = MainMenu()
            self.window.show_view(main_menu)
