import sys
import itchat
import os
import math
import PIL.Image as Image

# 需要装PIL和itchat两个库
print(sys.version)
print(sys.version_info)

# 扫码登录
itchat.auto_login()
# 得到朋友列表
friends = itchat.get_friends(update=True)[0:]
# 根据自己的昵称拼音全称建一个文件夹，如果PYQuanPin报错，就换
user = ' '
try:
    user = friends[0]["PYQuanPin"][0:]
except:
    print('获取拼音全称异常')
else:  # 获取NickName
    user = friends[0]["NickName"][0:]
# user = 'GZGS1'
# print(user)
if not os.path.exists(user):
    os.mkdir(user)
    print('存放单个头像文件的文件夹创建成功', user)
# 将路径变更到创建的文件夹
os.chdir(user)
# 后台打印当前文件夹
print(os.getcwd())

# 遍历朋友列表，下载头像到文件夹
for i in friends:
    try:
        i['img'] = itchat.get_head_img(userName=i["UserName"])
        i['ImgName'] = i["UserName"][1:] + ".jpg"
    except ConnectionError:
        print('get ' + i["UserName"][1:] + ' fail')
    fileImage = open(i['ImgName'], 'wb')
    fileImage.write(i['img'])
    fileImage.close()

friendsSum = len(friends)
imgList = os.listdir(os.getcwd())
numImages = len(imgList)
print('我有%s个好友, 得到%s张头像' % (friendsSum, numImages))
print()

eachSize = 100
eachLine = int(math.sqrt(numImages)) + 1
print("单个图像边长", eachSize, "像素，一行", eachLine, "个头像，最终图像边长", eachSize * eachLine)

toImage = Image.new('RGB', (eachSize * eachLine, eachSize * eachLine))  # 新建一块画布
x = 0
y = 0
for i in imgList:
    try:
        img = Image.open(i)  # 打开图片
    except IOError:
        print("Error: 没有找到文件或读取文件失败", i)  # 有些人没设置头像，就会有异常
    else:
        img = img.resize((eachSize, eachSize), Image.ANTIALIAS)  # 缩小图片
        toImage.paste(img, (x * eachSize, y * eachSize))  # 拼接图片
        x += 1
    if x == eachLine:
        x = 0
        y += 1
print("图像拼接完成")

# toImage.show()

os.chdir(os.path.pardir)
os.getcwd()
print('保存拼接的图片到目录：', os.getcwd())
toImage.save('%sall.jpg' % user, quality=100)

itchat.send_image('%sall.jpg' % user, 'filehelper')  # 发给文件助手
print('完成拼接和保存，退出登录')
itchat.logout()
