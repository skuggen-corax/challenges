with open('s8file', 'rb') as f:
    f.read(7)
    linen = 0 

    #f.read(1) # to get "unaligned" stuff
    #linen = 1
    while(byte := f.read(2)):
        print(hex(linen)+':\t', hex(byte[0]), hex(byte[1]), '\t', end="")

        if byte[0] & 15 == 1:
            # set to val
            print('SETT r' + str(byte[0] >> 4) + ',', hex(byte[1]), ';', byte[1])
        
        elif byte[0] & 15 == 2:
            # set to reg
            print('SETT r' + str(byte[0] >> 4) + ',', 'r'+str(byte[1]))

        elif byte == b'\x00\x00':
            print('STOPP')

        elif byte[0] & 15 == 3:
            print('FINN', '0x'+ str(byte[1]) + "{:X}".format((byte[0] >> 4)))

        elif byte[0] & 15 == 4:
            # last / lagr
            if byte[0] >> 4 == 0:
                print('LAST', 'r'+str(byte[1] & 15))
            elif byte[0] >> 4 == 1:
                print('LAGR', 'r'+str(byte[1] & 15))
            else:
                print(hex(byte[0]), hex(byte[1]), '  \t\t Ukjent last/lagre opkode')

        elif byte[0] & 15 == 5:
            # comparators
            if byte[0] >> 4 == 0:
                print('OG', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4) )
            elif byte[0] >> 4 == 1:
                print('ELLER', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 2:
                print('XELLER', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 3:
                print('VSKIFT', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 4:
                print('HSKIFT', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 5:
                print('PLUSS', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 6:
                print('MINUS', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            else:
                print(hex(byte[0]), hex(byte[1]), '  \t\t Ukjent logi opkode')

        elif byte[0] & 15 == 6:
            # les/skriv
            if byte[0] >> 4 == 0:
                print('LES', 'r'+str(byte[1]))
            elif byte[0] >> 4 == 1:
                print('SKRIV', 'r'+str(byte[1]))
            else:
                print(hex(byte[0]), hex(byte[1]), '  \t\t Ukjent IO opkode')

        elif byte[0] & 15 == 7:
            # comparators
            if byte[0] >> 4 == 0:
                print('LIK', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4) )
            elif byte[0] >> 4 == 1:
                print('ULIK', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 2:
                print('ME', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 3:
                print('MEL', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 4:
                print('SE', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            elif byte[0] >> 4 == 5:
                print('SEL', 'r'+str(byte[1] & 15) + ', r'+str(byte[1] >> 4))
            else:
                print(hex(byte[0]), hex(byte[1]), '  \t\t Ukjent comp opkode')
            
        elif byte[0] & 15 == 8:
            print('HOPP', '0x'+ "{:X}".format(byte[1]) + "{:X}".format((byte[0] >> 4)))
            # hopp
        elif byte[0] & 15 == 9:
            # bhopp
            print('BHOPP', '0x'+ "{:X}".format(byte[1]) + "{:X}".format((byte[0] >> 4)))

        elif byte[0] & 15 == 10: # 'a'
            print('TUR', '0x'+ "{:X}".format(byte[1]) + "{:X}".format((byte[0] >> 4)))

        elif byte[0] & 15 == 11: # 'b'
            print('RETUR')

        elif byte[0] & 15 == 12: # 'c'
            print('NOPE')

        else:
            print(hex(byte[0]), hex(byte[1]), '  \t\t Ukjent opkode')
        
        linen +=2
