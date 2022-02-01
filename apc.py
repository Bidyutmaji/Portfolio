import requests
import schedule
import json
from django.conf import  settings
import os


# def sched():
#     rk = requests.get('https://api.mfapi.in/mf').json()
#     apc_path = os.path.join(settings.MODELS, 'apc.json')

#     with open(apc_path, 'w') as jps:
#         json.dump(rk, jps)
#         print('Radhe Shyam!')
with open(r'C:\Radha-Madhava\Portfolio\models\apc.json', 'r') as jps:
    gn = json.load(jps)
# print(len(gn))

# schedule.every().day.at('11:46').do(sched)

# while True:
#     schedule.run_pending()

# schedule.every().day.at("05:47").do(job)\

for i in gn:
    # print(i)
    break
# print(gn[0]['schemeCode'])

jps = [e['schemeName'] for e in gn]
ekadashi = lambda e: 'quant small direct' in e
print(list(filter(ekadashi, jps)))

# filter()
# print(jps)

# class MutualFund:
#     def __init__(self, ):
        

print(5+True)
# print(long(12)+12)
print(dict({'z': 3, 'x': 1, 'y': 2}))

l = ['a','bb','dddd','ccc']
print(sorted(l))

for apc in os.listdir(r'C:\Radha-Madhava\Portfolio\models'):
    print(apc)