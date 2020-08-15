import hashlib
import json

class Block:
    def __init__(self, index, datetime, data, prevHash = ''):
        self.index = index
        self.datetime = datetime
        self.data = data
        self.prevHash = prevHash
        self.hash = self.hashFunc()
        
    def hashFunc(self):
        
        hashData = str(self.index) + str(self.datetime) + str(json.dumps(self.data)) + str(self.prevHash)
        hashData = hashData.encode()
        hashData = str(hashlib.sha256(hashData).hexdigest())
        return hashData