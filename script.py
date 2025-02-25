from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/data', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json()
        data_command = data.get('dataCommand')
        if data_command:
            # Process the command derived from data-command here
            command = f"Command derived from {data_command}"
            return jsonify({"message": "Command received", "command": command}), 200
        else:
            return jsonify({"message": "data-command field is missing"}), 400
    else:
        return jsonify({"message": "Request body must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
