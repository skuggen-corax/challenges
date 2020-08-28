import json
import hashlib
import locale

with open('eve-dns.json') as json_file:
    data = json.load(json_file)

subdomains = []
for record in data:
    if record["dns"]["type"] == "answer" and record["dns"]["rrname"] not in subdomains and "rd" not in record["dns"]:
        subdomains.append(record["dns"]["rrname"])

#locale.setlocale(locale.LC_COLLATE, "en_US.UTF-8")
subdomains.sort(key=locale.strxfrm) # faktisk viktig for A sortere som gjort i oppgaven
dom = "".join(dom for dom in subdomains)
print('EGG{',hashlib.md5(dom.encode()).hexdigest(), '}', sep="")

'''
Oppdatering:
Vi ønsker unike,
sorterte subdomener av journalsystem.ctf OG journelsystem.ctf
som er gjort uten "recursion desired"-bit satt.
'''
