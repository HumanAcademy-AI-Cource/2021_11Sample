#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリをインポート
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import rospy
from std_msgs.msg import String

# チャットメッセージを受け取るノードのクラス
class Uketoru():
    def __init__(self):
        # トピック名を保持する変数を作成
        self.topic_name = "/chat_message"
        # サブスクライバーを定義
        rospy.Subscriber(self.topic_name, String, self.callback)
        # 受け取ったデータを保持する変数を初期化
        self.text = ""
        
    def callback(self, msg):
        """
        サブスクライブしたデータを受け取る関数
        """

        # 受け取ったデータを保持する
        self.text = msg.data

    def run(self):
        """
        一連の処理を行う関数
        """

        # 白紙の画像を作成
        image = np.full((100, 400, 3), 255, np.uint8)
        # PILライブラリ用の画像に変換
        image = Image.fromarray(image)
        # 文字を書くための準備
        draw = ImageDraw.Draw(image)
        # 使用するフォントを指定
        font = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 14)
        # 各項目の情報をテキストで書く
        draw.text((5,5), unicode("ノード名：" + rospy.get_name(), 'utf-8'), font=font, fill=(0, 0, 0, 0))
        draw.text((5,30), unicode("トピック：" + self.topic_name, 'utf-8'), font=font, fill=(0, 0, 0, 0))
        draw.text((5,55), unicode("受け取ったメッセージ：" + self.text, 'utf-8'), font=font, fill=(0, 0, 0, 0))
        # OpenCV形式の画像に変換
        image = np.array(image, dtype=np.uint8)
        # 画像を表示する
        cv2.imshow("ノード名：" + rospy.get_name(), image)
        cv2.waitKey(1)
        
if __name__ == '__main__':
    # ノードを宣言
    rospy.init_node('uketoru_node')
    # クラスのインスタンスを作成
    uketoru = Uketoru()
    # 一定周期で処理を実行するための準備
    rate = rospy.Rate(10)
    # ループ処理開始
    while not rospy.is_shutdown():
        # 処理を実行
        uketoru.run()
        rate.sleep()
