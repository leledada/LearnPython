# 热门 https://www.qiushibaike.com/8hr/page/2/
# 24小时 https://www.qiushibaike.com/hot/page/2/
# 热图  https://www.qiushibaike.com/imgrank/page/2/
#  pic.qiushibaike.com/system/pictures/12022/120221273/medium/app120221273.jpg
#  pic.qiushibaike.com/system/pictures/12022/120221299/medium/app120221299.jpg
# https://pic.qiushibaike.com/system/pictures/12021/120212014/medium/app120212014.jpg
# https://pic.qiushibaike.com/system/pictures/12015/120158680/small/app120158680.jpg
import requests
import re
import os
import time
import _thread
import threading


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        print(path, ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False


# 简单防止随便输入非数字导致异常，page0是个404的页面，也排除
def get_input_page():
    while True:
        try:
            st_num = int(input('请输入起始(非0)页码: \n'))
        except:
            pass
        if type(st_num) == int and st_num != 0:
            break

    while True:
        try:
            end_num = int(input('请输入结束页码: \n'))
        except:
            pass
        if type(end_num) == int and st_num <= end_num:
            break

    return st_num, end_num


def get_img_list():
    st, end = get_input_page()
    p_list = []
    for pn in range(st, end + 1):
        # 通过前面的研究，找到糗百图片规律
        reg = r'pic.qiushibaike.com/system/pictures/.*?jpg'
        url = 'https://www.qiushibaike.com/imgrank/page/%d/' % pn
        rsp = requests.get(url)
        p_list += re.findall(reg, rsp.text)
    return p_list


def download_pic(path, img_list):
    for i in img_list:
        pic_url = 'https://%s' % i
        # print(pic_url)
        resp = requests.get(pic_url)
        with open(path + pic_url[-16:], 'wb')as f:
            f.write(resp.content)
            print(pic_url[-16:], '下载完毕。')


if __name__ == '__main__':
    st_time = time.time()
    my_path = "qiubai_pic/"
    mkdir(my_path)
    pic_list = get_img_list()
    # t1 = threading.Thread(target=download_pic, args=(my_path,pic_list,))
    # t2 = threading.Thread(target=download_pic, args=(my_path,pic_list,))
    # t3 = threading.Thread(target=download_pic, args=(my_path,pic_list,))
    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
    download_pic(my_path, pic_list)
    print('您指定的页面中图片已下载完毕。')
    end_time = time.time()
    print('耗时', end_time - st_time)
