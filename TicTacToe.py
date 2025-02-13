
grid = []
line = []
for i in range(3) :
    for j in range(3) :
        line.append(" ")
        grid.append(line)
        line = []



#grid printing
def print_grid() :
    for i in range(3) :
        print("|", end = "")
    for j in range(3) :
        print(grid[i][j], "|", end = "")

        print("")


#player turn
def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False
        print(f"{player2} ist an der Reihe")
    else:
        turn_player1 = True
        print(f"{player1} ist an der Reihe")
    return turn_player1


#choosing cell
def free_cell(cell):
    cell-= 1
    i = int(cell / 3)
    j = cell % 3
    if turn_player1 == True :
        grid[i] [j] = player1_symbol
    else:
         grid[i] [j] = player2_symbol
    return
grid


#checking cell
def free_cell(cell):
    cell-= 1
    i = int(cell / 3)
    j = cell % 3
    if grid  [i] [j] == player1_symbol or player2_symbol :
        print("zelle bereits belegt")
        return False
    return False


#Game opening
print("willkommen bei TicaTacToe")
print("")
print_grid()
print("")
player1 = input("Bitte Namen von Player1 eingeben : ")
player1_symbol = input("Bitte Symbol für Player 1 Angeben : ")
player2 = input("Bitte Namen von Player2 eingeben : ")
player2_symbol = input("Bitte Symbol für Player2 Angeben : ")
Game = True
full_grid = False
turn_player1 = False
winner = ""


#win check
def win check(grid, player1_symbol, player2_symbol):
full grid = True
player1_symbol_count=0
player2_symbol_count=0
#checking rows
for i in range(3):
    for j in range (3):
        if grid [i][j]
