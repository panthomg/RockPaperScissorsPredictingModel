from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)


memory = {
    'rock': {'rock': 0, 'paper': 0, 'scissors': 0},
    'paper': {'rock': 0, 'paper': 0, 'scissors': 0},
    'scissors': {'rock': 0, 'paper': 0, 'scissors': 0}
}
beats = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
last_user_move = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    global last_user_move
    user_move = request.json.get("move")
# from here we predict from users last move
    if last_user_move and sum(memory[last_user_move].values()) > 0:
        predicted_user_move = max(memory[last_user_move], key=memory[last_user_move].get)
    else:
        predicted_user_move = random.choice(['rock', 'paper', 'scissors'])

    computer_move = beats[predicted_user_move]
    if last_user_move:
        memory[last_user_move][user_move] += 1
#saving current movie to use next round
    last_user_move = user_move 

    return jsonify({
        "user_move": user_move,
        "computer_move": computer_move,
        "predicted_user_move": predicted_user_move
    })
if __name__ == "__main__":
    app.run(debug=True)
