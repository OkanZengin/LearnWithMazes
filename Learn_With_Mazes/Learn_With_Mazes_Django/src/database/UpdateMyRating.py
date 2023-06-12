from ..assets.SharedData import SharedData
from ..user.UserModel import User


def update_my_rating(maze_id):
    try:
        current_username = SharedData.current_username
        user_update = User.objects.get(username=current_username)

        mazes_i_played_and_rated = user_update.mazes_i_played_rated
        if mazes_i_played_and_rated is None:
            mazes_i_played_and_rated = []

        updated = False
        for maze in mazes_i_played_and_rated:
            if maze["maze_id"] == maze_id:
                maze["my_rating"] = SharedData.currently_played_given_star
                updated = True
                break

        if not updated:
            new_data = {"maze_id": maze_id, "my_rating": SharedData.currently_played_given_star}
            mazes_i_played_and_rated.append(new_data)

        User.objects.filter(username=current_username).update(mazes_i_played_rated=mazes_i_played_and_rated)

    except User.DoesNotExist:
        print("User not found")
    except Exception as e:
        print("Failed to update rating:", str(e))
