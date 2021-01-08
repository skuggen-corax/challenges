import gzip

with open('luke_9_hexcode.txt') as f:
    hexcode = [line for line in f.readlines()] # lagret på tre linjer

mapping = hexcode[0].strip()    #"🎅🤶❄⛄🎄🎁🕯🌟✨🔥🥣🎶🎆👼🦌🛷"
message = hexcode[2].strip()    #"🤶🛷✨🎶🎅✨🎅🎅🛷🤶🎄🔥🎆🦌🎁🛷🎅❄🛷🛷🎅🎶🎅✨🎅🦌🥣🔥🛷🦌⛄🎅🌟🛷🛷🔥🎄🦌🎅✨🦌🦌🕯🎶🎅🤶🦌❄🎁🕯🎅✨🎶👼🌟🎆🕯🌟❄👼🎅🎅🤶❄🎄👼🎆🔥🎁🛷🤶👼🎅🎅🎅🎅🎅🎅"

hexstring = ["{0:01x}".format(mapping.index(char)) for char in message]

# strange bytes ... gzip?
print(gzip.decompress(bytes.fromhex("".join(hexstring))).decode())