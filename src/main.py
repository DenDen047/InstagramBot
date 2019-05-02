import os
import sys
import re
import glob
import json
import random

from instabot import Bot


DATA_DIR = "/data"
LOG_DIR = "/log"
CONFIG_DIR = "/configs"


def main():
    # アカウント情報をロード
    with open('account_info.json', 'r') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']

    # アカウント情報をロード
    accounts_file = os.path.join(CONFIG_DIR, 'accounts.txt')
    account_list = []
    with open(accounts_file, 'r') as f:
        for i in f:
            account_list.append(i.rstrip('\n'))
    target_user_id = random.choice(account_list)

    # Login
    bot = Bot(
        base_path=LOG_DIR,
        comments_file=os.path.join(CONFIG_DIR, 'comments.txt')
    )
    bot.login(username=username, password=password)

    # 他人の画像をダウンロード
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

    # 引用する旨を伝える
    bot.comment_medias([media_id])

    # キャプション準備
    tags = ["#tokyo", "#awesomeplaces"]
    caption = "どこだか分かる？\n\n"
    caption += 'Credit: @{}\n\n'.format(target_user_id)
    caption += ' '.join(tags)

    # upload photo
    dummy_file = glob.glob(os.path.join(DATA_DIR, "*.jpg"))[0]
    result = bot.upload_photo(
        dummy_file,
        caption=caption)


if __name__ == '__main__':
    main()