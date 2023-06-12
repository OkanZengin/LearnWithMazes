def get_extreme_mazes(sorted_extreme_mazes):
    from ..usermaze.UserMazeModel import UserMaze
    query = {"user": "admin", "maze_level": "EXTREME"}
    result_set = UserMaze.objects.filter(**query)
    sorted_mazes = sorted(result_set, key=lambda maze: len(maze.maze_wall_positioning) if isinstance(maze.maze_wall_positioning, list) else 0)
    sorted_extreme_mazes.extend(sorted_mazes)


class ExtremeMazes:
    sorted_extreme_mazes = []
    get_extreme_mazes(sorted_extreme_mazes)


