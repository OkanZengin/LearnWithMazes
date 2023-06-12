from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.AStarSearchAlgorithm import a_star_search
from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import *


def on_mouse_press(self, x, y, button):
    for button_name, (button_x, button_y) in buttons.items():
        if button_x - BUTTON_WIDTH // 2 <= x <= button_x + BUTTON_WIDTH // 2 and \
                button_y - BUTTON_HEIGHT // 2 <= y <= button_y + BUTTON_HEIGHT // 2:
            from ..assets.SharedData import SharedData
            if button_name == "Go-Back":
                if SharedData.add_questions:
                    from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.MyProfile import MyProfile
                    my_profile = MyProfile()
                    my_profile.window.show_view(my_profile)
                else:
                    self.re_add_questions = True
            elif button_name == "By Click":
                self.wall_buttons_visible = False
                self.on_click_button = True
            elif button_name == "By Select":
                self.wall_buttons_visible = True
                draw_buttons()
            elif button_name == "Hide Grid":
                self.show_grid_lines = False
            elif button_name == "Show Grid":
                self.show_grid_lines = True
            elif button_name == "Solution":
                a_star_search(self, self.node_wall_index, self.grid_size, wall_images_values)
            elif button_name == "Clear":
                for row in range(self.grid_size):
                    for column in range(self.grid_size):
                        self.node_wall_index[row][column] = 0
                self.drawing = False
                self.drawing_unsolvable = False
                self.not_enough_doors = False
                self.too_many_doors = False
                self.blue_square_draw = []
                self.yellow_square_draw = []
            elif button_name == "Add Q & A":
                count = check_wall_count(self)
                self.not_enough_doors = False
                self.too_many_doors = False
                if count < 2:
                    self.not_enough_doors = True
                elif count > 5:
                    self.too_many_doors = True
                elif 2 <= count <= 5:
                    from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.AddQuestions import AddQuestions
                    add_questions_view = AddQuestions(self.door_count, self.node_wall_index, self.coordinates_for_doors)
                    add_questions_view.run()
            elif button_name == "SAVE":
                check_wall_count(self)
                from ..assets.SharedData import SharedData
                update_maze(self.maze_id, self.node_wall_index, self.coordinates_for_doors)
                SharedData.current_maze_id = self.maze_id
        for wall_button_name, (button_x, button_y) in wall_buttons.items():
            if (
                    button_x - WALL_BUTTON_SIZE / 2 <= x <= button_x + WALL_BUTTON_SIZE / 2
                    and button_y - WALL_BUTTON_SIZE / 2 <= y <= button_y + WALL_BUTTON_SIZE / 2
            ):
                self.clicked_wall_image = wall_button_name
        if self.on_click_button:
            if 5 <= x <= 465 and 5 <= y <= 465:
                column = int((x - 5) // (460 / self.grid_size))
                row = int((y - 5) // (460 / self.grid_size))
                if button == arcade.MOUSE_BUTTON_LEFT and self.wall_buttons_visible is False:
                    wall_index = self.node_wall_index[row][column]
                    self.node_wall_index[row][column] = (wall_index + 1) % len(wall_images)
                    self.drawing_unsolvable = False
                    self.drawing = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.blue_square_draw = []
                    self.yellow_square_draw =[]
                    break
                elif button == arcade.MOUSE_BUTTON_RIGHT and self.wall_buttons_visible is False:
                    wall_index = self.node_wall_index[row][column]
                    self.node_wall_index[row][column] = (wall_index - 1) % len(wall_images)
                    self.drawing_unsolvable = False
                    self.drawing = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.blue_square_draw = []
                    self.yellow_square_draw = []
                    break
                elif button == arcade.MOUSE_BUTTON_LEFT and self.wall_buttons_visible:
                    wall_image_name = self.clicked_wall_image
                    image_index = list(wall_images.keys()).index(wall_image_name)
                    self.node_wall_index[row][column] = image_index
                    self.drawing_unsolvable = False
                    self.drawing = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.blue_square_draw = []
                    self.yellow_square_draw = []
                    break


def set_grid_size(self, size):
    self.grid_size = size
    self.node_wall_index = [[0] * self.grid_size for _ in range(self.grid_size)]
    for row in range(self.grid_size):
        for column in range(self.grid_size):
            if row < len(self.node_wall_index) and column < len(self.node_wall_index[row]):
                self.node_wall_index[row][column] = 0


def update_node_wall_index(self, row, column):
    num_wall_images = len(wall_images)
    self.node_wall_index[row][column] += 1
    self.node_wall_index[row][column] %= num_wall_images


def draw_buttons():
    for wall_button_name, (button_x, button_y) in wall_buttons.items():
        button_image = wall_images[wall_button_name]
        arcade.draw_texture_rectangle(button_x, button_y, WALL_BUTTON_SIZE, WALL_BUTTON_SIZE, button_image)


def check_wall_count(self):
    self.door_count = 0
    self.coordinates_for_doors = []
    for row in range(self.grid_size):
        for column in range(self.grid_size):
            if self.node_wall_index[row][column] == 15 or \
                    self.node_wall_index[row][column] == 16:
                coordinate = (column, row)
                self.coordinates_for_doors.append(coordinate)
                self.door_count += 1

    return self.door_count


def update_maze(maze_id, maze_layout, coordinates_for_walls):
    try:
        from ..database.FindMazeDetails import find_maze_details
        user_maze = find_maze_details(maze_id)
        if user_maze:
            user_maze = user_maze[0]
            user_maze.maze_layout = maze_layout
            user_maze.maze_wall_positioning = coordinates_for_walls
            user_maze.save()
            from ..question.QuestionModel import Question
            Question.objects.filter(maze_id=maze_id).delete()
            from ..assets.SharedData import SharedData
            SharedData.add_questions = False
            return maze_id
        else:
            print("Maze not found")
    except Exception as e:
        print("Maze saving failed:", str(e))


