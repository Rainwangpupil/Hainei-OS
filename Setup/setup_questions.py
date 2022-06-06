setup_status = False

print("Hello, if you are not a Chinese and want to use the Hainei OS, please do not denigrate China (if you denigrate China). China's sacred dignity cannot be violated by you, and once you slander China, the 1.4 billion people in our country (China) will not forgive you.")
print('もしあなたが日本人なら、前任者が犯した凶悪犯罪を認めて下さい、南京大虐殺で、少なくとも30万人が殺されました、あなたの指導者によって"洗脳"されないでください、私は、あなたが日本を愛することを許します、しかし、あなたは、あなたの前任者が中国で犯したtを認めなくてはいけません')
def error():
    print('诶呀呀，多学学中国历史，下次再来下载海内系统吧') # 回答错误

def questions_one():
    chose = input('我国第一个把圆周率精确到第六位的数学家是：') # 祖冲之算出圆周率在3.1415926到3.1415927之间
    if '祖冲之' in chose:
        questions_two()
    else:
        error()

def questions_two():
    chose = input('李白是哪个朝代的诗人：') # 李白是唐代大诗人
    if '唐' in chose:
        questions_three()
    else:
        error()

def questions_three():
    chose = input('隋炀帝名字叫什么:') # 中国四大皇帝之一
    if '杨广' in chose:
        global setup_status
        print('恭喜你，成功获得免费下载海内系统(Hainei OS)的资格')
        setup_status = True
    else:
        error()

