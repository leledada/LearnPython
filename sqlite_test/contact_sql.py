# -*- coding: utf-8 -*-
import os
import sqlite3


# 添加记录
def insert(db, name, mobile, email):
    # ID 设成 NULL，sqlite 会填充自增 ID
    sql = r'''
        INSERT INTO TUSER (ID, NAME, MOBILE, EMAIL)
        VALUES (NULL, '%s', '%s', '%s');
    ''' % (name, mobile, email)
    db.execute(sql)
    db.commit()  # 执行所有写操作之后需要 commit 才会生效
    print('联系人保存成功。')


# 查询已有内容
def search(db, keyword):
    # 字符串格式化时，%%表示%字符本身
    sql = r'''
        SELECT * FROM TUSER WHERE
        NAME LIKE '%%%s%%' or
        MOBILE LIKE '%%%s%%' or
        EMAIL LIKE '%%%s%%';
    ''' % (keyword, keyword, keyword)
    # 获取结果，格式化显示
    queryset = db.execute(sql)
    print('ID NAME MOBILE EMAIL')
    for q in queryset:
        print(q[0], '\t'.join(q[1:]))


# 显示所有内容
def showall(db):
    sql = r'SELECT * FROM TUSER;'
    queryset = db.execute(sql)
    for q in queryset:
        print(q[0], '\t'.join(q[1:]))


# 删除记录
def delete(db, cid):
    # 先显示待删除内容，进行确认
    sql = r'SELECT * FROM TUSER WHERE ID=%s;' % cid
    queryset = db.execute(sql)
    for q in queryset:
        print(q[0], '\t'.join(q[1:]))

    confirm = input('确认删除此联系人？(y/[n])')
    if confirm.lower() == 'y':
        sql = r'DELETE FROM TUSER WHERE ID=%s;' % cid
        queryset = db.execute(sql)
        db.commit()
        print('删除联系人成功。')


# 先判断是否已存在数据库
DATABASE = 'testdb.db'
created = os.path.exists(DATABASE)
print(created)
# 建立连接，第一次会自动建库
conn = sqlite3.connect(DATABASE)
# 如果是第一次，创建表
if not created:
    # INTEGER PRIMARY KEY 可作为自增 ID，删除记录时用
    sql = '''
        CREATE TABLE IF NOT EXISTS TUSER
        (
            ID INTEGER PRIMARY KEY,
            NAME CHAR(8) NOT NULL,
            MOBILE CHAR(16),
            EMAIL VCHAR(64)
        );
    '''
    conn.execute(sql)

while True:
    choice = input('请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)\n')
    if choice == '1':
        name = ''
        while name.strip() == '':  # 避免用户输入空白字符
            name = input('姓名：')
        mobile = input('手机：')
        email = input('邮箱：')
        insert(conn, name, mobile, email)
    elif choice == '2':
        keyword = ''
        while keyword.strip() == '':
            keyword = input('查询关键字：')
        search(conn, keyword)
    elif choice == '3':
        showall(conn)
    elif choice == '4':
        cid = ''
        while not cid.isdigit():  # 判断输入是否为数字
            cid = input('联系人ID：')
        delete(conn, cid)
    elif choice == '':
        conn.close()  # 关闭连接
        break
    print()
