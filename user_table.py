# 创建 user_table 并从excel中取值插入数据库
# 定义一些操作

import pymysql
import xlrd

conn_user = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='zmzm980725',
                                 db='student',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit = False)

def commit():
    conn_user.commit()
def close():
    conn_user.close()
def rollback():
    conn_user.rollback()

def LoadUserTable():
    workbook = xlrd.open_workbook(r'C:\Users\asus\Desktop\dbtask\grades.xlsx')
    sheet = workbook.sheet_by_index(0)
    
    for row in range(3,sheet.nrows):
        try:
            with conn_user.cursor() as cursor:
                insert_sql = 'insert into user_table (user_id, user_name, user_password) values (%s, %s, %s)'
                cursor.execute(insert_sql, (sheet.row(row)[0].value ,sheet.row(row)[1].value, sheet.row(row)[0].value))
        except:
            print(row)
            rollback()
        finally:
            commit()

def ExitUser(name, password):
    with conn_user.cursor() as cursor:
        exit_sql = 'select * from user_table where user_id = %s and user_password = %s'
        cursor.execute(exit_sql, (name, password))
    b = cursor.fetchall()
    print(b)
    if b == ( ):
        return False;
    else:
        return True;

def GetUserName(ID):
    with conn_user.cursor() as cursor:
        select_sql = 'select user_name from user_table where user_id = %s'
        cursor.execute(select_sql, (ID))
    b = cursor.fetchall()
    return b[0]['user_name']    # 返回字典第一条的 user_name

# 修改密码
def Update(ID, pw):
    try:
        with conn_user.cursor() as cursor:
            update_sql = 'update user_table set user_password = %s where user_id = %s'
            cursor.execute(update_sql, (pw, ID))
    except:
        rollback()
        return False
    finally:
        commit()
        return True
"""
create table user_table(
user_id char(12) primary key,
user_password varchar(12),
user_name varchar(6));
"""
