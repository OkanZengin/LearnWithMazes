import arcade

from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.MazesiPlayedRatedButtons import on_mouse_press
from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.MazesiPlayedRatedOnDraw import on_draw

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BACKGROUND_IMAGE = "images/background.jpg"


class MazesIPlayed(arcade.View):

    def on_draw(self):
        on_draw()

    def on_mouse_press(self, x, y, button, modifiers):
        on_mouse_press(self, x, y, button, modifiers)


