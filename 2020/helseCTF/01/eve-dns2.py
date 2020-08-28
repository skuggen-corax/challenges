import json

subdomain = []

with open('eve-dns.json') as json_file:
    data = json.load(json_file)

for record in data:
    if record["dns"]["type"] == "answer" and record["dns"]["rrtype"] == "A" and record["dns"]["rcode"] == "NOERROR":
        record["dns"]["rrname"].split(".")
        if record["dns"]["rrname"].split(".")[1] == 'journalsystem':
            if record["dns"]["rrname"] not in subdomain:
                subdomain.append(record["dns"]["rrname"]) # + '>'

doms = "".join(dom for dom in subdomain)
#subdomains = set(subdomain)

print(doms, end = "")

#print('antall: ',len(subdomain))


#"type" == "answer"
#"rrtype": == "A"
#"rcode":"NOERROR"
#concat