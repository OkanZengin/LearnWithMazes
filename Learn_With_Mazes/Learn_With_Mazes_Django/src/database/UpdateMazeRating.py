def update_maze_rating(maze_id):
    from ..database.FindMazeDetails import find_maze_details
    from ..assets.SharedData import SharedData
    from ..usermaze.UserMazeModel import UserMaze
    maze_details = find_maze_details(maze_id)
    maze_rating = maze_details[0].rating
    maze_rate_count = maze_details[0].rate_count
    previous_rating_total = maze_rating * maze_rate_count
    new_rating_calculation = (previous_rating_total + SharedData.currently_played_given_star) / (maze_rate_count + 1)
    new_rating = new_rating_calculation
    user_maze = UserMaze.objects.get(maze_id=maze_id)
    user_maze.rating = new_rating
    user_maze.rate_count = maze_rate_count + 1
    user_maze.save()
