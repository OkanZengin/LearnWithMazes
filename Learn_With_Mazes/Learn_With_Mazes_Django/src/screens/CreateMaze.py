from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.CreateMazeButtons import on_mouse_press
from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.CreateMazeOnDraw import on_draw
from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import *


class CreateMaze(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)
        self.grid_size = GRID_SIZE
        self.maze_level = "EASY"
        self.cell_width = 460 / GRID_SIZE
        self.cell_height = 460 / GRID_SIZE
        self.grid_start_x = 5
        self.grid_start_y = 5
        self.grid_end_x = 465
        self.grid_end_y = 465
        self.min_door = 2
        self.max_door = 5
        self.clicked_wall_image = None
        self.maze_id = None
        self.show_grid_lines = True
        self.on_click_button = True
        self.wall_buttons_visible = False
        self.drawing = False
        self.drawing_yellow = False
        self.drawing_unsolvable = False
        self.not_enough_doors = False
        self.too_many_doors = False
        self.save_first = False
        self.is_maze_saved = False
        self.check_for_solution = False
        self.maze_saved_questions_not_added = False
        self.blue_square_draw = []
        self.yellow_square_draw = []
        self.node_wall_index = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.coordinates_for_doorss = []

    def on_mouse_press(self, x, y, button, modifiers):
        on_mouse_press(self, x, y, button)

    def on_draw(self):
        on_draw(self)


if __name__ == "__main__":
    game = CreateMaze()
    arcade.run()
