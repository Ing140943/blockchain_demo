# This is blockchain demo by python

Blockchain is the one of the technology that I interested in. So this is my blockchain demo study from youtube.

# Requirements
* Python 3.6+
* Postman or any tools for test API

# How to demonstrate it?
* Run the ```main.py``` file you will receive the ```http://127.0.0.1:5000``` so this is our main base url
* This is all related pathes
    - ```/is_valid```
    - ```/mining```
    - ```/get_chain```
You can try this path by using postman or type in the browser

# Step of this blockchain demp
1. After you run the ```main.py``` file assume that now your network is ready to add the block and the network already contain the ```genesis block```
2. You can try to your first block to our network by this path ```http://127.0.0.1:5000/mining```. The minig is the process that we assume that the minier already found the hash of that block and that block is already placed in the network.
3. You can check that each of blocks is valid by use this path ```http://127.0.0.1:5000/is_valid```. It will evaluate that the previous hash of the current block is the same as the hash of the previous block.
4. You can see all the block that verified by this path ```http://127.0.0.1:5000/get_chain```

This is the short brief about the concept of blockchain technology hope you enjoy it :)