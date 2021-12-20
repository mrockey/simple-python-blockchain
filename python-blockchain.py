from hashlib import sha256
import time


class block:
    # Timestamp, data, and previous hash are passed. CalculateHash() is called to determine current block's hash.
	def __init__ (self, timestamp, data, previousHash = ' '):
		self.timestamp = timestamp
		self.data = data
		self.previousHash = previousHash
		self.hash = self.calculateHash()

    # Timestamp, data, and previous hash are combined to created the current block's hash.
	def calculateHash(self):
		return sha256((str(self.timestamp) + str(self.data) + str(self.previousHash)).encode()).hexdigest()


class blockchain:
    # Upon creation of the blockchain object, the genesis block is mined automatically.
	def __init__(self):
		self.chain = [self.createGenesis()]

    # The genesis block creation:
	def createGenesis(self):
		return block(time.ctime(), "genesisBlock", "00000")

    # Mining a new block on the blockchain. Creates a new block object.
	def mineBlock(self, data):
		node = block(time.ctime(), data, self.chain[-1].hash)
		self.chain.append(node)

    # Print all the current blocks in the blockchain.
	def printBlockchain(self):
		for i in range(len(self.chain)):
			print(i, self.chain[i].timestamp, self.chain[i].data, self.chain[i].previousHash, self.chain[i].hash)


# Create blockchain.
RockChain = blockchain()

# Request data for next block.
print("Enter data that will be placed in the next block: ")
data = raw_input()

# Send data to be mined in new block.
print("\nNew block is being mined...")
RockChain.mineBlock(data)

# Print the blockchain.
print("\nNew block has been mined... printing blockchain: ")
RockChain.printBlockchain()