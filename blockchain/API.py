# API 만들기 #


# /transaction/new : 블록을 위한 새로운 트랜젝션 생성 #
# /mine : 서버에게 새로운 블록 채굴하라고 알려줌 #
# /chain : 블록체인 전체를 반환 #


# API 뼈대 생성 #

from flask import Flask
import flask
import json
from textwrap import dedent
from uuid import uuid4

from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }

    return flask.jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
