import arcade
from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.PlayLevelsButtons import PlayLevelsButtons
from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.PlayLevelsOnDraw import on_draw

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BACKGROUND_IMAGE = "images/background.jpg"


class PlayLevels(arcade.View):

    def on_draw(self):
        on_draw()

    def on_mouse_press(self, x, y, button, modifiers):
        PlayLevelsButtons.on_mouse_press(self, x, y, button, modifiers)


