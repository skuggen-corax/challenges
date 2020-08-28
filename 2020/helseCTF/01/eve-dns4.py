import json
import locale

with open('eve-dns.json') as json_file:
    data = json.load(json_file)

other = ""
admindoms = ""
content = []
for record in data:
    if record["dns"]["type"] == "answer" and record["dns"]["rrtype"] == "TXT":
        if "answers" in record["dns"]:
            domain = record["dns"]["rrname"].split('.')
            if len(domain[0]) == 15:
                dom = domain[0][11:]
                admindoms += dom
                content.append([int(dom, 16), record["dns"]["answers"][0]["rdata"]])
            else:
                dom = domain[0]
                other += record["dns"]["answers"][0]["rdata"]
            #print(dom, ' - ', record["dns"]["answers"][0]["rdata"])

hexstring = ""
content = sorted(content, key=lambda x: x[0])
for element in content:
    hexstring += element[1].replace(' ', '')

#print(hexstring)
filebytes = bytes.fromhex(hexstring)

with open('eve-dns4b.png', 'wb') as file:
    file.write(filebytes)

print('Extracted image: eve-dns4b.png')
print('Now, manually get script from eve-dns4b.png')
print('then run: python <script from eve-dns4b.png>', other.split('=')[1])