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

    
if __name__ == "__main__":
    app.run()
    # print(blockchain.chain[0]) # see the genesis block
    # print(blockchain.hash(blockchain.chain[0])) # encode the block