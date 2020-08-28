import json

ports = []

with open('eve-flow.json') as json_file:
    data = json.load(json_file)

for record in data:
    if record["dest_ip"] == "172.30.0.2":
        if int(record['dest_port']) not in ports:
            ports.append(int(record['dest_port']))

ports.sort()

ports = set(ports)

print(len(ports))