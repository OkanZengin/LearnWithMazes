

def a_star_search(self, node_wall_index, grid_size, wall_images_values):
    start_node = (0, 0)
    end_node = (grid_size - 1, grid_size - 1)
    open_list = []
    closed_list = [[None] * grid_size for _ in range(grid_size)]
    g_scores = [[float('inf')] * grid_size for _ in range(grid_size)]
    f_scores = [[float('inf')] * grid_size for _ in
                range(grid_size)]

    g_scores[start_node[0]][start_node[1]] = 0
    f_scores[start_node[0]][start_node[1]] = heuristic(start_node, end_node)

    open_list.append(start_node)
    path = None
    while open_list:
        current_node = get_node_with_lowest_f_score(open_list, f_scores)
        open_list.remove(current_node)
        if current_node == end_node:
            path = reconstruct_path(start_node, end_node, closed_list)
            self.yellow_square_draw.extend(path)
            self.blue_square_draw.append(end_node)
            break

        closed_list.append(current_node)
        x, y = current_node
        if current_node != start_node:
            starting = (0, 0)
            self.blue_square_draw.append(starting)
            self.blue_square_draw.append(current_node)
            self.drawing = True
            self.drawing_yellow = True

        neighbors = get_neighbors(current_node, grid_size, node_wall_index, wall_images_values)
        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            tentative_g_score = g_scores[current_node[0]][current_node[1]] + 1

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g_score >= g_scores[neighbor[0]][neighbor[1]]:
                continue

            g_scores[neighbor[0]][neighbor[1]] = tentative_g_score
            f_scores[neighbor[0]][neighbor[1]] = tentative_g_score + heuristic(neighbor, end_node)
            closed_list[neighbor[0]][neighbor[1]] = {'parent': current_node}

    if path is None:
        self.drawing_unsolvable = True
    return None


def get_node_with_lowest_f_score(open_list, f_scores):
    lowest_f_score = float('inf')
    lowest_node = None
    for node in open_list:
        if f_scores[node[0]][node[1]] < lowest_f_score:
            lowest_f_score = f_scores[node[0]][node[1]]
            lowest_node = node
    return lowest_node


def get_neighbors(node, grid_size, node_wall_index, wall_images_values):
    neighbors = []
    x, y = node
    if 0 <= y < grid_size - 1 and wall_images_values[node_wall_index[x][y]]["E"] == "1":
        if wall_images_values[node_wall_index[x][y + 1]]["W"] == "1":
            neighbors.append((x, y + 1))
    if 0 < y <= grid_size - 1 and wall_images_values[node_wall_index[x][y]]["W"] == "1":
        if wall_images_values[node_wall_index[x][y - 1]]["E"] == "1":
            neighbors.append((x, y - 1))
    if 0 <= x < grid_size - 1 and wall_images_values[node_wall_index[x][y]]["N"] == "1":
        if wall_images_values[node_wall_index[x + 1][y]]["S"] == "1":
            neighbors.append((x + 1, y))
    if 0 < x <= grid_size - 1 and wall_images_values[node_wall_index[x][y]]["S"] == "1":
        if wall_images_values[node_wall_index[x - 1][y]]["N"] == "1":
            neighbors.append((x - 1, y))
    return neighbors


def heuristic(node, end_node):
    return abs(node[0] - end_node[0]) + abs(node[1] - end_node[1])


def reconstruct_path(start_node, end_node, closed_list):
    current_node = end_node
    path = [current_node]
    while current_node != start_node:
        row, col = current_node
        previous_node = closed_list[row][col]['parent']
        path.append(previous_node)
        if previous_node != start_node:
            pass
        current_node = previous_node
    path.reverse()
    return path



