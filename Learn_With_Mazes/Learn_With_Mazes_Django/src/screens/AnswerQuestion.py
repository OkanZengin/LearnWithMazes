import pygame
from pygame.locals import *

from Learn_With_Mazes.Learn_With_Mazes_Django.src.assets.SharedData import SharedData

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50


class InputBox:
    def __init__(self, rect, placeholder):
        self.rect = rect
        self.active = False
        self.text = ""
        self.placeholder = placeholder
        self.show_text = True

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == KEYDOWN:
            if self.active:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        color = (255, 255, 255) if not self.active else (200, 200, 200)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(self.text if self.show_text else self.placeholder, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class AnswerQuestion:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.question_rect = pygame.Rect(25, 30, 250, 40)
        self.answer_box = InputBox(pygame.Rect(25, 80, 250, 40), "Enter Answer")
        self.answer_box.show_text = True
        self.check_rect = pygame.Rect(25, 130, 250, 40)
        self.should_exit = False

    def handle_event(self, event):
        self.answer_box.handle_event(event)

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.check_rect.collidepoint(event.pos):
                self.answer_box.show_text = False
                input_text = self.answer_box.text
                if input_text == self.answer:
                    self.should_exit = True
                    SharedData.answer_correct = True
                else:
                    self.should_exit = True
                    SharedData.answer_correct = False

    def draw(self, screen):
        screen.fill((255, 255, 255))
        color = (255, 255, 255)

        pygame.draw.rect(screen, color, self.question_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.question_rect, 2)
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(self.question, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.question_rect.center)
        screen.blit(text_surface, text_rect)

        self.answer_box.draw(screen)

        pygame.draw.rect(screen, (200, 200, 200), self.check_rect)
        check_font = pygame.font.SysFont(None, 24)
        check_text = check_font.render("CHECK", True, (0, 0, 0))
        check_text_rect = check_text.get_rect(center=self.check_rect.center)
        screen.blit(check_text, check_text_rect)

        if self.answer_box.text == "":
            placeholder_font = pygame.font.SysFont(None, 24)
            placeholder_text = placeholder_font.render(self.answer_box.placeholder, True, (150, 150, 150))
            placeholder_rect = placeholder_text.get_rect(center=self.answer_box.rect.center)
            screen.blit(placeholder_text, placeholder_rect)

    def run(self):
        pygame.init()
        screen_title = "Answer Question"
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        pygame.display.set_caption(screen_title)
        while True:
            for event in pygame.event.get():
                if self.should_exit:
                    pygame.quit()
                    return
                self.handle_event(event)
            self.draw(screen)
            pygame.display.flip()
            clock.tick(60)


def main():
    question_screen = AnswerQuestion()
    question_screen.run()


if __name__ == '__main__':
    main()
