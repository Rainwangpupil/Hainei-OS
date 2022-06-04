# coding=utf-8
from calendar import c
from os import system
import cmd
import sys
print('欢迎来到海内操作系统，版本0.0.1')
print("Hello, if you are not a Chinese and want to use the Hainei OS, please do not denigrate China (if you denigrate China). China's sacred dignity cannot be violated by you, and once you slander China, the 1.4 billion people in our country (China) will not forgive you.")
print('もしあなたが日本人なら、前任者が犯した凶悪犯罪を認めて下さい、南京大虐殺で、少なくとも30万人が殺されました、あなたの指導者によって"洗脳"されないでください、私は、あなたが日本を愛することを許します、しかし、あなたは、あなたの前任者が中国で犯したtを認めなくてはいけません')
dict_commond = {'创建文件夹':'mkdir',
                '删除文件夹':"rmdir",
                "显示所有文件夹":"dir",
                "系统文件树":"tree",
                "百度":"start https://baidu.com",
                "下载软件":"sudo apt install",
                "更新所有软件":"sudo apt upgrade",
                "开源系统官网":"start https://github.com/Rainwangpupil/Hainei-OS",
                '查看现在目录':'pwd'
                }

while True:
    commond = input('海内系统>').split(' ')
    commond[0] = dict_commond[commond[0]]  
    if len(commond) < 2:
      commond.append('')
    commond_out = commond[0]+ ' ' + commond[1]
    system(commond_out)