import os
import sys
import re
import glob
import json

from InstagramAPI import InstagramAPI


def main():
    # アカウント情報をロード
    with open('account_info.json', 'r') as f:
        data = json.load(f)
        login = data['login']
        password = data['password']

    # ログインテスト
    api = InstagramAPI(login, password)
    if (api.login()):
        api.getSelfUserFeed()  # get self user feed
        # print(api.LastJson)  # print last response JSON
        print("Login succes!")
    else:
        print("Can't login!")



if __name__ == '__main__':
    main()