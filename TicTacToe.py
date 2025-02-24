
import os
from flask import Flask, render_template, jsonify, request

# Absoluten Pfad setzen
app = Flask(__name__, template_folder=os.path.abspath("templates"))

# Debugging: Ausgabe, wo Flask nach Templates sucht
print("Flask sucht nach Templates in:", os.path.abspath("templates"))


# Spielfeld erstellen
grid = [[" " for _ in range(3)] for _ in range(3)]
turn_player1 = True
player1_symbol = "X"
player2_symbol = "O"

@app.route('/')
def home():
    return render_template("index.html")  # Ensure index.html is in the templates directory

@app.route('/restart', methods=['POST'])
def restart():
    global grid, turn_player1
    grid = [[" " for _ in range(3)] for _ in range(3)]
    turn_player1 = True
    return jsonify({"message": "Spiel wurde zurückgesetzt.", "grid": grid})

    


@app.route('/get_grid', methods=['GET'])
def get_grid():
    return jsonify(grid)

@app.route('/make_move', methods=['POST'])
def make_move():
    global turn_player1
    data = request.json
    if not data or "cell" not in data:
        return jsonify({"error": "Fehlende Eingabe!"})
    
    try:
        cell = int(data["cell"])
    except ValueError:
        return jsonify({"error": "Ungültige Eingabe! Bitte eine Zahl zwischen 1 und 9 wählen."})
    
    if not (1 <= cell <= 9):
        return jsonify({"error": "Ungültige Eingabe! Bitte eine Zahl zwischen 1 und 9 wählen."})
    

    cell -= 1  # Umwandlung auf 0-basierten Index
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
    
    if all(cell != " " for row in grid for cell in row):
        return "Unentschieden"
    
    return None


if __name__ == '__main__':
    app.run(debug=True)

