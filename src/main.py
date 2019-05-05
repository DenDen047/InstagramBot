import os
import sys
import re
import glob
import json
import random
from datetime import datetime

from instabot import Bot


DATA_DIR = "/data"
LOG_DIR = "/log"
CONFIG_DIR = "/configs"

# 初期設定
random.seed(datetime.now())


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
    print('User ID: @{}'.format(target_user_id))

    # キャプション情報をロード
    num_tag = 30
    captions_file = os.path.join(CONFIG_DIR, 'captions.txt')
    caption_list = []
    with open(captions_file, 'r') as f:
        for i in f:
            caption_list.append(i.rstrip('\n'))
    caption = random.choice(caption_list)

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
    media_id = random.choice(media_ids)
    media_id = 2034143614828840178
    print('Media ID: {}'.format(media_id))
    ## 画像のリンク元からキャプションを取得
    media_info = bot.get_media_info(media_id)
    caption_text = media_info[0]['caption']['text']
    ## キャプションから正規表現で引用元を特定
    repatter = re.compile(pattern)
    result = repatter.match(content)
    source_users = [target_user_id] # 引用元のuser id

    # 画像をダウンロード
    dummy_file = os.path.join(DATA_DIR, str(media_id))
    bot.download_photo(
        media_id,
        filename=dummy_file
    )

    # キャプション準備
    caption += "\n\n"
    caption += 'Credit: @{}\n\n'.format('\@'.join(source_users))
    caption += ' '.join(tags)
    print(caption)

    # # upload photo
    # dummy_files = glob.glob(os.path.join(DATA_DIR, "*.jpg"))
    # dummy_files.sort()
    # dummy_file = dummy_files[0]
    # result = bot.upload_photo(
    #     dummy_file,
    #     caption=caption)
    # print('Upload: {}'.format(result))

    # if result:
    #     # 引用する旨を伝える
    #     bot.comment_medias([media_id])

    # 不要な画像を削除
    for f in dummy_files:
        os.remove(f)
    files = glob.glob(os.path.join(DATA_DIR, "*.REMOVE*"))
    for f in files:
        os.remove(f)

if __name__ == '__main__':
    main()