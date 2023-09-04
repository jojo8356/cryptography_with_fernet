from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('unlock.key', 'wb') as unlock:
        unlock.write(key)
    return key

def read_key():
    with open('unlock.key', 'rb') as unlock:
        key = unlock.read()
    return key

def init_key():
    try:
        key = read_key()
    except:
        key = generate_key()
    return Fernet(key)

def encrypt(txt):
    f = init_key()
    return f.encrypt(txt)
    
def decrypt(encrypted):
    f = init_key()
    return f.decrypt(encrypted)
