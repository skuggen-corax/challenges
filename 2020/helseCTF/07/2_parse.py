import dpkt
import base64
import zlib

with open('task.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)

    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        if isinstance(ip.data, dpkt.tcp.TCP):

            tcp = ip.data
            if tcp.data != b'':
                #print(i, ':\n', tcp.data.decode())
                
                data = tcp.data.decode().split('\n')
                if data[0][:7] == 'kylling':
                    pass #print('kylling!')
                elif data[0][:4] == 'POST':
                    pass #print('post!')
                else:
                    #print('\nNest:')
                    code = data[-1]
                    cbytes = base64.b64decode(code)
                    decomp = zlib.decompress(cbytes).decode('ascii')
                    if 'EGG' in decomp:
                        print(decomp)