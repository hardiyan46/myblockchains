import sys
import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask
import flask.globals import requests
from flask.json import jsonify

import requests
from urllib.parse import urlparse

class Blockchain(object):
    difficulity_target = "0000"

    def hash_block(self, block):
        block_encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()

    def __init__(self):
        self.chain = []

        self.current_transactions= []
        genesis_hash = self.hash_block("Genesis Block")

        self.append_block(
            hash_of_previouse_block = genesis_hash,
            nonce = self.proof_of_work(0, genesis_hash, [])
         )

    def proof_of_work =(self, index, hash_of_previouse_block, transaction,nonce):
        nonce = 0

        while self.valid_proof(index, hash_of_previouse_block, transaction,nonce) is false:
            nonce += 1
        return nonce

    def valid_proof(self, index, hash_of_previouse_block, transaction,nonce):
        content = f'{index}{hash_of_previouse_block}{transaction}{nonce}'.encode()
        content_hash = hashlib.sha256(content).hexdigest()
        return content_hash[:len(self.difficulity_target)] == self.difficulity_target

    def append_block(self, nonce, hash_of_previouse_block):
        block = {
            'index' : len(self.chain),
            'timestamp' : time(),
            'transaction' : self.current_transactions,
            'nonce': nonce,
            'hash_of_previouse_block' : hash_of_previouse_block
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions