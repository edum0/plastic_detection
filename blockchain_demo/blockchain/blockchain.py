import hashlib
import json
import time
import base64
import os


BLOCKCHAIN_FILE = "blockchain.json"


class Block:
    def __init__(self, index, timestamp, image_data, numbers, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.image_data = image_data
        self.numbers = numbers
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "image_data": self.image_data,
            "numbers": self.numbers,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self):
        return self.__dict__


class Blockchain:
    def __init__(self):
        self.chain = []
        self.load_chain()

        if not self.chain:
            self.create_genesis_block()
            self.save_chain()

    def create_genesis_block(self):
        genesis = Block(0, time.time(), "GENESIS", [0, 0, 0], "0")
        self.chain.append(genesis)

    def add_block_from_data(self, image_path, numbers):
        with open(image_path, "rb") as f:
            image_base64 = base64.b64encode(f.read()).decode()

        previous_hash = self.chain[-1].hash

        block = Block(
            len(self.chain),
            time.time(),
            image_base64,
            numbers,
            previous_hash
        )

        self.chain.append(block)
        self.save_chain()

    def save_chain(self):
        with open(BLOCKCHAIN_FILE, "w") as f:
            json.dump([b.to_dict() for b in self.chain], f, indent=4)

    def load_chain(self):
        if os.path.exists(BLOCKCHAIN_FILE):
            with open(BLOCKCHAIN_FILE, "r") as f:
                data = json.load(f)
                self.chain = []

                for block_data in data:
                    block = Block(
                        block_data["index"],
                        block_data["timestamp"],
                        block_data["image_data"],
                        block_data["numbers"],
                        block_data["previous_hash"]
                    )
                    block.hash = block_data["hash"]
                    self.chain.append(block)
