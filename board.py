# player_id definition
player_1_id = 1
player_2_id = 2
player_1_mark = "X"
player_2_mark = "O"

def print_board(board):
  for elem in board:
    print(elem)


def place_mark(board, row, col, player_id):
  if player_id == player_1_id:
    board[row][col] = player_1_mark
  elif player_id == player_2_id:
    board[row][col] = player_2_mark
  
  
def check_mark(board, row, col):
  if row not in range(3) or col not in range(3):
    print("The row number can only be value between 0 and 2(included), and same to the column number")
    return False
  if board[row][col] == player_1_mark or board[row][col] == player_2_mark:
    return False
  return True
  
def take_turn_place_mark(board, player_id):
  print("please input the row number where player " + str(player_id) + " want to place the mark")
  row = int(input())
  print("please input the column number where player " + str(player_id) + " want to place the mark")
  col = int(input())
  is_location_available = check_mark(board, row, col)
  # ensure the location at the input row and column is available
  while not is_location_available:
    print("the location at row " + str(row) + " and column " + str(col) + " is not available, please re-input the row and column number")
    print("please input the row number where player " + str(player_id) + " want to place the mark")
    row = int(input())
    print("please input the column number where player " + str(player_id) + " want to place the mark")
    col = int(input())
    is_location_available = check_mark(board, row, col)
  if player_id == player_1_id:
    player_mark = player_1_mark
  else:
    player_mark = player_2_mark
  print("Player " + str(player_id) + " will input " + player_mark + " into board")
  place_mark(board, row, col, player_id)
  print_board(board)

# create a tic-tac-toe board
board = []
for _ in range(3):
  board.append(['-', '-', '-'])

# check who will place mark first; player id can only be 1 or 2, until player input the correct id
print("Input the id of the player who will place mark first: ")
first_player_id = int(input())
while first_player_id != player_1_id and first_player_id != player_2_id:
  print("player id can only be: " + str(player_1_id) + " or " + str(player_2_id))
  print("Input the id of the player who will place mark first: ")
  first_player_id = int(input())
  
if first_player_id == player_1_id:
  second_player_id = player_2_id

# player 1 and player 2 take turns based on who will place mark first
# maximum 5 times for battle
for _ in range(5):
  take_turn_place_mark(board, first_player_id)
  take_turn_place_mark(board, second_player_id)
  






  
  
  
  
  
  
