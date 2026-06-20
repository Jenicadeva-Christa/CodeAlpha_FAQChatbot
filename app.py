"""
CodeAlpha FAQ Chatbot - Web Server
==================================
Serves the chatbot web interface and processes user questions.
Author: Jenicadeva Christa S
"""

import os
from flask import Flask, render_template, request, jsonify
from chatbot import FAQChatbot
app = Flask(__name__)
try:
    chatbot = FAQChatbot()
except Exception as e:
    print(f"Error initializing FAQChatbot engine: {e}")
    chatbot = None
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    """
    Accepts user questions via POST, queries the NLP matching engine, and returns a JSON response.
    """
    if chatbot is None:
        return jsonify({"response": "The chatbot engine failed to initialize. Please contact system administration."}), 500
    data = request.get_json()    
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request payload. 'message' field is required."}), 400

    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"response": "Please enter a question, and I'll do my best to answer it!"}), 200

    try:
        response_text = chatbot.get_response(user_message)
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error handling chat request: {e}")
        return jsonify({"response": "I encountered an internal error. Please try asking again."}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
