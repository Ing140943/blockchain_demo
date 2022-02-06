import datetime
import json # some function in this module can apply with dictionary in python
import hashlib

class Blockchain:
    

    # Constructor for blockchain class
    def __init__(self):
        """Contain group of blocks"""
        self.chain = [] # list to contain block
        self.create_block(nonce=1, previous_hash="0")  #genesis block
        # self.create_block(nonce=10, previous_hash="00")  #genesis block
        # self.create_block(nonce=20, previous_hash="000")  #genesis block
    
    def create_block(self, nonce, previous_hash):
        """
        Create block in blockchain network and keep components of each block

        Parameters:
            nonce: Value to prove the hash number
            previuos_hash: hash of the previous hash

        Returns: 
            dict block
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "nonce": nonce,
            "previous_hash": previous_hash
        }
        
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """Get the previous block"""
        return self.chain[-1]
        
    def hash(self, block):
        """Encode the block, order the key attribut in the list and traslate \
            from python object (dict) => json object"""
        encode_block = json.dumps(block, sort_keys=True).encode() # from python object (dict) => json object
        return hashlib.sha256(encode_block).hexdigest()           # .sha256 => apply with sha 256 format, hexdigest = เลขฐาน 16

    def proof_of_work(self, previous_nonce):
        """Find the nonce value that can get the target hash
           first four digits => 0000xxxxxxxx"""
        new_nonce = 1 # nonce value that we want
        check_proof = False # variable to check nonce value must be close to target hash

        # solve mathematic problem
        while check_proof is False:
            # 1 set of hexadecimal number
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_nonce += 1
        return new_nonce

