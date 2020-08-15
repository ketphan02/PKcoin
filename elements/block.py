import hashlib
import json

class Block:
    def __init__(self, index, datetime, data, prevHash = ''):
        self.key = 0
        self.index = index
        self.datetime = datetime
        self.data = data
        self.prevHash = prevHash
        self.hash = self.hashFunc()
        
    def hashFunc(self):
        
        hashData = str(self.index) + str(self.datetime) + str(json.dumps(self.data)) + str(self.prevHash) + str(self.key)
        hashData = hashData.encode()
        hashData = str(hashlib.sha256(hashData).hexdigest())
        return hashData

    def mineBlock(self, diff):
        while self.hash[0:diff] != "0" * diff:
            self.key = self.key + 1
            self.hash = self.hashFunc()

        print(self.hash)