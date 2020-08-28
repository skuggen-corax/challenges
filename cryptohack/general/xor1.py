import binascii

'''
label
xor each with integer 13
crypto{result}
'''

inp = 'label'
secret = 13

decoded = "".join([chr(ord(c) ^ secret) for c in inp])

print('crypto{', decoded, '}', sep="")
