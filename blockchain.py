import datetime

class Blockchain:
    

    # Constructor for blockchain class
    def __init__(self):
        """Contain group of blocks"""
        self.chain = [] # list to contain block
        self.create_block(nonce=1, previous_hash=0)  #genesis block
    
    def create_block(self, nonce, previous_hash):
        """
        Create block in blockchain network and keep components of each block

        Parameters:
        nonce: Value to prove the hash number
        previuos_hash: hash of the previous hash

        Returns: 

        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "nonce": nonce,
            "previous_hash": previous_hash
            }
        
        self.chain.append(block)
        return block