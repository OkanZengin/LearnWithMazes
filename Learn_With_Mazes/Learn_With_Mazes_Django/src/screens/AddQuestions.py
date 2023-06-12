import pygame
from pygame.locals import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 300


class InputBox:
    def __init__(self, rect):
        self.rect = rect
        self.active = False
        self.text = ""


class AddQuestions:
    def __init__(self, door_count, node_wall_index, coordinates_for_walls):
        self.door_count = door_count
        self.node_wall_index = node_wall_index
        self.wall_coordinates = coordinates_for_walls
        self.input_boxes = []
        self.save_buttons = []
        self.save_texts = []
        self.should_exit = False
        self.question_saved = False
        self.not_all_questions_saved = False
        self.saved_question_count = 0
        self.saved_question = 0

    def create_input_boxes(self):
        box_width = 250
        box_height = 40
        box_spacing = 10
        start_x = 30
        start_y = 30

        for i in range(self.door_count):
            x = start_x
            y = start_y + (i * (box_height + box_spacing))
            question_input_box = InputBox(pygame.Rect(x, y, box_width, box_height))
            question_input_box.name = "Question"
            question_input_box.text = "Question"
            answer_input_box = InputBox(pygame.Rect(x + box_width + box_spacing, y, box_width, box_height))
            answer_input_box.name = "Answer"
            answer_input_box.text = "Answer"
            self.input_boxes.extend([question_input_box, answer_input_box])
            save_button_rect = pygame.Rect(610, 35+(i * 50), 80, 30)
            self.save_buttons.append(save_button_rect)

    def draw(self, screen):
        screen.fill((255, 255, 255))
        for input_box in self.input_boxes:
            color = (200, 200, 200) if input_box.active else (255, 255, 255)
            pygame.draw.rect(screen, color, input_box.rect)
            pygame.draw.rect(screen, (0, 0, 0), input_box.rect, 2)

            font = pygame.font.SysFont(None, 24)
            text_surface = font.render(input_box.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=input_box.rect.center)
            screen.blit(text_surface, text_rect)

        for i, coordinate in enumerate(self.wall_coordinates, start=0):
            x, y = coordinate
            text_surface = font.render(f"({x + 1}, {y + 1})", True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (550, (i * 50) + 40)
            screen.blit(text_surface, text_rect.topleft)

        for save_button_rect in self.save_buttons:
            pygame.draw.rect(screen, (200, 200, 200), save_button_rect)
            save_font = pygame.font.SysFont(None, 25)
            save_text = save_font.render("Save", True, (0, 0, 0))
            save_text_rect = save_text.get_rect(center=save_button_rect.center)
            screen.blit(save_text, save_text_rect)

        done_button_rect = pygame.Rect(325, 60 * self.door_count + 5, 80, 30)
        pygame.draw.rect(screen, (200, 200, 200), done_button_rect)
        done_font = pygame.font.SysFont(None, 25)
        done_text = done_font.render("DONE", True, (0, 0, 0))
        done_text_rect = done_text.get_rect(center=done_button_rect.center)
        screen.blit(done_text, done_text_rect)

        if self.question_saved:
            if self.saved_question == 1:
                suffix = "st"
            elif self.saved_question == 2:
                suffix = "nd"
            elif self.saved_question == 3:
                suffix = "rd"
            else:
                suffix = "th"
            font = pygame.font.Font(None, 24)
            text = font.render(f"{self.saved_question}{suffix} Question Saved", True, (255, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (550, 60 * self.door_count + 25)
            screen.blit(text, text_rect)
            pygame.display.update()
            delay = 1000
            pygame.time.wait(delay)
            self.question_saved = False
        if self.not_all_questions_saved:
            font = pygame.font.Font(None, 24)
            text = font.render("Not All Question Saved", True, (255, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (550, 60 * self.door_count + 25)
            screen.blit(text, text_rect)
            pygame.display.update()
            delay = 1000
            pygame.time.wait(delay)
            self.not_all_questions_saved = False
        from ..assets.SharedData import SharedData
        if SharedData.questions_added:
            font = pygame.font.Font(None, 18)
            text = font.render("Need to Save Questions First", True, (255, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (550, 60 * self.door_count + 25)
            screen.blit(text, text_rect)
            pygame.display.update()
            delay = 1000
            pygame.time.wait(delay)
            SharedData.questions_added = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for input_box in self.input_boxes:
                if input_box.rect.collidepoint(event.pos):
                    input_box.active = True
                    input_box.text = ""
                else:
                    input_box.active = False
            done_button_rect = pygame.Rect(325, 60 * self.door_count + 5, 70, 30)
            if done_button_rect.collidepoint(event.pos):
                if self.saved_question < self.door_count:
                    self.not_all_questions_saved = True
                else:
                    self.should_exit = True
                    from ..assets.SharedData import SharedData
                    SharedData.maze_saved_questions_added = True
                    SharedData.add_questions = True
                return

            for i, save_button_rect in enumerate(self.save_buttons):
                if save_button_rect.collidepoint(event.pos):
                    input_box_index = i * 2
                    question_text = self.input_boxes[input_box_index].text
                    answer_text = self.input_boxes[input_box_index + 1].text
                    self.save_texts.append((question_text, answer_text))
                    self.saved_question = i+1
                    self.question_saved = True
                    from ..question.QuestionModel import Question
                    from ..assets.SharedData import SharedData
                    maze_id = SharedData.current_maze_id
                    question = question_text
                    answer = answer_text
                    door_position = self.wall_coordinates[i]
                    try:
                        Question.objects.create(maze_id=maze_id, question=question, answer=answer,
                                                question_position=door_position)
                        self.saved_question_count += 1
                    except Exception as e:
                        print("Question save failed", str(e))
        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                active_index = None
                for i, input_box in enumerate(self.input_boxes):
                    if input_box.active:
                        active_index = i
                        input_box.active = False
                        break

                if active_index is not None:
                    next_index = (active_index + 1) % len(self.input_boxes)
                    self.input_boxes[next_index].active = True
                    self.input_boxes[next_index].text = ""
                return

            for input_box in self.input_boxes:
                if input_box.active:
                    if event.key == K_BACKSPACE:
                        input_box.text = input_box.text[:-1]
                        pygame.key.set_repeat(200, 50)
                    elif event.key == K_TAB:
                        continue
                    else:
                        input_box.text += event.unicode

    def run(self):
        pygame.init()
        screen_title = "Add Questions"
        screen = pygame.display.set_mode((SCREEN_WIDTH, (60 * self.door_count) + 50))
        pygame.display.set_caption(screen_title)
        clock = pygame.time.Clock()

        self.create_input_boxes()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    from ..assets.SharedData import SharedData
                    SharedData.questions_added = True
                elif self.should_exit:
                    pygame.quit()
                    return

                self.handle_event(event)

            self.draw(screen)

            pygame.display.flip()
            clock.tick(60)

