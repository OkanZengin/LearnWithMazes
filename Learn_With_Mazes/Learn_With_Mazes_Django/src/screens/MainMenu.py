from ..assets.MenuAssets import *
from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.MainMenuButtons import MainMenuButtons


class MainMenu(arcade.View):
    def on_show(self):
        self.button_list = []
        self.button_list.append(
            MainMenuButtons(150, 450, "images/create_maze_button.jpg",
                            MainMenuButtons.on_create_maze_button_press, self.window))
        self.button_list.append(
            MainMenuButtons(450, 450, "images/general_mazes_button.jpg",
                            MainMenuButtons.on_general_mazes_button_press, self.window))
        self.button_list.append(
            MainMenuButtons(300, 300, "images/mazes_i_played_button.jpg",
                            MainMenuButtons.on_mazes_i_played_button_press, self.window))
        self.button_list.append(
            MainMenuButtons(150, 150, "images/my_profile_button.jpg",
                            MainMenuButtons.on_my_profile_button_press, self.window))
        self.button_list.append(
            MainMenuButtons(450, 150, "images/play_levels_button.jpg",
                            MainMenuButtons.on_play_levels_button_press, self.window))

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      arcade.load_texture(MENU_BACKGROUND_IMAGE))

        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.button_list:
            if button.check_hover(x, y):
                button.on_press()

