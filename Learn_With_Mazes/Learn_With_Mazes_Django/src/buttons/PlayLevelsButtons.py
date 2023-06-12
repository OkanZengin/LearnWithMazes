import arcade
from ..assets.MenuAssets import button_1_x, button_1_y, button_1_width, button_1_height
num_columns = 4
button_spacing = 10
num_rows = 11
button_width = 120
button_height = 30
maze_text_x = 50
start_y = 450


class PlayLevelsButtons:
    def __init__(self, window):
        self.window = window

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for row in range(num_rows):
                row_y = start_y - (row * (button_height + button_spacing))
                for col in range(num_columns):
                    rect_x = maze_text_x + (col * (button_width + button_spacing))
                    if (
                        rect_x <= x <= rect_x + button_width
                        and row_y - button_height / 2 <= y <= row_y + button_height / 2
                    ):
                        if col == 0 and row > 0:
                            from ..database.PlayMazeEasyLevels import EasyMazes
                            maze_layout = EasyMazes.sorted_easy_mazes[row-1].maze_layout
                            maze_level = EasyMazes.sorted_easy_mazes[row-1].maze_level
                            maze_id = EasyMazes.sorted_easy_mazes[row-1].maze_id
                            maze_wall_positioning = EasyMazes.sorted_easy_mazes[row-1].maze_wall_positioning
                            creator = EasyMazes.sorted_easy_mazes[row-1].user
                            from ..assets.SharedData import SharedData
                            SharedData.current_node_wall_index = maze_layout
                            from ..screens.PlayMaze import PlayMaze
                            play_maze = PlayMaze(maze_layout, maze_level, maze_wall_positioning, maze_id, creator)
                            self.window.show_view(play_maze)
                        elif col == 1 and row > 0:
                            from ..database.PlayMazeMediumLevels import MediumMazes
                            maze_layout = MediumMazes.sorted_medium_mazes[row-1].maze_layout
                            maze_level = MediumMazes.sorted_medium_mazes[row-1].maze_level
                            maze_id = MediumMazes.sorted_medium_mazes[row-1].maze_id
                            maze_wall_positioning = MediumMazes.sorted_medium_mazes[row-1].maze_wall_positioning
                            creator = MediumMazes.sorted_medium_mazes[row - 1].user
                            from ..assets.SharedData import SharedData
                            SharedData.current_node_wall_index = maze_layout
                            from ..screens.PlayMaze import PlayMaze
                            play_maze = PlayMaze(maze_layout, maze_level, maze_wall_positioning,  maze_id, creator)
                            self.window.show_view(play_maze)
                        elif col == 2:
                            from ..database.PlayMazeHardLevels import HardMazes
                            maze_layout = HardMazes.sorted_hard_mazes[row-1].maze_layout
                            maze_level = HardMazes.sorted_hard_mazes[row-1].maze_level
                            maze_id = HardMazes.sorted_hard_mazes[row-1].maze_id
                            maze_wall_positioning = HardMazes.sorted_hard_mazes[row-1].maze_wall_positioning
                            creator = HardMazes.sorted_hard_mazes[row-1].user
                            from ..assets.SharedData import SharedData
                            SharedData.current_node_wall_index = maze_layout
                            from ..screens.PlayMaze import PlayMaze
                            play_maze = PlayMaze(maze_layout, maze_level, maze_wall_positioning,  maze_id, creator)
                            self.window.show_view(play_maze)
                        elif col == 3:
                            from ..database.PlayMazeExtremeLevels import ExtremeMazes
                            maze_layout = ExtremeMazes.sorted_extreme_mazes[row-1].maze_layout
                            maze_level = ExtremeMazes.sorted_extreme_mazes[row-1].maze_level
                            maze_id = ExtremeMazes.sorted_extreme_mazes[row-1].maze_id
                            maze_wall_positioning = ExtremeMazes.sorted_extreme_mazes[row-1].maze_wall_positioning
                            creator = ExtremeMazes.sorted_extreme_mazes[row-1].user
                            from ..assets.SharedData import SharedData
                            SharedData.current_node_wall_index = maze_layout
                            from ..screens.PlayMaze import PlayMaze
                            play_maze = PlayMaze(maze_layout, maze_level, maze_wall_positioning,  maze_id, creator)
                            self.window.show_view(play_maze)

                    if (
                            button_1_x - button_1_width / 2 <= x <= button_1_x + button_1_width / 2 and
                            button_1_y - button_1_height / 2 <= y <= button_1_y + button_1_height / 2
                    ):
                        from ..screens.MainMenu import MainMenu
                        main_menu = MainMenu()
                        main_menu.window.show_view(main_menu)
