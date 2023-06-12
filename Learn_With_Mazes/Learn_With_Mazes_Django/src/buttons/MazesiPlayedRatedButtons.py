
from ..assets.MenuAssets import *

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 100
num_rows = 17
num_columns = 6
start_y = 450


def on_mouse_press(self, x, y, button, modifiers):
    from ..database.FindMazesiPlayedRated import MazesIPlayedRated
    if MazesIPlayedRated.mazesiplayedids is None:
        MazesIPlayedRated.mazesiplayedids = []
    gettedmazes = MazesIPlayedRated.mazesiplayedids
    for row in range(num_rows):
        row_y = start_y - ((len(maze_list) * maze_text_spacing) + (row * (rect_height + rect_spacing)))
        for col in range(num_columns):
            rect_x = maze_text_x + (col * (rect_width-20 + rect_spacing))
            from ..assets.SharedData import SharedData
            if col == 0 and row == 0 and rect_x+15 <= x <= rect_x+15 + button_width \
                    and row_y <= y <= row_y + button_height:
                SharedData.order_by_user = True
                SharedData.order_by_rating = False
                SharedData.order_by_level = False
                SharedData.order_by_rate_count = False
            if col == 1 and row == 0 and rect_x+15 <= x <= rect_x+15 + button_width \
                    and row_y <= y <= row_y + button_height:
                SharedData.order_by_level = True
                SharedData.order_by_user = False
                SharedData.order_by_rating = False
                SharedData.order_by_rate_count = False
            if col == 2 and row == 0 and rect_x+15 <= x <= rect_x+15 + button_width \
                    and row_y <= y <= row_y + button_height:
                SharedData.order_by_rating = True
                SharedData.order_by_user = False
                SharedData.order_by_level = False
                SharedData.order_by_rate_count = False
            if col == 3 and row == 0 and rect_x+15 <= x <= rect_x+15 + button_width \
                    and row_y <= y <= row_y + button_height:
                SharedData.order_by_rate_count = True
                SharedData.order_by_user = False
                SharedData.order_by_level = False
                SharedData.order_by_rating = False
            if SharedData.order_by_user:
                mazes = sorted(gettedmazes, key=lambda maze: maze.user.lower())
            elif SharedData.order_by_level:
                mazes = sorted(gettedmazes,
                               key=lambda maze: ('EXTREME', 'HARD', 'MEDIUM', 'EASY').index(maze.maze_level))
            elif SharedData.order_by_rating:
                mazes = sorted(gettedmazes, key=lambda maze: (-maze.rating,))
            elif SharedData.order_by_rate_count:
                mazes = sorted(gettedmazes, key=lambda maze: (-maze.rate_count,))
            else:
                mazes = gettedmazes
            if col == 5 and 16 > row >= 1 and rect_x+15 <= x <= rect_x+15 + button_width \
                    and row_y+10 <= y <= row_y+10 + button_height:
                maze_layout = mazes[row + MazesIPlayedRated.current_page_value - 1].maze_layout
                maze_level = mazes[row + MazesIPlayedRated.current_page_value - 1].maze_level
                maze_id = mazes[row + MazesIPlayedRated.current_page_value - 1].maze_id
                walls = mazes[row + MazesIPlayedRated.current_page_value - 1].maze_wall_positioning
                creator = mazes[row + MazesIPlayedRated.current_page_value - 1].user
                from ..assets.SharedData import SharedData
                SharedData.current_node_wall_index = maze_layout
                from ..screens.PlayMaze import PlayMaze
                play_maze = PlayMaze(maze_layout, maze_level, walls, maze_id, creator)
                self.window.show_view(play_maze)
            elif col == 5 and row == 0 and rect_x+15 <= x <= rect_x+15 + button_width \
                    and row_y <= y <= row_y + button_height:
                if MazesIPlayedRated.current_page_value + 14 > len(MazesIPlayedRated.mazesiplayedids):
                    pass
                else:
                    MazesIPlayedRated.current_page_value += 14
            elif col == 5 and row == 16 and rect_x+15 <= x <= rect_x+15 + button_width \
                    and row_y <= y <= row_y + button_height:
                if MazesIPlayedRated.current_page_value == 0:
                    pass
                else:
                    MazesIPlayedRated.current_page_value -= 14

        if (
                button_1_x - button_1_width / 2 <= x <= button_1_x + button_1_width / 2 and
                button_1_y - button_1_height / 2 <= y <= button_1_y + button_1_height / 2
        ):
            from ..screens.MainMenu import MainMenu
            main_menu = MainMenu()
            main_menu.window.show_view(main_menu)
