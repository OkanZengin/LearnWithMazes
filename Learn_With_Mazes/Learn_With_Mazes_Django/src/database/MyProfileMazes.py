from ..assets.SharedData import SharedData
from ..usermaze.UserMazeModel import UserMaze


def get_my_mazes(sorted_mazes):
    query = {"user": SharedData.current_username}
    result_set = UserMaze.objects.filter(**query)
    sorted_mazes = sorted(result_set, key=lambda maze: ('EXTREME', 'HARD', 'MEDIUM', 'EASY').index(maze.maze_level))
    return sorted_mazes


class MyProfileMazes:
    current_page_value = 0
    my_sorted_mazes = []
    sorted_my_mazes = get_my_mazes(my_sorted_mazes)

