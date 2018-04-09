import re


# 读取屏蔽词文件
def load_blocked():
    with open('words.txt', 'r', encoding='utf8') as f:
        global b_words  # 使用全局变量记录屏蔽词
        b_words = [l.strip() for l in f.readlines() if l]


# 用正则表达式 (?i) 不区分大小写
def words_filter(text, charset='utf-8', symbol='*'):
    for w in b_words:
        # text = text.replace(w, symbol * len(w))
        text = re.sub(r'(?i)' + w, symbol * len(w), text)
    return text


# 测试效果
if __name__ == '__main__':
    # 读取屏蔽词
    load_blocked()
    print(b_words)
    while True:
        t = input('输入文字(直接回车退出)：\n')
        if not t:
            break
        print(words_filter(t))  # 输出替换结果
