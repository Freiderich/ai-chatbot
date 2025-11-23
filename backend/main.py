from flask import Flask, request, jsonify, send_from_directory
from bot.chatbot import get_bot_response  # your bot logic

app = Flask(__name__, static_folder="../frontend", static_url_path="")

# Serve frontend index.html
@app.route("/")
def index():
    return app.send_static_file("index.html")

# Serve CSS/JS automatically via static_folder
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

# Chat endpoint
@app.post("/chat")
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    response = get_bot_response(user_msg)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
