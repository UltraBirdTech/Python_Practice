# virus total API にリクエストを送る
# 学ぶポイント
# 1. 外部ライブラリのimport方法
# 2. 外部へのリクエスト方法

import urllib.request
import urllib.error
import urllib.parse
import json

import sys

VIRUS_TOTAL_REPORT_API_URL = 'https://www.virustotal.com/vtapi/v2/file/report'


def main():

    argv = sys.argv

    if len(argv) < 2:
        print('[ERROR]: 引数が足りません。引数としてファイルのハッシュ値を与えてください。')
        exit()

    try:
        api_key = apikey()
        response = request(argv[1], api_key)
        j = json.loads(response.read().decode('utf-8'))
        display(j)
    except FileNotFoundError as err:
        print('[ERROR]: api keyが記述されているファイルが存在しません。')
        print('[ERROR]: ファイルパスに"api_key.txt"を配置してください。')

    except Exception as err:
        print('[ERROR]: エラーが発生しました。' + str(err))


def apikey():
    api_key_file_path = './api_key.txt'
    with open(api_key_file_path) as f:
        read = f.read()
    api_key = read.replace('\n', '')
    print('[LOG] api key: ' + api_key)
    return api_key


def request(sha256, api_key):
    param = {'resource': sha256, 'apikey': api_key}
    data = urllib.parse.urlencode(param)
    req = urllib.request.Request(VIRUS_TOTAL_REPORT_API_URL, data.encode())
    return urllib.request.urlopen(req)

def display(j):
    print('[Hash Value]:' + str(j['resource']))
    print('[Message]:' + str(j['verbose_msg']))

    if j['response_code'] == 0:
        print('[ERROR]: Request is Fail')
        print('ファイルの参照に失敗しました。')
    else:
        print('[SUCCSESS]: Request is Succsess')
        for k, v in j['scans'].items():
            print('=' * 50)
            print('Vender Name:' + str(k))
            for key, value in v.items():
                print(str(key) + ':' + str(v[key]))


main()
