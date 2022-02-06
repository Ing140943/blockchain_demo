from blockchain import Blockchain
from flask import Flask, jsonify

# web server
app = Flask(__name__)
blockchain = Blockchain() # create genesis block
#routing
@app.route('/')
def hello():
    return "<h1>Hello Blockchain</h1>"

@app.route('/get_chain', methods=["GET"])
def get_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/mining', methods=['GET'])
def mining_block():
    # Proof of work
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block["nonce"]
    # Find Nonce value
    nonce = blockchain.proof_of_work(previous_nonce)
    # Previous hash
    previous_hash = blockchain.hash(previous_block)
    # Update block
    block = blockchain.create_block(nonce, previous_hash)
    response = {
        "message": "Mining Block Successful!",
        "index": block["index"],
        "timestamp": block["timestamp"],
        "nonce": block["nonce"],
        "previous_hash": block["previous_hash"]
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run()
    # print(blockchain.chain[0]) # see the genesis block
    # print(blockchain.hash(blockchain.chain[0])) # encode the block