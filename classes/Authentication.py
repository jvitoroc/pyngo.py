import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import pyparsing as pp

username = pp.Literal("").setResultsName('username')
delimiter = pp.Suppress(pp.Literal("|"))
equal = pp.Suppress(pp.Literal("="))
password = pp.Word(pp.empty).setResultsName('password')
powers = pp.Word(pp.empty).setResultsName('powers')

account = pp.LineStart()+username+delimiter+password+equal+powers+pp.lineEnd()

def lookUp(username, path):
    return account.parseFile(path+"/auth.dat")

"""
auth.dat
username|password=['get', 'insert']
"""

class Authentication:

    def __init__(self, username, password, path):

        data = lookUp(username, path)

        salt = os.urandom(8)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))
        if(key.decrypt(data['password']) == password):
            self.powers = key.decrypt(data['powers'])

    def canIGet(self):
        pass

    def canIInsert(self):
        pass

    def createAccount(self, username, password, powers):
        #must be root account
        pass