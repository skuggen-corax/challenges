import OpenSSL.crypto as c
from Crypto.PublicKey import RSA

file = "2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der"
with open(file, 'rb') as f:
    data = f.read()

cert = c.load_certificate(c.FILETYPE_ASN1, data)

pk = cert.get_pubkey()

key = c.dump_publickey(c.FILETYPE_ASN1, pk)

print("flag:", RSA.importKey(key).n)
