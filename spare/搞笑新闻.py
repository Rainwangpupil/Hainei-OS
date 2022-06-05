from random import randint
with open('./docx/搞笑新闻录.txt', 'r+', encoding="utf-8") as f:
    new = f.readlines()
    print(new[randint(0, len(new) - 1)])
while True:
    print('', end='')
