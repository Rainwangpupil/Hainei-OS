from os import system
import setup_load
load = setup_load.load

with open('{}/run_docx.txt'.format(load)) as file:
    file.write(load)

def software_git():
    chose = input('是否要下载git?（Y/N)')
    if ('y' in chose or 'Y' in chose):
        system('sudo apt install git')
        software_vim()
    software_vim()

def software_vim():
    chose = input('是否要下载vim（Y/N)')
    if ('y' in chose or 'Y' in chose):
        system('sudo apt install vim')
        software_python()
    software_python()

def software_python():
    chose = input('是否要下载Python（Y/N）')
    if ('y' in chose or 'Y' in chose):
        system('sudo apt install python')
        software_python()
    software_python()