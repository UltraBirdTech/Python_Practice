# virus total API にリクエストを送る
# 学ぶポイント
# 1. 外部ライブラリのimport方法
# 2. 外部へのリクエスト方法
# 3. エラーの処理

import requests
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
        data = response.json()
        display(data)
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
    params = {'resource': sha256, 'apikey': api_key}
    response = requests.get(VIRUS_TOTAL_REPORT_API_URL, params=params)
    return response


def display(data):
    print('[Hash Value]:' + str(data['resource']))
    print('[Message]:' + str(data['verbose_msg']))

    if data['response_code'] == 0:
        print('[ERROR]: Request is Fail')
    else:
        print('検知率:' + str(data['positives']) + '/' + str(data['total']))
        print('[SUCCESS]: Request is Success')
        for k, v in data['scans'].items():
            print('=' * 50)
            print('Vender Name:' + str(k))
            for key, value in v.items():
                print(str(key) + ':' + str(value))

if __name__ == '__main__':
    main()
