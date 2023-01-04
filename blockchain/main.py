# 블록체인 기본구조 #

class Blockchain(object):

    def __init__(self):
        self.chain=[]
        self.current_transactions=[]

    def new_block(self):
        pass

    def new_transaction(self):
        pass

    @staticmethod
    def hash(self):
        pass

    @property
    def last_block(self):
        pass


# 블록체인의 최소단위인 블록 제작 #

block = {
    'index':1,
    'timestamp' :1506057125.900785,
    'transactions':[
        {
            'sender':"8727147felf5426f9dd545de4b27ee00",
            'recipient':"a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount':5,
            }
        ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9847"
    }

#블록을 만들어서 이전 블록의 해시값을 저장하게 될 수 있도록 함#


# 블록에 트랜젝션 추가 #

class Blockchain(object):
    
    def new_transaction(self, sender, recipient, amount):

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

# 새로운 블록 생성 #

import hashlib
import json
from time import time


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

        # 가장 최초의 블록은 genesis block 생성

    def new_block(self, proof, previous_hash=None):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):

        return self.chain[-1]

# 블록 생성 + 블록 생성 원리 #


# 작업증명(POW) : 새로운 블록을 생성하거나 채굴하는 것 #
# 작업증명의 원리 : 어떤 정수 x 가 있을 때 다른 수인 y를 곱해서 0으로 끝나야 한다고 생각했다면, hash(x*y)=ac23dc....0이 되는 수를 찾는 것 #

from hashlib import sha256
x = 5
y = 0  
while sha256(str(x*y).encode()).hexdigest()[-1] != "0":
    y += 1
print('The solution is y = {0}'.format(y))


# 작업증명(POW) 구현 #

import hashlib
import json
from time import time
from uuid import uuid4


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100) # genesis block

    def new_block(self, proof, previous_hash=None):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):

        return self.chain[-1]

    def proof_of_work(self, last_proof):

        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):

        guess = str(last_proof * proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# 짠 코드를 블록체인 내부에 넣는 과정 #
