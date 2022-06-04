import random
import time
print('该软件可以用于随机抽人，比如：抽到谁谁去洗碗')
people_str = input('请输入“选手”（用空格分开）：')
people_list = people_str.split(' ')
print('这是你调的"选手"')
for i in people_list:
    print(i, end=' ')
print('\n')
print('正在抽人中...')
time.sleep(1)
random.shuffle(people_list)
print('这是抽人的结果:{}'.format(people_list[0]))