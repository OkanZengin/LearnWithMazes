def is_played():
    for row in range(10):
        for col in range(4):
            if col == 0:
                from ..database.PlayMazeEasyLevels import EasyMazes
                from ..assets.SharedData import SharedData
                maze_id = EasyMazes.sorted_easy_mazes[row].maze_id
                from ..database.GetMyRating import get_my_rating
                SharedData.user_s_played_maze = get_my_rating(maze_id)
                if SharedData.user_s_played_maze is None:
                    SharedData.user_played[row][col] = 0
                else:
                    SharedData.user_played[row][col] = 1
            elif col == 1:
                from ..database.PlayMazeMediumLevels import MediumMazes
                from ..assets.SharedData import SharedData
                maze_id = MediumMazes.sorted_medium_mazes[row].maze_id
                from ..database.GetMyRating import get_my_rating
                SharedData.user_s_played_maze = get_my_rating(maze_id)
                if SharedData.user_s_played_maze is None:
                    SharedData.user_played[row][col] = 0
                else:
                    SharedData.user_played[row][col] = 1
            elif col == 2:
                from ..database.PlayMazeHardLevels import HardMazes
                from ..assets.SharedData import SharedData
                maze_id = HardMazes.sorted_hard_mazes[row].maze_id
                from ..database.GetMyRating import get_my_rating
                SharedData.user_s_played_maze = get_my_rating(maze_id)
                if SharedData.user_s_played_maze is None:
                    SharedData.user_played[row][col] = 0
                else:
                    SharedData.user_played[row][col] = 1
            elif col == 3:
                from ..database.PlayMazeExtremeLevels import ExtremeMazes
                maze_id = ExtremeMazes.sorted_extreme_mazes[row].maze_id
                from ..assets.SharedData import SharedData
                from ..database.GetMyRating import get_my_rating
                SharedData.user_s_played_maze = get_my_rating(maze_id)
                if SharedData.user_s_played_maze is None:
                    SharedData.user_played[row][col] = 0
                else:
                    SharedData.user_played[row][col] = 1
