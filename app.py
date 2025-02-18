from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_strong_password(password):
    """Check if the password is strong."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[\W_]", password):
        return False
    return True

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if not is_strong_password(password):
        return jsonify({'message': 'Password is not strong enough'}), 400

    # Here you would add logic to save the user to a database
    # For this example, we'll just return a success message

    return jsonify({'message': 'User signed up successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)