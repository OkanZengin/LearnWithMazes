import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 28
GRID_SIZE = 5
BUTTON_PADDING = 10
WALL_BUTTON_SIZE = 40
WALL_BUTTON_PADDING = 5
BUTTON_COLOR = arcade.color.GRAY
BUTTON_TEXT_COLOR = arcade.color.WHITE
maze_background = arcade.load_texture("images/maze_background.png")

wall_images = {
    "E_Wall": arcade.load_texture("images/EWall.png"),
    "R_Wall": arcade.load_texture("images/RWall.png"),
    "T_Wall": arcade.load_texture("images/TWall.png"),
    "L_Wall": arcade.load_texture("images/LWall.png"),
    "B_Wall": arcade.load_texture("images/BWall.png"),
    "RT_Wall": arcade.load_texture("images/RTWall.png"),
    "LT_Wall": arcade.load_texture("images/LTWall.png"),
    "LB_Wall": arcade.load_texture("images/LBWall.png"),
    "RB_Wall": arcade.load_texture("images/RBWall.png"),
    "RL_Wall": arcade.load_texture("images/RLWall.png"),
    "TB_Wall": arcade.load_texture("images/TBWall.png"),
    "RLT_Wall": arcade.load_texture("images/RLTWall.png"),
    "LTB_Wall": arcade.load_texture("images/LTBWall.png"),
    "RLB_Wall": arcade.load_texture("images/RLBWall.png"),
    "RTB_Wall": arcade.load_texture("images/RTBWall.png"),
    "RL_Door_Wall": arcade.load_texture("images/RL_Door.png"),
    "TB_Door_Wall": arcade.load_texture("images/TB_Door.png"),
}

wall_images_values = [
    {"S": "1", "E": "1", "N": "1", "W": "1"},  # "E_Wall_Values":
    {"S": "1", "E": "0", "N": "1", "W": "1"},  # "R_Wall_Values":
    {"S": "1", "E": "1", "N": "0", "W": "1"},  # "T_Wall_Values":
    {"S": "1", "E": "1", "N": "1", "W": "0"},  # "L_Wall_Values":
    {"S": "0", "E": "1", "N": "1", "W": "1"},  # "B_Wall_Values":
    {"S": "1", "E": "0", "N": "0", "W": "1"},  # "RT_Wall_Values":
    {"S": "1", "E": "1", "N": "0", "W": "0"},  # "LT_Wall_Values":
    {"S": "0", "E": "1", "N": "1", "W": "0"},  # "LB_Wall_Values":
    {"S": "0", "E": "0", "N": "1", "W": "1"},  # "RB_Wall_Values":
    {"S": "1", "E": "0", "N": "1", "W": "0"},  # "RL_Wall_Values":
    {"S": "0", "E": "1", "N": "0", "W": "1"},  # "TB_Wall_Values":
    {"S": "1", "E": "0", "N": "0", "W": "0"},  # "RLT_Wall_Values":
    {"S": "0", "E": "1", "N": "0", "W": "0"},  # "LTB_Wall_Values":
    {"S": "0", "E": "0", "N": "1", "W": "0"},  # "RLB_Wall_Values":
    {"S": "0", "E": "0", "N": "0", "W": "1"},  # "RTB_Wall_Values":
    {"S": "1", "E": "0", "N": "1", "W": "0"},  # "RL_Door_WallValues":
    {"S": "0", "E": "1", "N": "0", "W": "1"},  # "TB_Door_WallValues":
]

buttons = {
    "Go-Back": (45, 570), "EASY": (140, 580), "MEDIUM": (140, 550), "HARD": (140, 520), "EXTREME": (140, 490),
    "Hide Grid": (230, 560), "Show Grid": (230, 520), "By Click": (410, 560), "By Select": (410, 520),
    "Solution": (320, 580), "Clear": (320, 540), "Add Q & A": (320, 500), "SAVE": (525, 50)
}
wall_buttons = {
    "R_Wall": (501, 547), "L_Wall": (561, 547), "T_Wall": (501, 487), "B_Wall": (561, 487),
    "RT_Wall": (501, 427), "LT_Wall": (561, 427), "RB_Wall": (501, 367), "LB_Wall": (561, 367),
    "TB_Wall": (501, 307), "RL_Wall": (561, 307), "RLT_Wall": (501, 247), "LTB_Wall": (561, 247),
    "RLB_Wall": (501, 187), "RTB_Wall": (561, 187), "RL_Door_Wall": (501, 127), "TB_Door_Wall": (561, 127),
}
