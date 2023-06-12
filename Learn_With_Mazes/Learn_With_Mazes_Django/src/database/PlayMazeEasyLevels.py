def get_easy_mazes(sorted_easy_mazes):
    from ..usermaze.UserMazeModel import UserMaze
    query = {"user": "admin", "maze_level": "EASY"}
    result_set = UserMaze.objects.filter(**query)
    sorted_mazes = sorted(result_set, key=lambda maze: len(maze.maze_wall_positioning) if isinstance(maze.maze_wall_positioning, list) else 0)
    sorted_easy_mazes.extend(sorted_mazes)


class EasyMazes:
    sorted_easy_mazes = []
    get_easy_mazes(sorted_easy_mazes)


