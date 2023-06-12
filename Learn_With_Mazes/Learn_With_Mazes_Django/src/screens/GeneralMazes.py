import arcade

from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.GeneralMazesButtons import on_mouse_press
from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.GeneralMazesOnDraw import on_draw

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50


class GeneralMazes(arcade.View):

    def on_draw(self):
        on_draw()

    def on_mouse_press(self, x, y, button, modifiers):
        on_mouse_press(self, x, y, button, modifiers)


