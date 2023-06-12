from ..assets.SharedData import SharedData
from ..user.UserModel import User
from ..usermaze.UserMazeModel import UserMaze


def find_mazes_i_played_rated():
    current_username = SharedData.current_username
    user_update = User.objects.get(username=current_username)
    mazes_i_played_and_rated = user_update.mazes_i_played_rated
    maze_ids = []
    if mazes_i_played_and_rated is not None:
        for maze in mazes_i_played_and_rated:
            maze_ids.append(maze["maze_id"])
        mazesiplayedids = []
        for maze_id in maze_ids:
            try:
                maze = UserMaze.objects.exclude(user="admin").get(maze_id=maze_id)
                mazesiplayedids.append(maze)
            except UserMaze.DoesNotExist:
                mazesiplayedids = []
        return mazesiplayedids


class MazesIPlayedRated:
    current_page_value = 0
    mazesiplayedids = find_mazes_i_played_rated()
