import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50


class InputBox:
    def __init__(self, rect, placeholder):
        self.rect = rect
        self.active = False
        self.text = ""
        self.placeholder = placeholder

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == KEYDOWN:
            if self.active and event.key and event.key != K_TAB:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                    pygame.key.set_repeat(200, 50)
                else:
                    self.text += event.unicode

    def draw(self, screen):
        color = (255, 255, 255) if not self.active else (200, 200, 200)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        font = pygame.font.SysFont(None, 24)
        if self.placeholder == "Password":
            text_to_display = '*' * len(self.text) if self.text else self.placeholder
        else:
            text_to_display = self.text if self.text else self.placeholder
        text_surface = font.render(text_to_display, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


class SignInSignUp:
    def __init__(self):
        self.input_boxes = []
        self.create_input_boxes()
        self.sign_in_rect = pygame.Rect(SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + BUTTON_HEIGHT + 20,
                                        BUTTON_WIDTH, BUTTON_HEIGHT)
        self.sign_up_rect = pygame.Rect(SCREEN_WIDTH / 2 - BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + BUTTON_HEIGHT * 2 + 40,
                                        BUTTON_WIDTH, BUTTON_HEIGHT)

        self.should_exit = False
        self.active = False

    def create_input_boxes(self):
        box_width = 300
        box_height = 40
        box_spacing = 20
        start_x = SCREEN_WIDTH / 2 - box_width / 2
        start_y = SCREEN_HEIGHT / 2 - (box_height + box_spacing) * 2

        username_box = InputBox(pygame.Rect(start_x, start_y, box_width, box_height), "Username")
        password_box = InputBox(pygame.Rect(start_x, start_y + box_height + box_spacing, box_width, box_height),
                                "Password")
        self.input_boxes.extend([username_box, password_box])

    def handle_event(self, event):
        from ..user.UserModel import User
        for input_box in self.input_boxes:
            input_box.handle_event(event)

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for input_box in self.input_boxes:
                if input_box.rect.collidepoint(event.pos):
                    if input_box.text == "Username" or input_box.text == "Password":
                        input_box.text = ""

            if self.sign_in_rect.collidepoint(event.pos):
                username = self.input_boxes[0].text
                password = self.input_boxes[1].text
                try:
                    from ..assets.SharedData import SharedData
                    user = User.objects.get(username=username, password=password)
                    self.should_exit = True
                    SharedData.current_username = user.username
                    SharedData.signed_in_flag = True
                except User.DoesNotExist:
                    SharedData.signed_in_flag = None

            if self.sign_up_rect.collidepoint(event.pos):
                from ..assets.SharedData import SharedData
                username = self.input_boxes[0].text
                password = self.input_boxes[1].text

                try:
                    User.objects.create(username=username, password=password)
                    self.should_exit = True
                    SharedData.current_username = username
                    SharedData.signed_up_flag = True
                    SharedData.signed_in_flag = True
                except Exception as e:
                    SharedData.signed_up_flag = None

        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                if self.input_boxes[0].active:
                    self.input_boxes[0].active = False
                    self.input_boxes[1].active = True

    def draw(self, screen):
        from ..assets.SharedData import SharedData
        screen.fill((255, 255, 255))

        for input_box in self.input_boxes:
            input_box.draw(screen)

        pygame.draw.rect(screen, (200, 200, 200), self.sign_in_rect)
        sign_in_font = pygame.font.SysFont(None, 24)
        sign_in_text = sign_in_font.render("Sign In", True, (0, 0, 0))
        sign_in_text_rect = sign_in_text.get_rect(center=self.sign_in_rect.center)
        screen.blit(sign_in_text, sign_in_text_rect)

        pygame.draw.rect(screen, (200, 200, 200), self.sign_up_rect)
        sign_up_font = pygame.font.SysFont(None, 24)
        sign_up_text = sign_up_font.render("Sign Up", True, (0, 0, 0))
        sign_up_text_rect = sign_up_text.get_rect(center=self.sign_up_rect.center)
        screen.blit(sign_up_text, sign_up_text_rect)
        if SharedData.signed_up_flag is False and SharedData.signed_in_flag:
            font = pygame.font.Font(None, 36)  # Choose the font and size
            text = font.render("Sign-in successfull", True, (255, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (200, 225)
            screen.blit(text, text_rect)
        elif SharedData.signed_in_flag is None:
            font = pygame.font.Font(None, 36)  # Choose the font and size
            text = font.render("Sign-in failed", True, (255, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (200, 225)
            screen.blit(text, text_rect)
        if SharedData.signed_up_flag:
            font = pygame.font.Font(None, 36)  # Choose the font and size
            text = font.render("Sign-up successfull", True, (255, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (200, 225)
            screen.blit(text, text_rect)
        elif SharedData.signed_up_flag is None:
            font = pygame.font.Font(None, 36)  # Choose the font and size
            text = font.render("Sign-up failed", True, (255, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (200, 225)
            screen.blit(text, text_rect)

    def run(self):
        pygame.init()
        screen_title = "Sign-in / Sign-up"
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(screen_title)
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or self.should_exit:
                    delay = 1000
                    pygame.time.wait(delay)
                    pygame.quit()
                    return
                self.handle_event(event)
            self.draw(screen)
            pygame.display.flip()
            clock.tick(60)
