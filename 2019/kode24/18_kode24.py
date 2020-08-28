recode = dict()
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']

i = 0
for i in range(len(alfabet)):
    recode[alfabet[i]] = alfabet[-(i+1)]
    #print(alfabet[i], alfabet[-(i+1)])

omvendt_alfabet = alfabet.reverse()
koda_setning = 'vårrå, joq vyl! tyw vål rclj qyw a sozy!!! ror os, zåwypk nåkkolz yl zåpkykryjjå. zyj yl zyp kryjjå onny hyz øolwakyp zyl, hyuji. kpåsyk op å nråpy! fofo'
recode[','] = ','
recode[' '] = ' '
recode['!'] = '!'
recode['.'] = '.'

for c in koda_setning:
    print(recode[c])
