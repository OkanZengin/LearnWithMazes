def find_all_mazes(all_sorted_mazes):
    from ..usermaze.UserMazeModel import UserMaze
    result_set = UserMaze.objects.all()
    all_sorted_mazes = []
    for document in result_set:
        username = document.user
        if username != "admin":
            all_sorted_mazes.append(document)
    return all_sorted_mazes


class FindAllMazes:
    current_page_value = 0
    all_sorted_mazes = []
    sorted_all_mazes = find_all_mazes(all_sorted_mazes)

