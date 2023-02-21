import sys
import json

same = {}
diff = {}
for line in sys.stdin:
    hr, num = line.rstrip('\n').split(' ** ')
    if (num < 100) and (num > 9) and (num % 2 == 0):
        same[hr] = num
    else:
        diff[hr] = num

js = {'same': same, 'different': diff}

with open('ocean.json', 'w') as f:
    json.dump(js, f)
