from string import ascii_lowercase, ascii_uppercase, digits

rotor = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']

tekst = "NKC FKT RTVCNIJA, MXFKP HHL CC FKMAOD XÆUEUR. ICYØB PCSÅ MUUN TKJ OD TØ ROOAD, ZF OÅØØUYGHÅ NCÆ LMQ NHP C IPKVO: ZSVHBXITB"
svar? = "HEI DIN LURIFAKS, KODEN FÅR DU GANSKE STRAKS. FØRST LITT GRØT JEG MÅ NÅ SPISE, OG PASSORDET FÅR DET TIL Å GLISE: SPRETTERT"
mod = [ -6,-6,6,0,  -2,-2,-6,0,  -6,1,-4,6,-8,-8,1,-10,0,0,
        -2,-8,-2,-6,-2,0,  -2,-8,6,0,  1,-10,0,  1,-10,1,-10,-4,1,0,  -4,-6,-3,-4,-10,1,0,0,
        -3,-4,-6,-8,-10,0,  -4,6,1,-8,0,  -6,-3,6,6,0,  -10,-6,-3,0,  -2,-4,0,  -6,1,0,  1,1,-6,-10,1,0,0,
        -10,1,0, 1,1,-8,-8,-6,-6,-3,-3,-8,0,  -8,-3,-8,0,  -8,-8,-10,0,  6,1,-4,0,  -3,0,  -2,-4,-2,-3,-10,0,0,
        -6,-3,-4,-3,-10,-3,-4,-2,-10]

def transpose(char, key):
    if char.isupper():
        alph = ascii_uppercase + 'ÆØÅ'
    else:
        return char
    
    if alph.index(char) + key < 0:
        key -= 1

    return alph[(alph.index(char) + key) % len(alph)]


result = ""
i = 0
while i < len(tekst):
    result += transpose(tekst[i], mod[i])

    i +=1

print(result)