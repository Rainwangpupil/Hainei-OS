from setup_questions import *
from time import sleep
from setup_software import *
def main_1():
    questions_one()
    if setup_status:
        print('正式进入海内系统下载状态')
        print('海内系统(英文名Hainei OS),是一个基于Linux的操作系统,使用Python开发。')
        sleep(1)
        print('海内系统是一个由小学生开发的操作系统，因为能力有限，目前只开发了命令行模式。')
        sleep(1)
        print('海内系统(Hainei OS)秉承“只有中国人能用的操作系统”。海内系统之所以叫海内，因为这是中国的一个称呼')
        main_2()

def main_2():
    software_git()