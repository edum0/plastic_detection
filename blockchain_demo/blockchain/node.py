from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route("/chain", methods=["GET"])
def get_chain():
    blockchain.load_chain()
    return jsonify([b.to_dict() for b in blockchain.chain])

if __name__ == "__main__":
    app.run(port=5000)
