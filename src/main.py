import os
import sys
import re
import glob
import json

from instabot import Bot


DATA_DIR = "../data"


def main():
    # アカウント情報をロード
    with open('account_info.json', 'r') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']


    bot = Bot()
    bot.login(username=username, password=password)
    user_id = bot.get_user_id_from_username("lego")
    user_info = bot.get_user_info(user_id)
    print(user_info['biography'])



if __name__ == '__main__':
    main()