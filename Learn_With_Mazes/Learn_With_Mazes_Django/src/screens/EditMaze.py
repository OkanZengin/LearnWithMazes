from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.EditMazeButtons import on_mouse_press
from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.EditMazeOnDraw import on_draw
from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import *


class EditMaze(arcade.View):
    def __init__(self, node_wall_index, maze_level, maze_id):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)
        self.maze_id = maze_id
        self.maze_level = maze_level
        if self.maze_level == "EASY":
            self.grid_size = 5
        elif self.maze_level == "MEDIUM":
            self.grid_size = 8
        elif self.maze_level == "HARD":
            self.grid_size = 10
        elif self.maze_level == "EXTREME":
            self.grid_size = 15
        self.re_add_questions = False
        self.node_wall_index = node_wall_index
        self.maze_level = maze_level
        self.cell_width = 460 / GRID_SIZE
        self.cell_height = 460 / GRID_SIZE
        self.grid_start_x = 5
        self.grid_start_y = 5
        self.grid_end_x = 465
        self.grid_end_y = 465
        self.clicked_wall_image = None
        self.maze_id = maze_id
        self.show_grid_lines = False
        self.on_click_button = True
        self.wall_buttons_visible = False
        self.drawing = False
        self.drawing_yellow = False
        self.drawing_unsolvable = False
        self.not_enough_doors = False
        self.too_many_doors = False
        self.blue_square_draw = []
        self.yellow_square_draw = []
        self.coordinates_for_doors = []

    def on_mouse_press(self, x, y, button, modifiers):
        on_mouse_press(self, x, y, button)

    def on_draw(self):
        on_draw(self)


if __name__ == "__main__":
    game = EditMaze()
    arcade.run()
