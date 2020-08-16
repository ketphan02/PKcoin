from elements.chain import BlockChain 
from elements.block import Block
from elements.transactions import Transactions

PKcoin = BlockChain()

PKcoin.minePendingTransactions('PhanKiet')
print(PKcoin.getBalance('PhanKiet'))

PKcoin.minePendingTransactions('PhanKiet')
print(PKcoin.getBalance('PhanKiet'))