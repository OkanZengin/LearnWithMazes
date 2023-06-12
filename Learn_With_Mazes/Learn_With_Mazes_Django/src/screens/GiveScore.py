import pygame
from pygame.locals import *
import math

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 100
STAR_SIZE = 30
STAR_MARGIN = 10


class ScoreScreen:
    def __init__(self, maze_id):
        self.stars = []
        self.selected_stars = 0
        self.should_exit = False
        self.hover_color = (255, 255, 0)  # Yellow
        self.default_color = (255, 255, 255)  # White
        self.maze_id = maze_id

    def handle_event(self, event):
        if event.type == QUIT:
            self.should_exit = True
        elif event.type == MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            for star in self.stars:
                if star["rect"].collidepoint(mouse_pos):
                    star["color"] = self.hover_color
                else:
                    star["color"] = self.default_color
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i, star in enumerate(self.stars):
                if star["rect"].collidepoint(mouse_pos):
                    self.selected_stars = i + 1
                    from ..assets.SharedData import SharedData
                    from ..database.UpdateMazeRating import update_maze_rating
                    from ..database.UpdateMyRating import update_my_rating
                    from ..database.FindMazesiPlayedRated import MazesIPlayedRated
                    from ..database.FindMazesiPlayedRated import find_mazes_i_played_rated
                    from ..database.MyProfileMazes import MyProfileMazes
                    from ..database.MyProfileMazes import get_my_mazes
                    from ..database.FindAllMazes import FindAllMazes
                    from ..database.FindAllMazes import find_all_mazes
                    SharedData.currently_played_given_star = self.selected_stars
                    update_maze_rating(self.maze_id)
                    update_my_rating(self.maze_id)
                    MazesIPlayedRated.mazesiplayedids = []
                    MazesIPlayedRated.mazesiplayedids = find_mazes_i_played_rated()
                    MyProfileMazes.sorted_my_mazes = []
                    MyProfileMazes.sorted_my_mazes = get_my_mazes(MyProfileMazes.my_sorted_mazes)
                    FindAllMazes.sorted_all_mazes = []
                    FindAllMazes.sorted_all_mazes = find_all_mazes(FindAllMazes.all_sorted_mazes)
                    print("Clicked star:", i + 1)  # Print the clicked star
                    self.should_exit = True
                    break

    def draw(self, screen):
        screen.fill((255, 255, 255))  # White background

        # Calculate the x-coordinate for the leftmost star
        stars_total_width = (STAR_SIZE + STAR_MARGIN) * 5 - STAR_MARGIN
        start_x = (SCREEN_WIDTH - stars_total_width) // 2

        # Draw the stars
        self.stars = []
        for i in range(5):
            star_x = start_x + (STAR_SIZE + STAR_MARGIN) * i
            star_y = (SCREEN_HEIGHT - STAR_SIZE) // 2
            star_rect = pygame.Rect(star_x, star_y, STAR_SIZE, STAR_SIZE)
            star_color = self.hover_color if star_rect.collidepoint(pygame.mouse.get_pos()) else self.default_color
            self.stars.append({"rect": star_rect, "color": star_color})

            # Draw star polygon
            pygame.draw.polygon(screen, star_color, create_star_points(
                (star_x + STAR_SIZE // 2, star_y + STAR_SIZE // 2),
                STAR_SIZE // 2,
                STAR_SIZE // 4,
                5
            ))
            pygame.draw.polygon(screen, (0, 0, 0), create_star_points(
                (star_x + STAR_SIZE // 2, star_y + STAR_SIZE // 2),
                STAR_SIZE // 2,
                STAR_SIZE // 4,
                5
            ), 2)

            # Draw small circle in the middle
            pygame.draw.circle(screen, star_color, (star_x + STAR_SIZE // 2, star_y + STAR_SIZE // 2),
                               STAR_SIZE // 3.45)

        pygame.display.flip()

    def run(self):
        pygame.init()
        screen_title = "Give Score"
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(screen_title)
        clock = pygame.time.Clock()
        while not self.should_exit:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


def create_star_points(center, outer_radius, inner_radius, num_points):
    angle = 2 * math.pi / num_points
    points = []
    for i in range(num_points * 2):
        radius = outer_radius if i % 2 == 0 else inner_radius
        x = center[0] + radius * math.sin(i * angle)
        y = center[1] + radius * math.cos(i * angle)
        points.append((x, y))
    return points

