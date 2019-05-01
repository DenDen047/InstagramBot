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

    # 他人の画像をダウンロード
    user_id = bot.get_user_id_from_username("daisuke_clover")
    media_ids = bot.get_user_medias(
        user_id="daisuke_clover",
        filtration=None,
        is_comment=None
    )
    print(media_ids)

    # 借用することをコメントs

    # download photo
    # bot.download_photo(
    #     "123", filename=os.path.join(DATA_DIR, "somefile"))

    # upload photo
    # result = bot.upload_photo(
    #     os.path.join(DATA_DIR, "test2.jpg"),
    #     caption="Credit: {}\n#tokyo")
    # print(result)


if __name__ == '__main__':
    main()