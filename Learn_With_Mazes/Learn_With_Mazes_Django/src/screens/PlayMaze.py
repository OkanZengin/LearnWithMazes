from Learn_With_Mazes.Learn_With_Mazes_Django.src.buttons.PlayMazeButtons import on_mouse_press, on_key_press
from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.PlayMazeOnDraw import on_draw
from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import *


class PlayMaze(arcade.View):
    def __init__(self, node_wall_index, maze_level, maze_wall_positioning, maze_id, creator):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)
        self.maze_level = maze_level
        self.creator = creator
        self.maze_id = maze_id
        if maze_level == "EASY":
            self.grid_size = 5
        elif maze_level == "MEDIUM":
            self.grid_size = 8
        elif maze_level == "HARD":
            self.grid_size = 10
        elif maze_level == "EXTREME":
            self.grid_size = 15
        self.maze_wall_positioning = maze_wall_positioning
        self.node_wall_index = node_wall_index
        self.cell_width = 550 / GRID_SIZE
        self.cell_height = 550 / GRID_SIZE
        self.grid_start_x = 5
        self.grid_start_y = 5
        self.grid_end_x = 555
        self.grid_end_y = 555
        self.on_click_button = True
        self.current_row = 0
        self.current_column = 0
        self.maze_solved = False
        self.blue_square_draw = []
        self.yellow_square_draw = []
        self.drawing = False
        self.drawing_yellow = False

    def on_mouse_press(self, x, y, button, modifiers):
        on_mouse_press(self, x, y, button)

    def on_key_press(self, key, modifiers):
        on_key_press(self, key, modifiers)

    def on_draw(self):
        on_draw(self)


if __name__ == "__main__":
    game = PlayMaze()
    arcade.run()
