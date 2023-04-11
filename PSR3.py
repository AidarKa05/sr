import requests
import json
import datetime

date = [int(el) for el in input().split('/')]
'''with open('space_life.json') as f:
    data = json.load(f)
host = data["host"]
port = data["port"]
response = requests.get(f'{host}:{port}')
json_res = response.json()
print(json_res)'''
data = [
{"ship": "Ural", "rest_time": 19.8, "date": "2023/04/02 11:54"},
{"ship": "Giant", "rest_time": 111.0, "date": "2023/03/30 8:13"},
{"ship": "Nigella", "rest_time": 12.4, "date": "2023/04/01 13:02"},
{"ship": "Far Stranger", "rest_time": 24, "date": "2023/03/31 21:54"},
{"ship": "Thunder", "rest_time": 56.8, "date": "2023/04/01 3:12"}
]
res = []
for i in range(len(data)):
    a = datetime.datetime(*date)
    dt, tm = data[i]['date'].split(' ')
    dtm = [int(el) for el in dt.split('/')] + [int(el) for el in tm.split(':')]
    b = datetime.datetime(*dtm)
    dlt = a - b
    pol = float(data[i]['rest_time'])
    rdlt = dlt.seconds/3600 + dlt.days*24
    if (pol - rdlt <= 24) and (pol - rdlt > 0):
        res.append(data[i]['ship'])
res.sort()
print(res)
