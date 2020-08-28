#PPK rebus:
#ROT(5)
input = "KNO fmwggkymyioån 30å6ø8432æå54710a9æ09a305å7z9829 fmwggkymyioån ngpoo"
#result "PST krøllparantes 30e6d8432ce54710f9c09f305e7b9829 krøllparantes slut"

dont = [' ','1','2','3','4','5','6','7','8','9','0']
rotor = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å','A','B','C','D','E','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','æ','ø','å','a','b','c','d','e']

result = ""
i = 0
while i < len(input):
    c = input[i]
    if c not in dont:
        idx = rotor.index(c)
        result += rotor[idx+5]
    else:
        result += c
    i +=1

print(result)
