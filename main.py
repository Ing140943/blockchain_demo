from blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain() # create genesis block
    print(blockchain.chain[0]) # see the genesis block
    print(blockchain.hash(blockchain.chain[0])) # encode the block