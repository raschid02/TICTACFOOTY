
from flask import Flask, jsonify, request

app = Flask(__name__)

# Spielfeld erstellen
grid = [[" " for _ in range(3)] for _ in range(3)]
turn_player1 = True
player1_symbol = "X"
player2_symbol = "O"

# Spielfeld zurückgeben
@app.route('/get_grid', methods=['GET'])
def get_grid():
    return jsonify(grid)

# Spielerzug ausführen
@app.route('/make_move', methods=['POST'])
def make_move():
    global turn_player1
    data = request.json
    cell = data["cell"] - 1
    i, j = cell // 3, cell % 3

    if grid[i][j] == " ":
        grid[i][j] = player1_symbol if turn_player1 else player2_symbol
        turn_player1 = not turn_player1
        winner = check_winner()
        return jsonify({"grid": grid, "winner": winner})
    else:
        return jsonify({"error": "Zelle bereits belegt!"})

# Gewinnüberprüfung
def check_winner():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != " ":
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != " ":
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return grid[0][2]
    return None

if __name__ == '__main__':
    app.run(debug=True)
