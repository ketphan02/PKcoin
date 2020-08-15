from block import Block

class BlockChain:
    def __init__(self):
        self.chain = [self.firstBlock()]

    def firstBlock(self):
        return Block(0, "01/01/2020", { 'amount': 0 }, '')

    def lastBlock(self):
        return self.chain[-1]
    
    def addBlock(self, newBlock):
        newBlock.prevHash = self.lastBlock().hash
        newBlock.hash = newBlock.hashFunc()
        self.chain.append(newBlock)