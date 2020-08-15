from .block import Block

class BlockChain:
    def __init__(self):
        self.chain = [self.firstBlock()]
        self.diff = 4

    def firstBlock(self):
        return Block(0, "01/01/2020", { 'amount': 0 }, '')

    def lastestBlock(self):
        return self.chain[-1]
    
    def addBlock(self, newBlock):
        newBlock.prevHash = self.lastestBlock().hash
        newBlock.mineBlock(self.diff)
        self.chain.append(newBlock)

    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            lastBlock = self.chain[i - 1]
            
            if (currentBlock.hash != currentBlock.hashFunc()):
                return False

            if (lastBlock.hash != currentBlock.prevHash):
                return False
        
        return True