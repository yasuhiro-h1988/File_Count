# -*- coding: Shift_JIS -*-

import glob
import os

i = 0

#拡張子を数えるパス


#検索する拡張子を入力
KAKU = input("計測するファイルの拡張子を入力してください\n(例：「File.jpg」であれば「jpg」と入力):\n")

Path = input("絶対パスを入力してください：\n")

files = glob.glob(os.path.join(Path + "\**\*." + KAKU),recursive=True)

for file in files:
    i += 1
str_i = str(i)

print("拡張子." + KAKU +"のファイル数：" + str_i + "個")

while True:
       key = input('Enterキーを押したら終了します')
       if not key:
           break