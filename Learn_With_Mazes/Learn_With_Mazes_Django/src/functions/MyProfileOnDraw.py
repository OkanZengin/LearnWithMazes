from ..assets.MenuAssets import *


def on_draw():
    arcade.start_render()

    arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                  arcade.load_texture(MENU_BACKGROUND_IMAGE))

    background_icon_texture = arcade.load_texture(BACKGROUND_IMAGE)
    arcade.draw_texture_rectangle(background_icon_x, background_icon_y,
                                  background_icon_texture.width * background_icon_scale,
                                  background_icon_texture.height * background_icon_scale, background_icon_texture)
    num_rows = 12
    from ..database.MyProfileMazes import MyProfileMazes
    for row in range(num_rows):
        row_y = start_y - ((len(maze_list) * maze_text_spacing) + (row * (rect_height + rect_spacing)))
        for col in range(num_cols):
            rect_x = maze_text_x + (col * (rect_width + rect_spacing))
            if col < 3 and row == 0:
                label = ["Maze Level", "Maze Rating", "Rate Count"][col]
            elif col == 3 and 11 > row > 0 and (row - 1 + MyProfileMazes.current_page_value) \
                    < len(MyProfileMazes.sorted_my_mazes):
                label = "PLAY"
            elif col == 4 and 11 > row > 0 and (row - 1 + MyProfileMazes.current_page_value) \
                    < len(MyProfileMazes.sorted_my_mazes):
                label = "🗑️️️️️️"
            elif col == 5 and 11 > row > 0 and (row - 1 + MyProfileMazes.current_page_value) \
                    < len(MyProfileMazes.sorted_my_mazes):
                label = "✏️"
            elif col == 3 and row == 0:
                label = ""
            elif col == 4 and row == 0:
                label = "NEXT"
            elif col == 0 and 11 > row > 0 and (row - 1 + MyProfileMazes.current_page_value) \
                    < len(MyProfileMazes.sorted_my_mazes):
                maze_level = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_level
                label = maze_level
            elif col == 1 and 11 > row > 0 and (row - 1 + MyProfileMazes.current_page_value) \
                    < len(MyProfileMazes.sorted_my_mazes):
                maze_rating = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].rating
                formatted_rating = "{:.2f}".format(maze_rating)
                label = formatted_rating
            elif col == 2 and 11 > row > 0 and (row - 1 + MyProfileMazes.current_page_value) \
                    < len(MyProfileMazes.sorted_my_mazes):
                rate_count = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].rate_count
                label = rate_count
            elif col > 3 and row == 11:
                label = "BACK"
            else:
                label = ""

            if col == 3 and 11 > row >= 1:
                arcade.draw_rectangle_filled(rect_x+55, row_y+10, button_width, button_height,
                                             arcade.color.ANTIQUE_RUBY)
                arcade.draw_text(
                    label,
                    rect_x,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=12,
                    width=button_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                )
            elif col == 5 and row == 0:
                pass
            elif col == 4 and 11 > row >= 1:
                arcade.draw_rectangle_filled(rect_x + 25, row_y + 10, button_width / 2 - 5, button_height,
                                             arcade.color.ANTIQUE_RUBY)
                arcade.draw_text(
                    label,
                    rect_x + 15,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=10,
                    width=button_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                    font_name="Segoe UI Emoji"
                )
            elif col == 5 and 11 > row >= 1:
                arcade.draw_rectangle_filled(rect_x-30, row_y + 10, button_width / 2-5, button_height,
                                             arcade.color.ANTIQUE_RUBY)
                arcade.draw_text(
                    label,
                    rect_x - 85,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=12,
                    width=button_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                    font_name="Segoe UI Emoji"
                )
            elif col < 4 and 11 > row >= 0:
                arcade.draw_rectangle_filled(rect_x+55, row_y+10, rect_width, rect_height,
                                             arcade.color.ANTIQUE_RUBY)
                arcade.draw_text(
                    label,
                    rect_x,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=12,
                    width=rect_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                )
            elif col == 4 and row == 0:
                arcade.draw_rectangle_filled(rect_x + 55, row_y + 10, rect_width, rect_height,
                                             arcade.color.ANTIQUE_RUBY)
                arcade.draw_text(
                    label,
                    rect_x,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=12,
                    width=rect_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                )
            elif col == 4 and row == 11:
                arcade.draw_rectangle_filled(rect_x + 55, row_y + 10, rect_width, rect_height,
                                             arcade.color.ANTIQUE_RUBY)
                arcade.draw_text(
                    label,
                    rect_x,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=12,
                    width=rect_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                )

    arcade.draw_rectangle_filled(button_1_x, button_1_y, button_1_width, button_1_height, arcade.color.BURNT_ORANGE)
    arcade.draw_text("Go Back", button_1_x, button_1_y, arcade.color.FLORAL_WHITE, font_size=16,
                     width=button_1_width, align="center", anchor_x="center", anchor_y="center", font_name="Consolas")

    arcade.draw_texture_rectangle(button_2_x-20, button_2_y-20, button_2_width+20, 20+button_2_height,
                                  arcade.load_texture("images/mazes_i_played_button.jpg"))

    arcade.draw_rectangle_filled(button_3_x, button_3_y, button_3_width, button_3_height, arcade.color.BURNT_ORANGE)
    arcade.draw_text("Sign Out", button_3_x, button_3_y, arcade.color.FLORAL_WHITE, font_size=16,
                     width=button_2_width, align="center", anchor_x="center", anchor_y="center", font_name="Consolas")

