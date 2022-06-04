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
        questions_four()
    else:
        error()

def questions_four():
    chose = input('日本侵华战争第一个公开支持的国家是：') # 波兰不仅是公开支持侵华战争，还是第一个给予日本在我国侵华资金和武装力量支持的国家
    if '波兰' in chose:
        questions_five()
    else:
        error()

def questions_five():
    chose = input('日本投降时间为:') # 1945年8月15日正午，日本天皇宣布投降
    if '1945' in chose and '8' in chose and '15' in chose:
        questions_six()
    else:
        error()

def questions_six():
    chose = input('南京大屠杀人数至少有:') # 30万人，这还只是我国检测到的尸体的数量，可能连35万都不止
    if '30万' in chose or '30w' in chose:
        questions_seven()
    else:
        error()

def questions_seven():
    chose = input('虎门销烟，是谁烧掉了鸦片：') # 林则徐，当众烧掉了好几吨鸦片
    if '林则徐' in chose:
        questions_eight()
    else:
        error()

def questions_eight():
    global setup_status
    chose = input('我国古代秦始皇的名字叫：') # 嬴政，修筑万里长城，第一个自称“皇帝”的人
    if '嬴政' in chose:
        print('恭喜你，成功获得免费下载海内系统(Hainei OS)的资格')
        setup_status = True
    else:
        error()
