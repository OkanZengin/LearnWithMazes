def find_maze_details(maze_id):
    maze = []
    from ..usermaze.UserMazeModel import UserMaze
    query = {"maze_id": f"{maze_id}"}
    maze = UserMaze.objects.filter(**query)
    return maze
