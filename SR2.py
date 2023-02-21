import json
import requests

with open('serv.json') as file:
    data = json.load(file)
serv = data["server"]
port = data["port"]
request = f"http://{serv}:{port}"
response = requests.get(request)
res = response.json()
calc = res["calculated orbit"]
obs = res["observations"]
n = len(calc)
res = []
for i in range(n):
    l_c = (float(calc[i][0]) ** 2 + float(calc[i][1]) ** 2 + float(calc[i][2]) ** 2) ** 0.5
    l_o = (float(obs[i][0]) ** 2 + float(obs[i][1]) ** 2 + float(obs[i][2]) ** 2) ** 0.5
    count = round(abs(l_c - l_o), 2)
    res.append(str(count))
print(' '.join(res))
