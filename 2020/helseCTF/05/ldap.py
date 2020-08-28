from collections import Counter

with open('ldap.log') as f:
    data = [line for line in f.readlines()]

users = []

for line in data:
    if ',ou=users,dc=pasientjournal,dc=ctf" "entry" requested' in line:
        users.append(line.split("=")[2].split(',')[0])

userset = set(users)
usercounter = Counter(users)


print(usercounter.most_common(6))
#print('antall brukere:', len(users))