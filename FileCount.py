# -*- coding: Shift_JIS -*-

import glob
import os

i = 0

#�g���q�𐔂���p�X


#��������g���q�����
KAKU = input("�v������t�@�C���̊g���q����͂��Ă�������\n(��F�uFile.jpg�v�ł���΁ujpg�v�Ɠ���):\n")

Path = input("��΃p�X����͂��Ă��������F\n")

files = glob.glob(os.path.join(Path + "\**\*." + KAKU),recursive=True)

for file in files:
    i += 1
str_i = str(i)

print("�g���q." + KAKU +"�̃t�@�C�����F" + str_i + "��")

while True:
       key = input('Enter�L�[����������I�����܂�')
       if not key:
           break