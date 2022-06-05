from os import system
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
                '查看现在目录':'pwd',
                '打开网站':'start',
                'dos黑客工具':'start Software/dos_attack.py',
                '抽人器':'start Software/随机抽人器.py',
                '必应':'start https://cn.bing.com/?mkt=zh-cn',
                '搞笑新闻':'start Software/搞笑新闻.py'
                }


while True:
    commond = input('海内系统>') # 分解命令与命令值
    try:
      commond_list = commond.split(' ')
      #为了防止出现用户输入Linux自带命令错误的情况
      commond_list[0] = dict_commond[commond_list[0]]  # 把海内系统命令转换为Linux系统命令
      if len(commond) < 2:
        commond_list.append('') # 将一些没有命令值的命令填充命令值''
      commond_out = commond_list[0]+ ' ' + commond_list[1] # 分解后，将它们合并，作为Linux命令
      system(commond_out) # 运行命令
    except:
      system(commond)