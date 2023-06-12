def get_medium_mazes(sorted_medium_mazes):
    from ..usermaze.UserMazeModel import UserMaze
    query = {"user": "admin", "maze_level": "MEDIUM"}
    result_set = UserMaze.objects.filter(**query)
    sorted_mazes = sorted(result_set, key=lambda maze: len(maze.maze_wall_positioning) if isinstance(maze.maze_wall_positioning, list) else 0)
    sorted_medium_mazes.extend(sorted_mazes)


class MediumMazes:
    sorted_medium_mazes = []
    get_medium_mazes(sorted_medium_mazes)


