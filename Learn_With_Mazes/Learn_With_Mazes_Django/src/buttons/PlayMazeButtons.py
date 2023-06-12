import arcade
from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.CreateMazeAssets import wall_images_values
from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.SharedData import SharedData
from Learn_With_Mazes.Learn_With_Mazes_Django.src.functions.AStarSearchAlgorithm import a_star_search


def on_mouse_press(self, x, y, button):
    if button == arcade.MOUSE_BUTTON_LEFT:
        go_back_button_width = 100
        go_back_button_height = 25
        go_back_button_x = 10
        go_back_button_y = self.window.height - go_back_button_height - 10

        if go_back_button_x < x < go_back_button_x + go_back_button_width and \
                go_back_button_y < y < go_back_button_y + go_back_button_height:
            from ..screens.MainMenu import MainMenu
            main_menu = MainMenu()
            main_menu.window.show_view(main_menu)
        if 465 <= x <= 595 and 565.5 <= y <= 595:
            a_star_search(self, SharedData.current_node_wall_index, len(SharedData.current_node_wall_index),
                          wall_images_values)
        if 245 <= x <= 405 and 565.5 <= y <= 595:
            self.drawing_yellow = False


def on_key_press(self, key, modifiers):
    from ..assets.SharedData import SharedData
    maze_id = self.maze_id
    if key == arcade.key.UP:
        if is_moving_north_valid(SharedData.current_node_wall_index, self.current_row, self.current_column):
            self.current_row += 1
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 15:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 16:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if self.current_row == self.current_column == len(SharedData.current_node_wall_index) - 1:
                self.maze_solved = True
                if self.creator != "admin":
                    from ..screens.GiveScore import ScoreScreen
                    give_score = ScoreScreen(maze_id)
                    give_score.run()
                else:
                    from ..database.UpdateMyRating import update_my_rating
                    update_my_rating(maze_id)
            else:
                pass
    elif key == arcade.key.DOWN:
        if is_moving_south_valid(SharedData.current_node_wall_index, self.current_row, self.current_column):
            self.current_row -= 1
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 15:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 16:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if self.current_row == self.current_column == len(SharedData.current_node_wall_index) - 1:
                self.maze_solved = True
                if self.creator != "admin":
                    from ..screens.GiveScore import ScoreScreen
                    give_score = ScoreScreen(maze_id)
                    give_score.run()
                else:
                    from ..database.UpdateMyRating import update_my_rating
                    update_my_rating(maze_id)
            else:
                pass
    elif key == arcade.key.LEFT:
        if is_moving_west_valid(SharedData.current_node_wall_index, self.current_row, self.current_column):
            self.current_column -= 1
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 15:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 16:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if self.current_row == self.current_column == len(SharedData.current_node_wall_index) - 1:
                self.maze_solved = True
                if self.creator != "admin":
                    from ..screens.GiveScore import ScoreScreen
                    give_score = ScoreScreen(maze_id)
                    give_score.run()
                else:
                    from ..database.UpdateMyRating import update_my_rating
                    update_my_rating(maze_id)
            else:
                pass
    elif key == arcade.key.RIGHT:
        if is_moving_east_valid(SharedData.current_node_wall_index, self.current_row, self.current_column):
            self.current_column += 1
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 15:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if SharedData.current_node_wall_index[self.current_row][self.current_column] == 16:
                wall_position = "({}, {})".format(self.current_row, self.current_column)
                question, answer = get_the_wall_question(maze_id, wall_position)
                from ..screens.AnswerQuestion import AnswerQuestion
                answer_questions = AnswerQuestion(question, answer)
                answer_questions.run()
                if SharedData.answer_correct is False:
                    self.current_row = 0
                    self.current_column = 0
                    SharedData.answer_correct = None
                else:
                    SharedData.answer_correct = None
            else:
                pass
            if self.current_row == self.current_column == len(SharedData.current_node_wall_index) - 1:
                self.maze_solved = True
                if self.creator != "admin":
                    from ..screens.GiveScore import ScoreScreen
                    give_score = ScoreScreen(maze_id)
                    give_score.run()
                else:
                    from ..database.UpdateMyRating import update_my_rating
                    update_my_rating(maze_id)
            else:
                pass


def is_moving_north_valid(node_wall_index, current_row, current_column):
    if 0 <= current_row < len(node_wall_index)-1 \
            and wall_images_values[node_wall_index[current_row][current_column]]["N"] == "1" \
            and wall_images_values[node_wall_index[current_row + 1][current_column]]["S"] == "1":
        return True
    else:
        return False


def is_moving_east_valid(node_wall_index, current_row, current_column):
    if 0 <= current_column < len(node_wall_index)-1 \
            and wall_images_values[node_wall_index[current_row][current_column]]["E"] == "1" \
            and wall_images_values[node_wall_index[current_row][current_column + 1]]["W"] == "1":
        return True
    else:
        return False


def is_moving_south_valid(node_wall_index, current_row, current_column):
    if 0 < current_row <= len(node_wall_index) \
            and wall_images_values[node_wall_index[current_row][current_column]]["S"] == "1" \
            and wall_images_values[node_wall_index[current_row - 1][current_column]]["N"] == "1":
        return True
    elif current_row == 0:
        return False
    else:
        return False


def is_moving_west_valid(node_wall_index, current_row, current_column):
    if 0 < current_column <= len(node_wall_index) \
            and wall_images_values[node_wall_index[current_row][current_column]]["W"] == "1" \
            and wall_images_values[node_wall_index[current_row][current_column - 1]]["E"] == "1":
        return True
    elif current_column == 0:
        return False
    else:
        return False


def get_the_wall_question(maze_id, wall_position):
    from ..question.QuestionModel import Question
    query = {"maze_id": f"{maze_id}", "question_position": f"{wall_position}"}
    questionobj = Question.objects.filter(**query).first()
    if questionobj:
        return questionobj.question, questionobj.answer
    else:
        return None, None
