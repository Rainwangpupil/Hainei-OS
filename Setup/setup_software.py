from os import system,mkdir
import setup_load
import shutil
# C:\Users\kevinwang\Desktop
load = setup_load.load
system('mkdir {}\Software'.format(load))
with open('{}/run_docx.txt'.format(load), 'w+') as file:
    file.write(load)
def software_git():
    chose = input('是否要下载git?（Y/N)')
    if ('y' in chose or 'Y' in chose):
        system('sudo apt install git')
    software_vim()

def software_vim():
    chose = input('是否要下载vim（Y/N)')
    if ('y' in chose or 'Y' in chose):
        system('sudo apt install vim')
    software_python()

def software_python():
    chose = input('是否要下载Python（Y/N）')
    if ('y' in chose or 'Y' in chose):
        system('sudo apt install python')
    software_dos_attack()

def software_dos_attack():
    chose = input('是否要现在dos攻击程序（作者自制，详细操作方法请看https://github.com/rainwangpupil/dos_attack首页）')
    if ('y' in chose or 'Y' in chose):
         shutil.copy('./spare/dos_attack.py','{}/Software'.format(load))
    software_random_people()

def software_random_people():
    chose = input('是否要下载随机抽人程序（作者自制，详细操作方法软件里有说明）')
    if ('y' in chose or 'Y' in chose):
        shutil.copy('./spare/随机抽人器.py','{}/Software'.format(load))

