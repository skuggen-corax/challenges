import json
import hashlib 

with open('eve-dns.json') as json_file:
    data = json.load(json_file)

subdomain = []
for record in data:
    record["dns"]["rrname"].split(".")
    if record["dns"]["rrname"].split(".")[1] == 'journalsystem':
        subdomain.append(record["dns"]["rrname"].split(".")[0])

subdomains = set(subdomain)

print('EGG{',hashlib.md5(str(len(subdomains)).encode()).hexdigest(), '}', sep="")