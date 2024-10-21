from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response  # Import your chatbot function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = chatbot_response(user_input)  # Call your chatbot function
    return jsonify(bot_response)

if __name__ == "__main__":
    app.run(debug=True)
