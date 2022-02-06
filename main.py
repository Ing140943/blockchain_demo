from blockchain import Blockchain
from flask import Flask

# web server
app = Flask(__name__)
blockchain = Blockchain() # create genesis block
#routing
@app.route('/')
def hello():
    return "<h1>Hello Blockchain</h1>"

if __name__ == "__main__":
    app.run()
    # print(blockchain.chain[0]) # see the genesis block
    # print(blockchain.hash(blockchain.chain[0])) # encode the block