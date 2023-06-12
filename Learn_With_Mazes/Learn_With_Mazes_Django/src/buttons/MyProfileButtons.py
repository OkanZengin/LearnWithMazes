from ..assets.MenuAssets import *

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
num_rows = 12


def on_mouse_press(self, x, y, button, modifiers):
    from ..assets.SharedData import SharedData
    from ..database.MyProfileMazes import MyProfileMazes
    from ..database.MyProfileMazes import get_my_mazes
    MyProfileMazes.sorted_my_mazes = get_my_mazes(MyProfileMazes.my_sorted_mazes)
    for row in range(num_rows):
        row_y = start_y - ((len(maze_list) * maze_text_spacing) + (row * (rect_height + rect_spacing)))
        for col in range(num_cols):
            rect_x = maze_text_x + (col * (rect_width + rect_spacing))
            if col == 3 and 11 > row >= 1 and rect_x <= x <= rect_x + button_width \
                    and row_y <= y <= row_y + button_height:
                maze_layout = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_layout
                maze_level = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_level
                maze_id = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_id
                maze_wall_positions = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].\
                    maze_wall_positioning
                creator = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].user
                SharedData.current_node_wall_index = maze_layout
                from ..screens.PlayMaze import PlayMaze
                play_maze = PlayMaze(maze_layout, maze_level, maze_wall_positions, maze_id, creator)
                self.window.show_view(play_maze)
                MyProfileMazes.sorted_my_mazes = get_my_mazes(MyProfileMazes.my_sorted_mazes)
            elif col == 4 and 11 > row >= 1 and rect_x <= x <= rect_x + (button_width/2-5) and row_y <= y <= row_y + \
                    button_height:
                maze_layout = MyProfileMazes.sorted_my_mazes[row - 1 + MyProfileMazes.current_page_value].maze_layout
                maze_id = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_id
                from ..usermaze.UserMazeModel import UserMaze
                UserMaze.objects.filter(maze_layout__exact=maze_layout).delete()
                from ..question.QuestionModel import Question
                Question.objects.filter(maze_id=maze_id).delete()
                MyProfileMazes.sorted_my_mazes = get_my_mazes(MyProfileMazes.my_sorted_mazes)
            elif col == 5 and 11 > row >= 1 and rect_x - 55 <= x <= rect_x - 55 + (button_width/2-5) \
                    and row_y <= y <= row_y + button_height:
                maze_layout = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_layout
                maze_level = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_level
                maze_id = MyProfileMazes.sorted_my_mazes[row-1 + MyProfileMazes.current_page_value].maze_id
                from ..screens.EditMaze import EditMaze
                edit_maze = EditMaze(maze_layout, maze_level, maze_id)
                self.window.show_view(edit_maze)
                MyProfileMazes.sorted_my_mazes = get_my_mazes(MyProfileMazes.my_sorted_mazes)
            elif col == 4 and row == 0 and rect_x <= x <= rect_x + button_width and row_y <= y <= row_y + button_height:
                if MyProfileMazes.current_page_value + 10 < len(MyProfileMazes.sorted_my_mazes):
                    MyProfileMazes.current_page_value += 10
                else:
                    pass
            elif col == 4 and row == 11 and rect_x <= x <= rect_x + button_width and row_y <= y <= row_y + \
                    button_height:
                if MyProfileMazes.current_page_value != 0:
                    MyProfileMazes.current_page_value -= 10
                else:
                    pass

    if (
            button_1_x - button_1_width / 2 <= x <= button_1_x + button_1_width / 2 and
            button_1_y - button_1_height / 2 <= y <= button_1_y + button_1_height / 2
    ):
        from ..screens.MainMenu import MainMenu
        main_menu = MainMenu()
        main_menu.window.show_view(main_menu)
    elif (
            button_2_x - button_2_width / 2 <= x <= button_2_x + button_2_width / 2 and
            button_2_y - button_2_height / 2 <= y <= button_2_y + button_2_height / 2
    ):
        from ..screens.MazesIPlayed import MazesIPlayed
        mazes_i_played = MazesIPlayed()
        mazes_i_played.window.show_view(mazes_i_played)
    elif (
            button_3_x - button_3_width / 2 <= x <= button_3_x + button_3_width / 2 and
            button_3_y - button_3_height / 2 <= y <= button_3_y + button_3_height / 2
    ):
        from ..assets.SharedData import SharedData
        SharedData.signed_in_flag = False
        SharedData.current_username = None
        from ..screens.MainMenu import MainMenu
        main_menu = MainMenu()
        main_menu.window.show_view(main_menu)
