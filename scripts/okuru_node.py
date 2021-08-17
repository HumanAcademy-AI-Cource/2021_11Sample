#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリをインポート
import rospy
from std_msgs.msg import String

# チャットメッセージを送るノードのクラス
class Okuru():
    def __init__(self):
        # トピック名を保持する変数を作成
        self.topic_name = "/chat_message"
        # パブリッシャーを定義
        self.pub = rospy.Publisher(self.topic_name, String, queue_size=1)
        
    def run(self):
        """
        一連の処理を行う関数
        """

        # キーボードから入力を貰う
        text = raw_input("送るメッセージを入力してください: ")
        # 文字列を配信する（パブリッシュする）
        self.pub.publish(text)

if __name__ == '__main__':
    # ノードを宣言
    rospy.init_node('okuru_node')
    # クラスのインスタンスを作成
    okuru = Okuru()
    # 一定周期で処理を実行するための準備
    rate = rospy.Rate(10)
    # 2秒待つ
    rospy.sleep(2)
    # ループ処理開始
    while not rospy.is_shutdown():
        # 処理を実行
        okuru.run()
        rate.sleep()
