import copy

game_board = [[0,0],[0,0]]

backup_board = game_board[:]
backup_board_TWO = copy.deepcopy(game_board)

backup_board[0][0] = 1

print(f"备份地图ONE:{backup_board}")
print(f"备份地图TWO:{backup_board_TWO}")
print(f"原地图：{game_board}")


#   [:]、.copy()、 list()、 dict()  它们全是浅拷贝
#   对于二位列表，必须用copy.deepcopy()