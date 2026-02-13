from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/records", methods=["GET"])
def get_records():
    return jsonify([
        {"image_path": "image1.png", "numbers": [1, 2, 3, 4]},
        {"image_path": "image2.png", "numbers": [5, 6, 7, 8]},
        {"image_path": "image1.png", "numbers": [9, 10, 11, 12]}
    ])

if __name__ == "__main__":
    app.run(port=6000)
