import hashlib

def md5_crypt(string):
    return hashlib.new("md5", string.encode('utf-8')).hexdigest()