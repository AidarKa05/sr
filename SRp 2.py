import json
import requests
import csv

with open('migration.json') as migration:
    data = json.load(migration)

request = f"https://{data['serv']}:{data['gate']}"
response = requests.get(request)

kind = response[data['kind']]

rows = []

for d in kind:
    have = False
    if d['size'] >= data['min_size']:
        for i in range(len(rows)):
            if d['place'] == rows[i]['place'] and d['size'] == rows[i]['size']:
                rows[i]['total'] += d['amount']
                have = True
            if not have:
                rows. append({
                    'place': d['place'],
                    'size': d['size'],
                    'total': d['amount']
                })

rows.sort(key=lambda x: (-x['total'], x['place']))

with open('butterflies.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='*')
    writer.writerow(['place', 'size', 'total'])
    for i in rows:
        writer.writerow([i['place'], i['size'], i['total']])
