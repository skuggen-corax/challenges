#!/usr/bin/env python
'''
script gets EGG right, but something is strange on first message from server

hint: GODTERI
1110111010 00 111011101110 00 11101010 00 1110 00 10 00 10111010 00 101     <= 1110 = -, 10 = ., 00 = word
langlangko    langlanglang    langkoko    lang    ko    kolangko    koko
--.           ---             -..         -       .     .-.         ..
'''

import Crypto.Cipher.XOR
import base64
from scapy.utils import rdpcap
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
import time

MORSE = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 
                    'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
                    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
                    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                    'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', 
                    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
                    ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
MORSE_REV = {value:key for key,value in MORSE.items()}

client = '10.100.6.187'
server = '10.218.12.1'

def parse_word(word):
    #print('\n',word.split('000'))

    # ook to morse
    word = word.replace('1110', '-')
    word = word.replace('10', '.')
    word = word.replace('00', ' ')
    word = word.replace('1', ' ')
    conv = word.split(' ')

    #morse to txt
    conved = []
    for w in conv:
        if w != '':
            conved.append(MORSE_REV[w])
    print("".join(conved), end=" ")

count = 0
word = []
letter = []
for (pkt_data) in rdpcap('c2_trafikk_v2.pcap'):
    count += 1
    
    # special stuff for first packet
    if count == 1:
        first_time = pkt_data.time
        time = first_time
        last_time = first_time
        last_sender = ""
    else:
        time = pkt_data.time

    ether_pkt = Ether(pkt_data)

    # who is sender?
    if pkt_data[IP].src == server:
        sender = "server"
    elif pkt_data[IP].src == client:
        sender = 'client'

    # time since last packet
    t_diff = round(time - last_time)

    if last_sender != sender:
        print('\nFrom: ', sender, ': ', sep="", end="")
        #t_diff = 0

    # parse differen intervals as ook
    # interval of 8 is interpreted as 00000001, interval of 1 is just 1
    if t_diff == 8:
        #print('\n',end="")
        word.append('000')
        parse_word("".join(word))
        word = ['1']
    elif t_diff == 0:
        word.append('1')
    elif t_diff == 1:
        word.append('1')
    elif t_diff == 2:
        word.append('01')
    elif t_diff == 4:
        word.append('0001')
    else:
        word.append('0001')

    # decode red herring text - just for fun
    secret = filter(lambda x: x.startswith('X-Secret'), bytes(ether_pkt)[-204:].decode().split('\n')) # find key
    secret = list(secret)[0].split(' ')[1].strip()  # get key value
    secret = bytes(bytearray.fromhex(format(int(secret), 'x'))) # get bytes as hex from the string (where the key is in decimal)
    code = bytes(ether_pkt)[-204:].decode().split('\n')[-1]  # get message
    cbytes = base64.b64decode(code) # decode base64 message
    xor = Crypto.Cipher.XOR.new(secret) # xor cipher with key
    decode = xor.decrypt(cbytes)    # decode coded message
    #print('\nmsg: ', decode.decode())

    last_time = time
    last_sender = sender
print('\n')