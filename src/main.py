import os
import sys
import re
import glob
import json

from instabot import Bot


DATA_DIR = "/data"
LOG_DIR = "/log"


def main():
    # アカウント情報をロード
    with open('account_info.json', 'r') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']

    # Login
    bot = Bot(base_path=LOG_DIR)
    bot.login(username=username, password=password)
    user_id = bot.get_user_id_from_username("lego")
    user_info = bot.get_user_info(user_id)
    print(user_info['biography'])

    # download pic
    bot.download_photo(
        "123", filename=os.path.join(DATA_DIR, "somefile.jpg"))


if __name__ == '__main__':
    main()