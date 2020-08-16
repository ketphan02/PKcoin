from .block import Block
from .transactions import Transactions
from datetime import datetime

class BlockChain:
    def __init__(self):
        self.chain = [self.firstBlock()]
        self.diff = 5
        self.pendingTransactions = []
        self.miningReward = 20

    def firstBlock(self):
        return Block("01/01/2020", [Transactions('', '', 0)])

    def lastestBlock(self):
        return self.chain[-1]
    
    def addBlock(self, newBlock):
        newBlock.prevHash = self.lastestBlock().hash
        newBlock.mineBlock(self.diff)
        self.chain.append(newBlock)

    def createTransaction(self, transaction):
        self.pendingTransactions.append(transaction)

    def minePendingTransactions(self, miningRewardAddress):
        print("Starting the process...")

        block = Block(datetime.now(), self.pendingTransactions)
        block.mineBlock(self.diff)

        print("Mined !")
        self.chain.append(block)

        self.pendingTransactions = [ Transactions('', miningRewardAddress, self.miningReward) ]

    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            lastBlock = self.chain[i - 1]
            
            if (currentBlock.hash != currentBlock.hashFunc()):
                return False

            if (lastBlock.hash != currentBlock.prevHash):
                return False
        
        return True

    def getBalance(self, address):
        balance = 0

        for block in self.chain:
            for trans in block.transactions:
                if trans.fromAddress == address:
                    balance = balance - trans.amount
                if trans.toAddress == address:
                    balance = balance + trans.amount

        return balance
