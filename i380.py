#i-380 twitter bot, use twitter api and maybe a weather api to give updates to drivers through twitter

import requests
import json
import pandas as pd
from collections import OrderedDict

#Twitter Keys and Info
API_KEY = "7oOHa8P5D8jxWR4uMOALqP09uW"
API_SECRET_KEY = "d5N5HGtxk0qRqYQcW1I89IWy1NRgt1Ipg6pKuQYqCT3knJBAMj"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANM4jgEAAAAAktJM2AIdj2sjTGXCovP3bHPnuQU%3DdutS5VkOVd0KWt3gtJPhgFZbvdXabIVH0tH8Pa6LRb8sL9OArQ"


Client_ID = 'MGZJa190ZVRfQk42UWFiTm9ib086MTpjaQ'
Client_Secret = 'RrPj4LY60uhrF7VGXsXEkSetRYOFj0AkzM2g-i2SQg1tkWmJV6'

#TomTom Traffic API Key
apiKey = "cbSYhP2tme3eZ8tXyzL3vixSxoDsBbM7"

bbox = "41.66380868562328,-91.65740394562818,41.920630394935166,-91.64610336406754"

response = requests.get('https://api.tomtom.com/traffic/services/4/incidentDetails/s3/'+bbox+'/22/-1/json?key='+apiKey+'&projection=EPSG4326&originalPosition=true')

dict = json.loads(response.content)
print(dict)
keys = dict.keys()
values = dict.values()

#split dict into keys and values
counter = 0
values = []
items = dict.items()
for item in items:
    counter +=1
    row = OrderedDict()
    row['tm']=values.append(item[1])


df = pd.DataFrame(values)
df = df["poi"].apply(pd.Series).unstack()
print(df)

collector = []
counter=0
for block in df:
    counter += 1
    row = OrderedDict()
    row['INCIDENT_ID'] = block['id']
    row['LONGITUDE'] = block['p'].get('x','')
    row['LATITUDE'] = block['p'].get('y','')
    row['ICON_CATEGORY'] = block['ic']
    row['MAGNITUDE_OF_DELAY'] = block['ty']
    row['CLUSTER_SIZE'] = block['cs']
    row['INCIDENT_DESCRIPTION'] = block['d']
    row['FROM'] = block['f']
    row['TO'] = block['t']
    row['LENGTH_METERS'] = block['l']
collector.append(row)
pdf = pd.DataFrame(collector)
print(pdf)
