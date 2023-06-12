def get_hard_mazes(sorted_hard_mazes):
    from ..usermaze.UserMazeModel import UserMaze
    query = {"user": "admin", "maze_level": "HARD"}
    result_set = UserMaze.objects.filter(**query)
    sorted_mazes = sorted(result_set, key=lambda maze: len(maze.maze_wall_positioning) if isinstance(maze.maze_wall_positioning, list) else 0)
    sorted_hard_mazes.extend(sorted_mazes)


class HardMazes:
    sorted_hard_mazes = []
    get_hard_mazes(sorted_hard_mazes)


