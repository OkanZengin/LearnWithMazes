from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.MyProfileButtons import on_mouse_press
from ..assets.MenuAssets import *
from ..functions.MyProfileOnDraw import on_draw


class MyProfile(arcade.View):

    def on_draw(self):
        on_draw()

    def on_mouse_press(self, x, y, button, modifiers):
        on_mouse_press(self, x, y, button, modifiers)
