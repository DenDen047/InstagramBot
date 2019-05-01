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
    target_user_id = "daisuke_clover"
    media_ids = bot.get_user_medias(
        user_id=target_user_id,
        filtration=None,
        is_comment=None
    )
    media_id = media_ids[0]

    # download photo
    dummy_file = os.path.join(DATA_DIR, "dummy")
    bot.download_photo(
        media_id,
        filename=dummy_file
    )
    dummy_file += '.jpg'

    # キャプション準備
    tags = ["#tokyo", "#awesomeplaces"]
    caption = "どこだか分かる？\n\n"
    caption += 'Credit: @{}\n\n'.format(target_user_id)
    caption += ' '.join(tags)

    # upload photo
    result = bot.upload_photo(
        dummy_file,
        caption=caption)
    print(result)


if __name__ == '__main__':
    main()