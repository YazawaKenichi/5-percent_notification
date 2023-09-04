#!/usr/bin/env python3
# coding : utf-8

import tweepy
from optparse import OptionParser

def get_args(ui = False):
    usage = "%prog ACCESS_TOKEN [-v]"
    parser = OptionParser(usage = usage)

    parser.add_option(
            "-v",
            action = "store_true",
            default = False,
            dest = "visible",
            help = "デバッグモード"
            )
    return parser.parse_args()

def post_tweet(ck, cs, at, ats, msg):
    client = tweepy.Client(consumer_key=ck, consumer_secret=cs, access_token=at, access_token_secret=ats)
    client.create_tweet(text=msg)

if __name__ == "__main__":
    optiondict, args = get_args(ui = False)
    UI = optiondict.visible

    consumer_key = args[0]
    consumer_secret = args[1]
    access_token = args[2]
    access_secret = args[3]
    bearer_token = args[4]
    client_id = args[5]
    client_secret = args[6]

    message = "hoge"

    post_tweet(consumer_key, consumer_secret, access_token, access_secret, msg = message)


