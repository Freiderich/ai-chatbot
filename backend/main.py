from flask import Flask, request, jsonify, send_from_directory
from bot.chatbot import get_bot_response
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

# Serve the frontend index.html
@app.get("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# Chat API
@app.post("/chat")
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    response = get_bot_response(user_msg)
    return jsonify({"reply": response})

# Serve other frontend static files (CSS/JS)
@app.get("/<path:path>")
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
