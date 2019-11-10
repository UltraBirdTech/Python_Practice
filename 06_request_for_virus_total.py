# virus total API にリクエストを送る
# 学ぶポイント
# 1. 外部ライブラリのimport方法
# 2. 外部へのリクエスト方法
# 3. エラーの処理

import requests
import sys
from sys import argv

VIRUS_TOTAL_REPORT_API_URL = 'https://www.virustotal.com/vtapi/v2/file/report'


def main():

    argv = sys.argv

    if len(argv) < 2:
        print('[ERROR]: 引数が足りません。引数としてファイルのハッシュ値を与えてください。')
        exit()

    try:
        response = request(argv[1])
        check_status_code(response.status_code)
        data = response.json()
        display(data)
    except FileNotFoundError as err:
        print('[ERROR]: api keyが記述されているファイルが存在しません。')
        print('[ERROR]: ファイルパスに"api_key.txt"を配置してください。')
    except RequestError as err:
        print('[ERROR]: ' + err.status_code)
        print('[USAGE]: ' + 'Please look API reference "' + err.reference_url + '"')
    except Exception as err:
        print('[ERROR]: エラーが発生しました。' + str(err))


def apikey():
    api_key_file_path = './api_key.txt'
    with open(api_key_file_path) as f:
        read = f.read()
    api_key = read.replace('\n', '')
    print('[LOG] api key: ' + api_key)
    return api_key


def request(sha256):
    params = {'resource': sha256, 'apikey': apikey()}
    response = requests.get(VIRUS_TOTAL_REPORT_API_URL, params=params)
    return response


def check_status_code(status_code):
    if status_code == 200:
        return

    raise RequestError(status_code)


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

class RequestError(Exception):
    def __init__(self, status_code):
        self.status_code = str(status_code)
        self.reference_url = 'https://developers.virustotal.com/reference#api-responses'


if __name__ == '__main__':
    main()
