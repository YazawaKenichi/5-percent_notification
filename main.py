#!/usr/bin/env python3
# coding : utf-8

import requests
from optparse import OptionParser

class LINENotifyBot():
    API_URL = "https://notify-api.line.me/api/notify"

    # コンストラクタ
    def __init__(self, token):
        # ヘッダの設定
        self.__headers = {"Authorization" : f"Bearer {token}"}

    # 送信処理
    def send(self, message, image = None, sticker_package_id = None, sticker_id = None):
        # パラメータ
        payload = {
                "message" : message,
                "stickerPackageId" : sticker_package_id,
                "stickerId" : sticker_id
                }
        files = {}
        # 画像ファイルが指定されている場合は読み込み
        if image != None:
            files = {"imageFile" : open(image, "rb")}
        # 送信
        r = requests.post(LINENotifyBot.API_URL, headers = self.__headers, data = payload, files = files)

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

if __name__ == "__main__":
    optiondict, args = get_args(ui = False)
    UI = optiondict.visible
    # 送信先 URL
    access_token = args[0]
    # メッセージ
    message = "Hello, World!"
    # インスタンス化
    bot = LINENotifyBot(token = access_token)
    # 送信
    bot.send(message = message, image = None, sticker_package_id = None, sticker_id = None)



