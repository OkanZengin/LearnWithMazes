class SharedData:
    current_username = None
    signed_in_flag = False
    signed_up_flag = False
    maze_id_exists = True
    current_maze_id = None
    current_list = 0
    current_node_wall_index = []
    answer_correct = None
    question_saved = False
    currently_played_maze_id = None
    currently_played_maze_rating = None
    currently_played_maze_rate_count = None
    currently_played_maze_my_rate = None
    currently_played_maze_player_id = None
    currently_played_given_star = 0
    order_by_user = False
    order_by_level = False
    order_by_rating = False
    order_by_rate_count = False
    questions_added = False
    maze_saved_questions_added = True
    user_played = [[0] * 4 for _ in range(10)]
    user_s_played_maze = None
    add_questions = True

