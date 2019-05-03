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

    # 参考アカウントをロード
    accounts_file = os.path.join(CONFIG_DIR, 'accounts.txt')
    account_list = []
    with open(accounts_file, 'r') as f:
        for i in f:
            account_list.append(i.rstrip('\n'))
    target_user_id = random.choice(account_list)

    # タグ情報をロード
    num_tag = 30
    tags_file = os.path.join(CONFIG_DIR, 'tags.txt')
    tag_list = []
    with open(tags_file, 'r') as f:
        for i in f:
            tag_list.append(i.rstrip('\n'))
    tags = random.sample(tag_list, num_tag) # タグをランダムに選択

    # Login
    bot = Bot(
        base_path=LOG_DIR,
        comments_file=os.path.join(CONFIG_DIR, 'comments.txt')
    )
    bot.login(username=username, password=password)

    # 他人の画像情報を取得
    media_ids = bot.get_user_medias(
        user_id=target_user_id,
        filtration=False
    )
    media_id = media_ids[0]
    print('Media ID: {}'.format(media_id))

    # 画像をダウンロード
    dummy_file = os.path.join(DATA_DIR, "dummy")
    bot.download_photo(
        media_id,
        filename=dummy_file
    )

    # 引用する旨を伝える
    bot.comment_medias([media_id])

    # キャプション準備
    caption = "Who can name this spot?\nどこだか分かる？\n\n"
    caption += 'Credit: @{}\n\n'.format(target_user_id)
    caption += ' '.join(tags)
    print(caption)

    # upload photo
    dummy_files = glob.glob(os.path.join(DATA_DIR, "*.jpg"))
    dummy_files.sort()
    dummy_file = dummy_files[0]
    result = bot.upload_photo(
        dummy_file,
        caption=caption)

    # 不要な画像を削除
    for f in dummy_files:
        os.remove(f)
    files = glob.glob(os.path.join(DATA_DIR, "*.REMOVE"))
    for f in files:
        os.remove(f)

if __name__ == '__main__':
    main()