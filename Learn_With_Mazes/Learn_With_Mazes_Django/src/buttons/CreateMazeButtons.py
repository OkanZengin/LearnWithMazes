from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.AStarSearchAlgorithm import a_star_search
from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import *
from Learn_With_Mazes.Learn_With_Mazes_Django.src.usermaze.UserMazeModel import UserMaze


def on_mouse_press(self, x, y, button):
    for button_name, (button_x, button_y) in buttons.items():
        if button_x - BUTTON_WIDTH // 2 <= x <= button_x + BUTTON_WIDTH // 2 and \
                button_y - BUTTON_HEIGHT // 2 <= y <= button_y + BUTTON_HEIGHT // 2:
            if button_name == "Go-Back":
                from ..assets.SharedData import SharedData
                if SharedData.maze_saved_questions_added:
                    from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.MainMenu import MainMenu
                    main_menu = MainMenu()
                    main_menu.window.show_view(main_menu)
                else:
                    self.maze_saved_questions_not_added = True
            elif button_name in ["EASY", "MEDIUM", "HARD", "EXTREME"]:
                if button_name == "EASY":
                    set_grid_size(self, 5)
                    self.drawing = False
                    self.drawing_unsolvable = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.save_first = False
                    self.check_for_solution = False
                    self.blue_square_draw = []
                    self.yellow_square_draw = []
                    self.maze_level = "EASY"
                    self.min_door = 2
                    self.max_door = 5
                elif button_name == "MEDIUM":
                    set_grid_size(self, 8)
                    self.drawing = False
                    self.drawing_unsolvable = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.save_first = False
                    self.check_for_solution = False
                    self.blue_square_draw = []
                    self.yellow_square_draw = []
                    self.maze_level = "MEDIUM"
                    self.min_door = 3
                    self.max_door = 6
                elif button_name == "HARD":
                    set_grid_size(self, 10)
                    self.drawing = False
                    self.drawing_unsolvable = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.save_first = False
                    self.check_for_solution = False
                    self.blue_square_draw = []
                    self.yellow_square_draw = []
                    self.maze_level = "HARD"
                    self.min_door = 4
                    self.max_door = 8
                elif button_name == "EXTREME":
                    set_grid_size(self, 15)
                    self.drawing = False
                    self.drawing_unsolvable = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.save_first = False
                    self.check_for_solution = False
                    self.blue_square_draw = []
                    self.yellow_square_draw = []
                    self.maze_level = "EXTREME"
                    self.min_door = 5
                    self.max_door = 10
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
                self.check_for_solution = False
                self.save_first = False
                self.not_enough_doors = False
                self.too_many_doors = False
            elif button_name == "Clear":
                for row in range(self.grid_size):
                    for column in range(self.grid_size):
                        self.node_wall_index[row][column] = 0
                self.drawing = False
                self.drawing_unsolvable = False
                self.not_enough_doors = False
                self.too_many_doors = False
                self.save_first = False
                self.check_for_solution = False
                self.blue_square_draw = []
                self.yellow_square_draw = []
            elif button_name == "Add Q & A":
                self.check_for_solution = False
                self.maze_saved_questions_not_added = False
                if self.is_maze_saved:
                    count = check_door_count(self)
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    if count < self.min_door:
                        self.not_enough_doors = True
                    elif count > self.max_door:
                        self.too_many_doors = True
                    elif self.min_door <= count <= self.max_door:
                        from Learn_With_Mazes.Learn_With_Mazes_Django.src.screens.AddQuestions import AddQuestions
                        add_questions_view = AddQuestions(self.door_count, self.node_wall_index,
                                                          self.coordinates_for_doors)
                        add_questions_view.run()
                        self.is_maze_saved = False
                else:
                    self.save_first = True
            elif button_name == "SAVE":
                self.save_first = False
                door_count = check_door_count(self)
                if door_count < self.min_door:
                    self.not_enough_doors = True
                if door_count > self.max_door:
                    self.too_many_doors = True
                elif self.min_door <= door_count <= self.max_door and self.drawing_yellow is False:
                    self.check_for_solution = True
                elif self.min_door <= door_count <= self.max_door and self.drawing_yellow:
                    self.too_many_doors = False
                    self.not_enough_doors = False
                    from ..assets.SharedData import SharedData
                    username = SharedData.current_username
                    self.maze_id = save_maze(username, self.maze_level, self.node_wall_index, self.coordinates_for_doors)
                    SharedData.current_maze_id = self.maze_id
                    self.is_maze_saved = True
                    SharedData.maze_saved_questions_added = False

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
                    self.save_first = False
                    self.check_for_solution = False
                    self.blue_square_draw = []
                    self.yellow_square_draw = []
                    break
                elif button == arcade.MOUSE_BUTTON_RIGHT and self.wall_buttons_visible is False:
                    wall_index = self.node_wall_index[row][column]
                    self.node_wall_index[row][column] = (wall_index - 1) % len(wall_images)
                    self.drawing_unsolvable = False
                    self.drawing = False
                    self.not_enough_doors = False
                    self.too_many_doors = False
                    self.save_first = False
                    self.check_for_solution = False
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
                    self.save_first = False
                    self.check_for_solution = False
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


def check_door_count(self):
    self.door_count = 0
    self.coordinates_for_doors = []
    for row in range(self.grid_size):
        for column in range(self.grid_size):
            if self.node_wall_index[row][column] == 15 or \
                    self.node_wall_index[row][column] == 16:
                coordinate = (row, column)
                self.coordinates_for_doors.append(coordinate)
                self.door_count += 1

    return self.door_count


def save_maze(username, maze_level, maze_layout, coordinates_for_walls):
    from ..functions.GenerateId import generate_random_string
    generated_maze_id = generate_random_string(24)
    try:
        user_maze = UserMaze.objects.create(
            maze_id=generated_maze_id,
            user=username,
            maze_level=maze_level,
            maze_layout=maze_layout,
            maze_wall_positioning=coordinates_for_walls
        )

        maze_id = generated_maze_id
        return maze_id
    except Exception as e:
        print("Maze saving failed:", str(e))



