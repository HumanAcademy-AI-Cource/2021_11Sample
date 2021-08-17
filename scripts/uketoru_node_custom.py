#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリをインポート
import cv2
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

        print("メッセージを受け取るノードです。")
        #################################
        # ここから自由に書いてください
        #################################
        
        print(1+1)
        print("Hello!")
        print("受信したメッセージ：{}".format(self.text))
        print("書き換えたメッセージ：{}！！！！！！！".format(self.text))

        #################################
        # ここまで
        #################################

        
if __name__ == '__main__':
    # ノードを宣言
    rospy.init_node('uketoru_node_custom')
    # クラスのインスタンスを作成
    uketoru = Uketoru()
    rospy.spin()
