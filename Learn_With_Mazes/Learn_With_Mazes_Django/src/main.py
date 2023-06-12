import arcade
from screens.OpeningScreen import OpeningScreen
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learn_With_Mazes.settings')
django.setup()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Learn With Mazes"


def main():
    game = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    opening_screen = OpeningScreen()
    game.show_view(opening_screen)
    arcade.run()


if __name__ == "__main__":
    main()
