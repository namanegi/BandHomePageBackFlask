from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import os

DATA_PATH = os.path.dirname(os.path.realpath(__file__))
PRI_FILE = os.path.join(DATA_PATH, 'private.pem')
PUB_FILE = os.path.join(DATA_PATH, 'receiver.pem')

class KeyNotFound(Exception):
    pass

def init_keys():
    private_key = RSA.generate(2048)
    with open(PRI_FILE, "w") as f:
        tmp = private_key.export_key().decode('utf-8')
        f.write(tmp)

    public_key = private_key.publickey()
    with open(PUB_FILE, "w") as f:
        tmp = public_key.export_key().decode('utf-8')
        f.write(tmp)

def read_pri_key():
    with open(PRI_FILE, 'rb') as f:
        private_pem = f.read()
        private_key = RSA.import_key(private_pem)

    if private_key is None:
        raise KeyNotFound
    else:
        return private_key

def read_pub_key():
    with open(PUB_FILE, 'rb') as f:
        public_pem = f.read()
        public_key = RSA.import_key(public_pem)
    
    if public_key is None:
        raise KeyNotFound
    else:
        return public_key

def encoding_str(message: str):
    public_key = read_pub_key()
    cipher_rsa = PKCS1_OAEP.new(public_key)
    return cipher_rsa.encrypt(message.encode())

def decoding_str(coded_mess: str):
    private_key= read_pri_key()
    decipher_rsa = PKCS1_OAEP.new(private_key)
    return decipher_rsa.decrypt(coded_mess).decode('UTF-8')
