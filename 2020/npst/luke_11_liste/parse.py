import re, string, sqlite3

conn = sqlite3.connect('liste.db')
c = conn.cursor()

susp_md5s = []
#skrive ce ... d8

with open('copy.db-wal', 'rb') as f:
    s = f.read()
    
    offset = 0
    while offset >= 0:
        offset = s.find(b'\x4d', offset+4)
        
        if offset == -1:
            break # iukke flere records

        # masse forskjellige stop bytes? rot
        eoffset = s.find(b'\x8a', offset)

        if eoffset == -1:
            eoffset = s.find(b'\xd8', offset)
        
        if eoffset > s.find(b'\x00\x00\x00', offset+4) and s.find(b'\x00\x00\x00', offset+4) != -1:
            #print(0)
            eoffset = s.find(b'\x00\x00\x00', offset) + 1

        if eoffset > s.find(b'\x00\x00\x04', offset+4) and s.find(b'\x00\x00\x04', offset+4) != -1:
            #print('04')
            eoffset = s.find(b'\x00\x00\x04', offset) +1

        if eoffset > s.find(b'\x27\x4d', offset+4) and s.find(b'\x27\x4d', offset+4) != -1:
            #print('3')
            eoffset = s.find(b'\x27\x4d', offset+4) -4

        if eoffset > s.find(b'\x8b', offset+4) and s.find(b'\x8b', offset+4) != -1:
            #print('a')
            eoffset = s.find(b'\x8b', offset)

        # some incremental stop bytes: ce->d8
        for i in range(206, 217):
            byte = bytearray()
            byte.append(i)
            
            if eoffset > s.find(byte, offset+4) and s.find(byte, offset+4) != -1:
                #print(bytes(byte))
                eoffset = s.find(byte, offset)

        #print(eoffset, offset, eoffset - offset) # for debug
        if s[offset+1:offset+2] in [c.encode() for c in string.ascii_uppercase]:
            if eoffset != -1:
                parsed = re.split('(?=[A-Z])', s[offset+1:eoffset-33].decode())[1:] + [s[eoffset-33:eoffset-1].decode()] # + [len(s[eoffset-33:eoffset-1].decode())])
                
            else:
                parsed = re.split('(?=[A-Z])', s[offset+1:eoffset-31].decode())[1:] + [s[eoffset-31:].decode()] # + [len(s[eoffset-31:].decode())])
            
            first = parsed[0]
            last = parsed[1]
            md5 = parsed[2]

            # noen md5 i wal som ikke passer med md5 i .db?
            c.execute('SELECT * FROM snille WHERE fornavn=? and etternavn=?', (first, last))
            fetched_md5 = c.fetchone()[2]
            if md5 != fetched_md5:
                susp_md5s.append(md5)
                susp_md5s.append(fetched_md5)
                print('different md5:', first, last, 'wal:', md5, 'db:', fetched_md5)

            # noen snille md5 som er i slemme?
            c.execute('SELECT * FROM slemme WHERE md5=?', (md5,))
            alt = c.fetchall()
            if len(alt) > 0:
                print(alt)

            # noen md5 som har mer enn 1 snill?
            c.execute('SELECT * FROM snille WHERE md5=?', (md5,))
            alt = c.fetchall()
            if len(alt) > 1:
                print(alt)

# sjekke mistenkelige md5s
print('suspect md5s:',susp_md5s)

for md5hash in susp_md5s:
    c.execute('SELECT * FROM snille WHERE md5=?', (md5hash,))
    match = c.fetchone()
    print('susp-match in snille for', md5hash, ':', match)

for md5hash in susp_md5s:
    c.execute('SELECT * FROM slemme WHERE md5=?', (md5hash,))
    match = c.fetchone()
    print('susp-match in slemme for', md5hash, ':', match)


print('flagg: PST{' + susp_md5s[0] + '}')

conn.close()