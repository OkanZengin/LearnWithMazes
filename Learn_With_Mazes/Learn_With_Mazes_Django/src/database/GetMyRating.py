from ..user.UserModel import User
from ..assets.SharedData import SharedData


def get_my_rating(maze_id):
    user = User.objects.get(username=SharedData.current_username)
    mazes_i_played_and_rated = user.mazes_i_played_rated
    if mazes_i_played_and_rated is not None:
        for maze in mazes_i_played_and_rated:
            if maze["maze_id"] == maze_id:
                return maze["my_rating"]
    else:
        pass
    return None
