from ..assets.MenuAssets import *


def on_draw():
    arcade.start_render()
    arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                  arcade.load_texture(MENU_BACKGROUND_IMAGE))

    background_icon_texture = arcade.load_texture(BACKGROUND_IMAGE)
    arcade.draw_texture_rectangle(background_icon_x, background_icon_y,
                                  background_icon_texture.width * background_icon_scale,
                                  background_icon_texture.height * background_icon_scale, background_icon_texture)

    num_columns = 4
    num_rows = 11
    button_width = 120
    button_height = 30
    button_spacing = 10
    maze_text_x = 50
    start_y = 450

    for col in range(num_columns):
        rect_x = maze_text_x + (col * (button_width + button_spacing))
        label = ["EASY", "MEDIUM", "HARD", "EXTREME"][col]
        arcade.draw_rectangle_filled(
            rect_x + button_width / 2, start_y, button_width, button_height, arcade.color.COOL_BLACK
        )
        arcade.draw_text(
            label,
            rect_x,
            start_y,
            arcade.color.AFRICAN_VIOLET,
            font_size=18,
            width=button_width,
            align="center",
            anchor_x="left",
            anchor_y="center",
            font_name="Consolas",
        )

    for row in range(num_rows - 1):
        row_y = start_y - ((row + 1) * (button_height + button_spacing))
        for col in range(num_columns):
            rect_x = maze_text_x + (col * (button_width + button_spacing))
            label = f"Level: {row + 1}"
            from ..assets.SharedData import SharedData
            if SharedData.user_played[row][col] == 1:
                button_color = arcade.color.GREEN
            else:
                button_color = arcade.color.COOL_BLACK

            arcade.draw_rectangle_filled(
                rect_x + button_width / 2, row_y, button_width, button_height, button_color
            )
            arcade.draw_text(
                label,
                rect_x,
                row_y,
                arcade.color.AFRICAN_VIOLET,
                font_size=12,
                width=button_width,
                align="center",
                anchor_x="left",
                anchor_y="center",
                font_name="Consolas",
            )

    arcade.draw_rectangle_filled(button_1_x, button_1_y, button_1_width, button_1_height, arcade.color.LIGHT_GRAY)
    arcade.draw_text("Go Back", button_1_x, button_1_y, arcade.color.BLACK, font_size=16,
                     width=button_1_width, align="center", anchor_x="center", anchor_y="center", font_name="Consolas")



