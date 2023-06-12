from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import *


def on_draw(self):
    arcade.start_render()
    arcade.draw_texture_rectangle(280, 280, 550, 550, maze_background)
    go_back_button_width = 100
    go_back_button_height = 25
    go_back_button_x = 10
    go_back_button_y = self.window.height - go_back_button_height - 10

    arcade.draw_rectangle_filled(go_back_button_x + go_back_button_width / 2,
                                 go_back_button_y + go_back_button_height / 2,
                                 go_back_button_width, go_back_button_height, arcade.color.LIGHT_GRAY)
    arcade.draw_text("Go Back", go_back_button_x + 15, go_back_button_y + 5, arcade.color.BLACK, 12,
                     anchor_x="left", anchor_y="baseline", font_name="Consolas")
    arcade.draw_rectangle_filled(540, 580, go_back_button_width+10, go_back_button_height+5, arcade.color.LIGHT_GRAY)
    arcade.draw_text("Solution", 505, 572, arcade.color.BLACK, 12,
                     anchor_x="left", anchor_y="baseline", font_name="Consolas")
    arcade.draw_rectangle_filled(330, 580, go_back_button_width+50, go_back_button_height+5, arcade.color.LIGHT_GRAY)
    arcade.draw_text("Hide Solution", 275, 572, arcade.color.BLACK, 12,
                     anchor_x="left", anchor_y="baseline", font_name="Consolas")
    self.cell_width = 550 / self.grid_size
    self.cell_height = 550 / self.grid_size
    self.previous_node = [0, 0]

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
                if wall_image_name == "E_Wall":
                    arcade.draw_texture_rectangle(x + self.cell_width / 2, y + self.cell_height / 2,
                                                  grid_node_width - 1, grid_node_height - 1, wall_image_texture)
                else:
                    arcade.draw_texture_rectangle(x + self.cell_width / 2, y + self.cell_height / 2,
                                                  grid_node_width + 1, grid_node_height + 1, wall_image_texture)
    arcade.draw_text("start", self.cell_width / 4.5, self.cell_height / 2.5, arcade.color.BLUE,
                     145 / self.grid_size,
                     anchor_x="left", anchor_y="baseline", font_name="Impact")
    arcade.draw_text("end", 550 - self.cell_width / 4.5, 550 - self.cell_height / 4, arcade.color.BLUE,
                     145 / self.grid_size,
                     anchor_x="right", anchor_y="top", font_name="Impact")

    circle_radius = self.cell_width / 5
    circle_x = (self.cell_width/2) + self.grid_start_x + (self.current_column * self.cell_width)
    circle_y = (self.cell_width/2) + self.grid_start_y + (self.current_row * self.cell_height)
    arcade.draw_circle_filled(circle_x, circle_y, circle_radius, arcade.color.RED)

    if self.maze_solved:
        arcade.draw_text("MAZE SOLVED", 275, 300, arcade.color.AMARANTH_PURPLE, 70, anchor_x="center", anchor_y="baseline", font_name="Impact")
        arcade.draw_text("CONGRATULATIONS", 275, 280, arcade.color.APPLE_GREEN, 45, anchor_x="center", anchor_y="top", font_name="Impact")

    if self.drawing_yellow:
        for coordinate in self.yellow_square_draw:
            scol, srow = coordinate
            x = self.grid_start_x + srow * self.cell_width
            y = self.grid_start_y + scol * self.cell_height
            grid_node_width = self.cell_width
            arcade.draw_circle_filled(x + self.cell_width / 2, y + self.cell_height / 2,
                                      grid_node_width / 8, arcade.color.COOL_BLACK)
