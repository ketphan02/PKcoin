from elements.chain import BlockChain 
from elements.block import Block

PKcoin = BlockChain()

PKcoin.addBlock(Block(1, "26/05/2020", { 'amount': 100 }))

PKcoin.addBlock(Block(2, "15/08/2020", { 'amount': 60 }))