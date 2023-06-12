from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import *


def on_draw(self):
    arcade.start_render()
    arcade.draw_texture_rectangle(235, 235, 460, 460, maze_background)
    for button_name, (button_x, button_y) in buttons.items():
        if button_name == "SAVE":
            width = 115
            height = 66
            arcade.draw_rectangle_filled(button_x+5, button_y, width, height, BUTTON_COLOR)
            arcade.draw_text(button_name, button_x, button_y, BUTTON_TEXT_COLOR, font_size=10, anchor_x="center",
                             anchor_y="center", font_name="Consolas")
        else:
            arcade.draw_rectangle_filled(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR)
            arcade.draw_text(button_name, button_x, button_y, BUTTON_TEXT_COLOR, font_size=10, anchor_x="center",
                             anchor_y="center", font_name="Consolas")
    self.cell_width = 460 / self.grid_size
    self.cell_height = 460 / self.grid_size
    self.previous_node = [0, 0]

    if self.show_grid_lines:
        for column in range(self.grid_size + 1):
            x = self.grid_start_x + column * self.cell_width
            y1 = self.grid_start_y
            y2 = self.grid_end_y
            arcade.draw_line(x, y1, x, y2, arcade.color.BLACK)
        for row in range(self.grid_size + 1):
            y = self.grid_start_y + row * self.cell_height
            x1 = self.grid_start_x
            x2 = self.grid_end_x
            arcade.draw_line(x1, y, x2, y, arcade.color.BLACK)

    rectangle_positions = [(500, 545), (560, 545), (500, 485), (560, 485), (500, 425), (560, 425), (500, 365),
                           (560, 365), (500, 305), (560, 305), (500, 245), (560, 245), (500, 185), (560, 185),
                           (500, 125), (560, 125)]
    [arcade.draw_rectangle_filled(x, y, 51, 51, arcade.color.LIGHT_GRAY) or
     arcade.draw_rectangle_outline(x, y, 50, 50, arcade.color.LIGHT_GRAY, 5) for x, y in rectangle_positions]
    if self.wall_buttons_visible:
        for button_name, (button_x, button_y) in wall_buttons.items():
            button_image = wall_images[button_name]
            arcade.draw_texture_rectangle(button_x, button_y, WALL_BUTTON_SIZE, WALL_BUTTON_SIZE, button_image)
    if self.on_click_button:
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                x = self.grid_start_x + column * self.cell_width
                y = self.grid_start_y + row * self.cell_height
                grid_node_width = self.cell_width
                grid_node_height = self.cell_height
                wall_index = self.node_wall_index[row][column]
                wall_image_name = list(wall_images.keys())[wall_index]
                wall_image_texture = wall_images[wall_image_name]
                if wall_image_name == "E_Wall" and self.clicked_wall_image is None:
                    arcade.draw_texture_rectangle(x + (self.cell_width - 1) / 2, y + (self.cell_height - 1) / 2,
                                                  grid_node_width - 2, grid_node_height - 2, wall_image_texture)

                elif wall_image_name != "E_Wall" and self.clicked_wall_image is None:
                    arcade.draw_texture_rectangle(x + self.cell_width / 2, y + self.cell_height / 2,
                                                  grid_node_width + 1, grid_node_height + 1, wall_image_texture)
                elif wall_image_name == "E_Wall" and self.clicked_wall_image:
                    arcade.draw_texture_rectangle(x + self.cell_width / 2, y + self.cell_height / 2,
                                                  grid_node_width - 1, grid_node_height - 1, wall_image_texture)
                else:
                    arcade.draw_texture_rectangle(x + self.cell_width / 2, y + self.cell_height / 2,
                                                  grid_node_width + 1, grid_node_height + 1, wall_image_texture)
    arcade.draw_text("start", self.cell_width / 4.5, self.cell_height / 2.5, arcade.color.COOL_BLACK,
                     145 / self.grid_size,
                     anchor_x="left", anchor_y="baseline", font_name="Impact")
    arcade.draw_text("end", 465 - self.cell_width / 4.5, 465 - self.cell_height / 4, arcade.color.COOL_BLACK,
                     145 / self.grid_size,
                     anchor_x="right", anchor_y="top", font_name="Impact")

    if self.drawing:
        for coordinate in self.blue_square_draw:
            scol, srow = coordinate
            x = self.grid_start_x + srow * self.cell_width
            y = self.grid_start_y + scol * self.cell_height
            grid_node_width = self.cell_width
            grid_node_height = self.cell_height
            arcade.draw_rectangle_filled(x + self.cell_width / 2, y + self.cell_height / 2,
                                         grid_node_width / 5, grid_node_height / 5, arcade.color.BLUE)

    if self.drawing_yellow:
        for coordinate in self.yellow_square_draw:
            scol, srow = coordinate
            x = self.grid_start_x + srow * self.cell_width
            y = self.grid_start_y + scol * self.cell_height
            grid_node_width = self.cell_width
            arcade.draw_circle_filled(x + self.cell_width / 2, y + self.cell_height / 2,
                                      grid_node_width / 8, arcade.color.YELLOW)

    if self.drawing_unsolvable:
        arcade.draw_text("UNSOLVABLE", 235, 235, arcade.color.BLACK,
                         60,
                         anchor_x="center", anchor_y="center", font_name="Impact")

    if self.check_for_solution:
        arcade.draw_text("Check For Solution First", 235, 235, arcade.color.BLACK,
                         30,
                         anchor_x="center", anchor_y="center", font_name="Impact")

    if self.not_enough_doors:
        arcade.draw_text("NOT ENOUGH DOORS", 235, 235, arcade.color.BLACK,
                         40,
                         anchor_x="center", anchor_y="center", font_name="Impact")

    if self.too_many_doors:
        arcade.draw_text("TOO MANY DOORS", 235, 235, arcade.color.BLACK,
                         40,
                         anchor_x="center", anchor_y="center", font_name="Impact")
    if self.save_first:
        arcade.draw_text("Save Maze First", 235, 235, arcade.color.BLACK,
                         40,
                         anchor_x="center", anchor_y="center", font_name="Impact")

    if self.maze_saved_questions_not_added:
        arcade.draw_text("You need to add questions", 235, 235, arcade.color.BLACK,
                         24,
                         anchor_x="center", anchor_y="center", font_name="Impact")

    if self.is_maze_saved:
        arcade.draw_text("Maze SAVED", 235, 335, arcade.color.BLACK,
                         30,
                         anchor_x="center", anchor_y="center", font_name="Impact")

        arcade.draw_text("Please Add Questions", 235, 235, arcade.color.BLACK,
                         30,
                         anchor_x="center", anchor_y="center", font_name="Impact")
