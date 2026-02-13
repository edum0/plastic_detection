import requests
import time
from blockchain.blockchain import Blockchain

RECORDS_API = "http://localhost:6000/records"

def fetch_and_add():
    blockchain = Blockchain()

    response = requests.get(RECORDS_API)
    records = response.json()

    for record in records:
        print("Adding block:", record)
        blockchain.add_block_from_data(
            record["image_path"],
            record["numbers"]
        )

    print("All records added.")

if __name__ == "__main__":
    time.sleep(2)  
    fetch_and_add()
