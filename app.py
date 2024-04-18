from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Dictionary to store active chat sessions
active_chats = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/chat')
def chat():
    # Assuming you're retrieving the room ID from somewhere, replace 'room_id' with your actual variable
    room_id = request.args.get('room')
    return render_template('chat.html', room=room_id)

