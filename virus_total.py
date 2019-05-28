import requests

url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': 'e7416f0e54656ee951c464471fdea80e33e89e859d798eb158fdd713f7646d72', 'resource': 'fda487091f8a14b19e9eaeaef85215d7f03e54c2588754996c0cd9906d433b08'}

response = requests.get(url, params=params)

print(response.json())