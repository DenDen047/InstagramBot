import os
import sys
import re
import glob
import json

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


def main():
    # アカウント情報をロード
    with open('account_info.json', 'r') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']

    # set workspace folder at desired location (default is at your home folder)
    set_workspace(path=None)

    # get an InstaPy session!
    session = InstaPy(
        username=username,
        password=password
    )

    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_dont_include(["friend1", "friend2", "friend3"])

        # activity
        session.like_by_tags(["natgeo"], amount=10)



if __name__ == '__main__':
    main()