import json
import numpy as np
from PIL import Image

with open('eve-flow2.json') as json_file:
    data = json.load(json_file)

ports = dict()
n_udp = 0
udp_ports = []
s_udp = ""
s_tcp = ""
tcp_ports = []
tcp_ports_lsb = []
for record in data:
    #if record["dest_ip"] == "172.30.0.2":
    #if int(record['dest_port']) not in ports:
    if record['proto'] == "UDP":
        n_udp += 1
        s_udp += chr(int(record['dest_port']))
        udp_ports.append(int(record['dest_port']))
        #print('dest når udp:', chr(int(record['dest_port'])))
    else:
        s_tcp += chr(int(record['dest_port'])) #chr
        tcp_ports.append(int(record['dest_port']))
        tcp_ports_lsb.append(int(record['dest_port'])& 0b1)

        theport = int(record['dest_port'])
        if theport in ports:
            ports[theport] += 1
        else:
            ports[theport] = 1


port_lsb = "".join([str(x) for x in tcp_ports_lsb]).encode()

#print(ports)
print(s_udp)
#print(s_tcp)
#print('antall p20:', p20)
#print('antall udp:', n_udp)
#print('høyeste sport:',max(sport))
#print('høyeste dport:',max(dport))
#print('antall porter:',len(ports))
#print(tcp_ports)
#print(lsb)
#print(max(tcp_ports))

#visu = Image.new("L", (769, 23)) 
img_data = np.reshape(np.array(tcp_ports), (23, -1))
#img_data.resize((200,89))
visu = Image.fromarray(img_data, mode="1")
visu.show()

#print(len(ports))
#print(ports)

# counts of port-usage
#print('(ports, checks):', sorted(ports.items(), key = lambda kv:(kv[1], kv[0])))

'''
source:
    95 stk UDP fra port 666: dest_port gir ascii verdier: 
        "Bra! Men dessverre fant du bare et EGG{ } uten innhold -- hva med visualisering av TCP-pakkene?"
    17687 stk TCP fra port 20 (til port 1-46)
    23 * 769
'''