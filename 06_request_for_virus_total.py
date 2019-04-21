# virus total API にリクエストを送る
# 学ぶポイント
# 1. 外部ライブラリのimport方法
# 2. 外部へのリクエスト方法

import urllib.request
import urllib.error
import urllib.parse

import sys

argv = sys.argv

virus_total_api_url = 'https://www.virustotal.com/vtapi/v2/file/report'

# api_key
api_key = ''

data_sha256 = argv[1]
param = {'resource': data_sha256, 'apikey': api_key}
data = urllib.parse.urlencode(param)
req = urllib.request.Request(virus_total_api_url, data.encode())
response = urllib.request.urlopen(req)

json = json.loads(response.read().decode('utf-8')
print(json)
