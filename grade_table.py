# 创建 grade_table 并从excel中取值插入数据库
# 定义一些操作

import pymysql
import xlrd
import showUI

# Connect to the database
class table():
    conn_grade = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='zmzm980725',
                                 db='student',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit = False)

    


    def CreateTable(self):
                """
                create table grade_table(
                stu_id char(12) primary key,
                stu_name varchar(6),
                dw1_grade varchar(3),   
                sygh_grade varchar(3),  
                dy1_grade varchar(3),   
                cxjc1_grade varchar(3), 
                jds_grade varchar(3),   
                gs1_grade varchar(3),   
                ty1_grade varchar(3),   
                xljk_grade varchar(3),  
                dy2_grade varchar(3),   
                cxsj1_grade varchar(3), 
                ty2_grade varchar(3),   
                gs2_grade varchar(3),
                ls_grade varchar(3),
                jx_grade varchar(3),    
                sx_grade varchar(3),    
                dl_grade varchar(3),    
                cxjc2_grade varchar(3), 
                cxsj2_grade varchar(3), 
                gpa varchar(6));
                """

 #   def insert(self):

    def show(self):
        with table.conn_grade.cursor() as cursor:
            cursor.execute('select stu_id, stu_name, gpa from grade_table')
            b = cursor.fetchall() # 获取单条数据
            for i in [*b]:
                #print('%s %s' % (i[0], i[1]))
                print(i)
    
    def init(self):
        LoadGradeTable(table)


    def deleteall(self):
        try:
            with table.conn_grade.cursor() as cursor:
                delete_sql = 'delete from grade_table'
                cursor.execute(delete_sql)
        except:
            table.rollback(table);
        finally:
            table.commit(table)


    def commit(self):
        table.conn_grade.commit()
    def close(self):
        table.conn_grade.close()
    def rollback(self):
        table.conn_grade.rollback()

        

# 以下是对单条数据进行操作的函数，没有定义在类内部
# Read data from excel and put them into grade_table   
def LoadGradeTable(table):
    workbook = xlrd.open_workbook(r'C:\Users\asus\Desktop\dbtask\grades.xlsx')
    sheet = workbook.sheet_by_index(0)
    
    for row in range(3,sheet.nrows):
        try:
            with table.conn_grade.cursor() as cursor:
                insert_sql = 'insert into grade_table (stu_id, stu_name, dw1_grade, sygh_grade, dy1_grade, cxjc1_grade, \
                jds_grade, gs1_grade, ty1_grade, xljk_grade, dy2_grade, cxsj1_grade, ty2_grade, gs2_grade, ls_grade, \
                jx_grade, sx_grade, dl_grade, cxjc2_grade, cxsj2_grade, gpa) \
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(insert_sql, (sheet.row(row)[0].value ,sheet.row(row)[1].value, int(sheet.row(row)[3].value), int(sheet.row(row)[4].value), int(sheet.row(row)[5].value), int(sheet.row(row)[6].value), int(sheet.row(row)[7].value), int(sheet.row(row)[8].value), int(sheet.row(row)[9].value), int(sheet.row(row)[10].value), int(sheet.row(row)[11].value), int(sheet.row(row)[12].value), int(sheet.row(row)[13].value), int(sheet.row(row)[14].value), int(sheet.row(row)[15].value), int(sheet.row(row)[16].value), int(sheet.row(row)[17].value), int(sheet.row(row)[18].value), int(sheet.row(row)[19].value), int(sheet.row(row)[20].value), eval(sheet.row(row)[26].value)))

        except:
            print(row)
            table.rollback(table)
        finally:
            table.commit(table)

# 通过 stu_id 删除数据
def Delete(table, stu_id):
    try:
        with table.conn_grade.cursor() as cursor:
            delete_sql = 'delete from grade_table where stu_id = %s'
            cursor.execute(delete_sql, (stu_id))
    except:
        table.rollback(table);
    finally:
        table.commit(table)

# 通过excel文件的行数，插入一条数据
def InsertFromExcel(table, row):
    try:
        with table.conn_grade.cursor() as cursor:
            insert_sql = 'insert into grade_table (stu_id, stu_name, dw1_grade, sygh_grade, dy1_grade, cxjc1_grade, \
            jds_grade, gs1_grade, ty1_grade, xljk_grade, dy2_grade, cxsj1_grade, ty2_grade, gs2_grade, ls_grade, \
            jx_grade, sx_grade, dl_grade, cxjc2_grade, cxsj2_grade, gpa) \
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(insert_sql, (sheet.row(row)[0].value ,sheet.row(row)[1].value, int(sheet.row(row)[3].value), 
                                        int(sheet.row(row)[4].value), int(sheet.row(row)[5].value), int(sheet.row(row)[6].value),
                                        int(sheet.row(row)[7].value), int(sheet.row(row)[8].value), int(sheet.row(row)[9].value), 
                                        int(sheet.row(row)[10].value), int(sheet.row(row)[11].value), int(sheet.row(row)[12].value), 
                                        int(sheet.row(row)[13].value), int(sheet.row(row)[14].value), int(sheet.row(row)[15].value), 
                                        int(sheet.row(row)[16].value), int(sheet.row(row)[17].value), int(sheet.row(row)[18].value), 
                                        int(sheet.row(row)[19].value), int(sheet.row(row)[20].value), eval(sheet.row(row)[26].value)))

    except:
        print(row)
        table.rollback(table)
    finally:
        table.commit(table)

# 插入学生成绩
def Insert(stu_id, stu_name, dw1_grade, sygh_grade, dy1_grade, cxjc1_grade, jds_grade, gs1_grade, ty1_grade, xljk_grade, 
           dy2_grade, cxsj1_grade, ty2_grade, gs2_grade, ls_grade, jx_grade, sx_grade, dl_grade, cxjc2_grade, cxsj2_grade, gpa):
    try:
        with table.conn_grade.cursor() as cursor:
            insert_sql = 'insert into grade_table (stu_id, stu_name, dw1_grade, sygh_grade, dy1_grade, cxjc1_grade, \
            jds_grade, gs1_grade, ty1_grade, xljk_grade, dy2_grade, cxsj1_grade, ty2_grade, gs2_grade, ls_grade, \
            jx_grade, sx_grade, dl_grade, cxjc2_grade, cxsj2_grade, gpa) \
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(insert_sql, (stu_id, stu_name, dw1_grade, sygh_grade, dy1_grade, cxjc1_grade, jds_grade, gs1_grade, 
                                        ty1_grade, xljk_grade, dy2_grade, cxsj1_grade, ty2_grade, gs2_grade, ls_grade, jx_grade, 
                                        sx_grade, dl_grade, cxjc2_grade, cxsj2_grade, gpa))
    except:
        print(row)
        table.rollback(table)
        return False
    finally:
        table.commit(table)
        return True

# 查找学生成绩，返回学生成绩字典
def Select(table, ID):
    with table.conn_grade.cursor() as cursor:
        select_sql = 'select * from grade_table where stu_id = %s'
        cursor.execute(select_sql, (ID))
        b = cursor.fetchall() # 获取单条数据
    return b
# 单科成绩查询
def Select1(g):
    if g == 1:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, dw1_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 2:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, sygh_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 3:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, dy1_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 4:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, cxjc1_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 5:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, jds_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 6:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, gs1_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 7:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, ty1_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 8:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, xljk_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 9:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, dy2_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 10:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, cxsj1_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 11:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, ty2_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 12:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, gs2_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 13:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, ls_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 14:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, jx_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 15:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, sx_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 16:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, dl_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 17:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, cxjc2_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 18:
        with table.conn_grade.cursor() as cursor:
            sql = 'select stu_id, stu_name, cxsj2_grade from grade_table'
            cursor.execute(sql)
            b = cursor.fetchall()
        return b

# 修改学生信息
def Update(stu_id, stu_name, dw1_grade, sygh_grade, dy1_grade, cxjc1_grade, jds_grade, gs1_grade, ty1_grade, xljk_grade, 
           dy2_grade, cxsj1_grade, ty2_grade, gs2_grade, ls_grade, jx_grade, sx_grade, dl_grade, cxjc2_grade, cxsj2_grade, gpa):
    try:
        with table.conn_grade.cursor() as cursor:
            insert_sql = 'update grade_table set stu_name = %s, dw1_grade = %s, sygh_grade = %s, dy1_grade = %s \
            , cxjc1_grade = %s, jds_grade = %s, gs1_grade = %s, ty1_grade = %s, xljk_grade = %s, dy2_grade = %s \
            , cxsj1_grade = %s, ty2_grade = %s, gs2_grade = %s, ls_grade = %s, jx_grade = %s, sx_grade = %s \
            , dl_grade = %s, cxjc2_grade = %s, cxsj2_grade = %s, gpa = %s \
            where stu_id = %s'
            cursor.execute(insert_sql, (stu_name, dw1_grade, sygh_grade, dy1_grade, cxjc1_grade, jds_grade, gs1_grade, 
                                        ty1_grade, xljk_grade, dy2_grade, cxsj1_grade, ty2_grade, gs2_grade, ls_grade, jx_grade, 
                                        sx_grade, dl_grade, cxjc2_grade, cxsj2_grade, gpa, stu_id))
    except:
        table.rollback(table)
    finally:
        table.commit(table)

# 是否存在学号为 stu_id 的学生
def Exist(stu_id):
    with table.conn_grade.cursor() as cursor:
        select_sql = 'select * from grade_table where stu_id = %s'
        cursor.execute(select_sql, (stu_id))
        b = cursor.fetchall()
    print(b)
    if b == ():
        return False
    else:
        return True



