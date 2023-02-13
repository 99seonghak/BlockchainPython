import hashlib
import json
import datetime
from time import time
from uuid import uuid4

# 블록체인 기본구조
class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # 새로운 블록 생성
        self.new_block(previous_hash=1, proof=100) # genesis block

    def new_block(self, proof, previous_hash=None):

        #  블록의 모습
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : str(datetime.datetime.now()),
            'transactions' : self.current_transactions,
            'proof' : proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    # 블록에 트랜잭션 추가
    def new_transaction(self, sender, recipient, amount):

        self.current_transactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
        })

        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block):
        
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):

        return self.chain[-1]
    
    # 작업증명(PoW) ** Hashcash 알고리즘
    # 원리 : 어떤 정수 x가 있을 때 다른 수인 y를 곱해서 0으로 끝나야 한다고 결정,
    # hash( x * y ) = ac23dc ... 0이 되는 수를 찾는 것이다.
    # 작업증명(PoW) 구현
    def proof_of_work(self, last_proof):

        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):

        guess = str(last_proof * proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
    
        return guess_hash[:5] == "00000"

'''

# 해당 코드를 실행시키면 y = 21이 나온다.
# 바로 저 0값이 점점 길어지면 길어질수록 문제가 어려워진다.
# 그 값을 찾으면 해당 코인을 보상   
from hashlib import sha256
x = 5
y = 0  
while sha256(str(x*y).encode()).hexdigest()[-1] != "0":
    y += 1
print('The solution is y = {0}'.format(y))

'''