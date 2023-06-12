from ..assets.MenuAssets import *


def on_draw():
    arcade.start_render()
    arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                  arcade.load_texture(MENU_BACKGROUND_IMAGE))
    background_icon_texture = arcade.load_texture(BACKGROUND_IMAGE)
    arcade.draw_texture_rectangle(background_icon_x, background_icon_y,
                                  background_icon_texture.width * background_icon_scale,
                                  background_icon_texture.height * background_icon_scale, background_icon_texture)

    num_columns = 6
    num_rows = 17
    button_width = 90
    maze_text_x = 50
    start_y = 450
    from ..database.FindAllMazes import FindAllMazes
    from ..database.GetMyRating import get_my_rating
    from ..assets.SharedData import SharedData
    gettedmazes = FindAllMazes.sorted_all_mazes
    if SharedData.order_by_user:
        mazes = sorted(gettedmazes, key=lambda maze: maze.user.lower())
    elif SharedData.order_by_level:
        mazes = sorted(gettedmazes, key=lambda maze: ('EXTREME', 'HARD', 'MEDIUM', 'EASY').index(maze.maze_level))
    elif SharedData.order_by_rating:
        mazes = sorted(gettedmazes, key=lambda maze: (-maze.rating,))
    elif SharedData.order_by_rate_count:
        mazes = sorted(gettedmazes, key=lambda maze: (-maze.rate_count,))
    else:
        mazes = gettedmazes
    for row in range(num_rows):
        row_y = start_y - ((len(maze_list) * maze_text_spacing) + (row * (rect_height + rect_spacing)))
        for col in range(num_columns):

            rect_x = maze_text_x + (col * (rect_width - 20 + rect_spacing))
            if col < 5 and row == 0:
                label = ["Creator", "Maze Level", "Maze Rating", "Rate Count", "My Rating"][col]
            elif col == 5 and row > 0 and (row + FindAllMazes.current_page_value - 1) < len(mazes):
                label = "PLAY"
            elif col == 5 and row == 0:
                label = "NEXT"
            elif col == 5 and row == 16:
                label = "BACK"
            elif col == 0 and 16 > row > 0 and (row + FindAllMazes.current_page_value - 1) < len(mazes):
                maze_creator = mazes[row + FindAllMazes.current_page_value - 1].user
                label = maze_creator
            elif col == 1 and 16 > row > 0 and (row + FindAllMazes.current_page_value - 1) < len(mazes):
                maze_level = mazes[row + FindAllMazes.current_page_value - 1].maze_level
                label = maze_level
            elif col == 2 and 16 > row > 0 and (row + FindAllMazes.current_page_value - 1) < len(mazes):
                maze_rating = mazes[row + FindAllMazes.current_page_value - 1].rating
                formatted_rating = "{:.2f}".format(maze_rating)
                label = formatted_rating
            elif col == 3 and 16 > row > 0 and (row + FindAllMazes.current_page_value - 1) < len(mazes):
                rate_count = mazes[row + FindAllMazes.current_page_value - 1].rate_count
                label = rate_count
            elif col == 4 and 16 > row > 0 and (row + FindAllMazes.current_page_value - 1) < len(mazes):
                maze_id = mazes[row + FindAllMazes.current_page_value - 1].maze_id
                my_rating = get_my_rating(maze_id)
                if my_rating is not None:
                    label = my_rating
                else:
                    label = "None"
            elif col < 5 and 16 > row > 0 and (row + FindAllMazes.current_page_value - 1) >= len(mazes):
                label = ""

            if col == 5 and row == 0:
                arcade.draw_rectangle_filled(
                    rect_x + 15, row_y + 10, rect_width - 20, rect_height, arcade.color.ALABAMA_CRIMSON
                )
                arcade.draw_text(
                    label,
                    rect_x - 40,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=14,
                    width=button_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                    font_name="Consolas",
                )
            if col == 5 and 16 > row > 0:
                arcade.draw_rectangle_filled(
                    rect_x + 15, row_y + 10, rect_width - 20, rect_height, arcade.color.BLUE_SAPPHIRE
                )
                arcade.draw_text(
                    label,
                    rect_x - 40,
                    row_y,
                    arcade.color.GHOST_WHITE,
                    font_size=10,
                    width=button_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                    font_name="Consolas",
                )
            elif col == 5 and row == 16:
                arcade.draw_rectangle_filled(
                    rect_x + 15, row_y + 10, rect_width - 20, rect_height, arcade.color.ALABAMA_CRIMSON
                )
                arcade.draw_text(
                    "BACK",
                    rect_x - 40,
                    row_y,
                    arcade.color.FLORAL_WHITE,
                    font_size=14,
                    width=button_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                    font_name="Consolas",
                )
            elif col < 5 and row == 16:
                pass
            elif col < 5 and row == 0:
                arcade.draw_rectangle_filled(
                    rect_x + 15, row_y + 10, rect_width - 20, rect_height, arcade.color.ASPARAGUS
                )
                arcade.draw_text(
                    label,
                    rect_x - 40,
                    row_y,
                    arcade.color.COOL_BLACK,
                    font_size=10,
                    width=rect_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                    font_name="Consolas",
                )
            elif col < 5:
                arcade.draw_rectangle_filled(
                    rect_x + 15, row_y + 10, rect_width - 20, rect_height, arcade.color.BURNT_ORANGE
                )
                arcade.draw_text(
                    label,
                    rect_x - 40,
                    row_y,
                    arcade.color.COOL_BLACK,
                    font_size=10,
                    width=rect_width,
                    align="center",
                    anchor_x="left",
                    anchor_y="bottom",
                    font_name="Consolas",
                )

    arcade.draw_rectangle_filled(button_1_x, button_1_y, button_1_width, button_1_height, arcade.color.LIGHT_GRAY)
    arcade.draw_text("Go Back", button_1_x, button_1_y, arcade.color.BLACK, font_size=16,
                     width=button_1_width, align="center", anchor_x="center", anchor_y="center", font_name="Consolas")
