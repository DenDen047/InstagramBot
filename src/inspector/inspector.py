import os
import sys
import re
import glob
import json
import random
from datetime import datetime

from instabot import Bot


SAMPLES_DIR = "/samples"


def main():
    # prepare bot
    with open('../account_info.json', 'r') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']

    bot = Bot(
        base_path=LOG_DIR,
        comments_file=os.path.join(CONFIG_DIR, 'comments.txt')
    )
    bot.login(username=username, password=password)

    # get url
    url = ''

    # get media id

    # get media info

    # output as a file

if __name__ == '__main__':
    main()