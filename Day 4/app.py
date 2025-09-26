

from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the User Management API!"})


# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]})
    return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = str(len(users) + 1)  # simple auto-increment id
    users[user_id] = data
    return jsonify({"message": "User added", "user_id": user_id}), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify({"message": "User updated", user_id: users[user_id]})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", user_id: deleted_user})
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
      
      
      
      app.run(debug=True)
