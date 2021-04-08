import os, random


# Meldingene er på engelsk, med store bokstaver og mellomrom.
meldinger = [
    ??????
    ??????
    ...
    ??????
    ??EGG{...???...}???
]
random.shuffle(meldinger)

secret = os.urandom(128)

def xor(a, b):
    l = min(len(a), len(b))
    return bytes(x ^ y for x, y in zip(a[0: l], b[0: l]))

for plaintext in meldinger:
    assert len(plaintext) < len(secret)
    w = xor(plaintext, secret)
    print(w.hex())


