import requests 

# flag_1: 1f3191fabf49137b4a1c8e41d2cb3730

base_url ="http://math:7070/challenge"
user_agent = {'User-Agent': 'Math Calculator (Python 3)'}

tall = set()
resultat = 0
i =0
while i < 1:
    r = requests.get(url = base_url, headers = user_agent)
    resultat = eval(r.text)

    print('#',i, r.url)
    print('#',i, r.text)
    print('#',i,'result:', resultat)
    if resultat in tall:
        print("hadde tallet:", resultat)
    tall.add(resultat)

    i+=1

answer = {challenge: r.text,
        result': int(resultat)}

r = requests.post(url = base_url, headers = user_agent, data = answer)

print(r)

#print(sorted(tall))