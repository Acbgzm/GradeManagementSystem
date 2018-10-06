# 创建管理员和用户的操作界面
# 分备完成权限内的全部操作

import grade_table
import user_table
import admin_table
from tkinter import *
from showUI import *
from tkinter.messagebox import *

import matplotlib.pyplot as plt
import numpy as np


def ShowGradeUI(b):
    win_showgrade = Tk()
    win_showgrade.title(' %s 的成绩'%b[0]['stu_name'])
    lbl1 = Label(win_showgrade, text = '大学物理一:%s '%b[0]['dw1_grade']).grid(row = 0, column = 0)
    lbl2 = Label(win_showgrade, text = '职业生涯规划:%s '%b[0]['sygh_grade']).grid(row = 0, column = 1)
    lbl3 = Label(win_showgrade, text = '大学英语一:%s '%b[0]['dy1_grade']).grid(row = 0, column = 2)
    lbl4 = Label(win_showgrade, text = '程序设计基础一:%s '%b[0]['cxjc1_grade']).grid(row = 1, column = 0)
    lbl5 = Label(win_showgrade, text = '中国近代史纲要:%s '%b[0]['jds_grade']).grid(row = 1, column = 1)
    lbl6 = Label(win_showgrade, text = '高等数学一:%s '%b[0]['gs1_grade']).grid(row = 1, column = 2)
    lbl7 = Label(win_showgrade, text = '体育一:%s '%b[0]['ty1_grade']).grid(row = 2, column = 0)
    lbl8 = Label(win_showgrade, text = '心理健康教育:%s '%b[0]['xljk_grade']).grid(row = 2, column = 1)
    lbl9 = Label(win_showgrade, text = '大学英语二:%s '%b[0]['dy2_grade']).grid(row = 2, column = 2)
    lbl10 = Label(win_showgrade, text = '程序设计实践一:%s '%b[0]['cxsj1_grade']).grid(row = 3, column = 0)
    lbl11 = Label(win_showgrade, text = '体育二:%s '%b[0]['ty2_grade']).grid(row = 3, column = 1)
    lbl12 = Label(win_showgrade, text = '高等数学二:%s '%b[0]['gs2_grade']).grid(row = 3, column = 2)
    lbl13 = Label(win_showgrade, text = '离散数学:%s '%b[0]['ls_grade']).grid(row = 4, column = 0)
    lbl14 = Label(win_showgrade, text = '军事理论与训练:%s '%b[0]['jx_grade']).grid(row = 4, column = 1)
    lbl15 = Label(win_showgrade, text = '思想道德修养:%s '%b[0]['sx_grade']).grid(row = 4, column = 2)
    lbl16 = Label(win_showgrade, text = '计算机科学导论:%s '%b[0]['dl_grade']).grid(row = 5, column = 0)
    lbl17 = Label(win_showgrade, text = '程序设计基础二:%s '%b[0]['cxjc2_grade']).grid(row = 5, column = 1)
    lbl18 = Label(win_showgrade, text = '程序设计实践二:%s '%b[0]['cxsj2_grade']).grid(row = 5, column = 2)
    lbl19 = Label(win_showgrade, text = '------GPA:%s------ '%b[0]['gpa']).grid(row = 6, column = 0, columnspan = 3)
    win_showgrade.mainloop()


def UserUI(ID):
    
    # 调用 ShowGradeUI() 显示所有成绩
    def ShowGrade():
        b = grade_table.Select(grade_table.table, ID)
        print(b)
        ShowGradeUI(b)
    # 显示修改密码界面,通过按钮调用 ChangePassword() 
    def ChangePasswordUI():
        def Ready():
            user_table.Update(ID, entNewPw.get())
            showinfo(title = '', message = '修改成功！')
        win_userupdate = Tk()
        lblTip = Label(win_userupdate, text = '新密码:').grid(row = 0, column = 0)
        entNewPw = Entry(win_userupdate, width = 15)
        btnUpdate = Button(win_userupdate, text = '修改', command = Ready).grid(row = 1, column = 0)
        entNewPw.grid(row = 0, column = 1)
        win_userupdate.mainloop()

    win_user = Tk()
    win_user.title('用户')

    lblTip = Label(win_user, text = '欢迎您，%s'%user_table.GetUserName(ID))
    btnSelect = Button(win_user, text = '查询我的成绩', command = ShowGrade)
    btnUpdate = Button(win_user, text = '修改密码', command = ChangePasswordUI)
    
    lblTip.pack()
    btnSelect.pack()
    btnUpdate.pack()
    win_user.mainloop()


def AdminUI(adminID):
    win_admin = Tk()
    win_admin.title('管理员')


    
    def InsertGradeUI():
        win_insert = Tk()
        def Ready():
            if grade_table.Exist(ent0.get()) == True:
                showinfo(title = '', message = '该学生信息已存在!')
            else:
                x = grade_table.Insert(ent0.get(), ent20.get(), ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get(), 
                                   ent7.get(), ent8.get(), ent9.get(), ent10.get(), ent11.get(), ent12.get(), 
                                   ent13.get(), ent14.get(), ent15.get(), ent16.get(), ent17.get(), ent18.get(), ent19.get())
                showinfo(title = '', message = '成功！')

        lbl0 = Label(win_insert, text = '学号:').grid(row = 0, column = 1)
        ent0 = Entry(win_insert, width = 12)
        ent0.grid(row = 0, column = 2)
        lbl20 = Label(win_insert, text = '姓名:').grid(row = 0, column = 3)
        ent20 = Entry(win_insert, width = 8)
        ent20.grid(row = 0, column = 4)
        lbl1 = Label(win_insert, text = '大学物理一:').grid(row = 1, column = 0)
        ent1 = Entry(win_insert, width = 3)
        ent1.grid(row = 1, column = 1)
        lbl2 = Label(win_insert, text = '职业生涯规划:').grid(row = 1, column = 2)
        ent2 = Entry(win_insert, width = 3)
        ent2.grid(row = 1, column = 3)
        lbl3 = Label(win_insert, text = '大学英语一:').grid(row = 1, column = 4)
        ent3 = Entry(win_insert, width = 3)
        ent3.grid(row = 1, column = 5)
        lbl4 = Label(win_insert, text = '程序设计基础一:').grid(row = 2, column = 0)
        ent4 = Entry(win_insert, width = 3)
        ent4.grid(row = 2, column = 1)
        lbl5 = Label(win_insert, text = '中国近代史纲要:').grid(row = 2, column = 2)
        ent5 = Entry(win_insert, width = 3)
        ent5.grid(row = 2, column = 3)
        lbl6 = Label(win_insert, text = '高等数学一:').grid(row = 2, column = 4)
        ent6 = Entry(win_insert, width = 3)
        ent6.grid(row = 2, column = 5)
        lbl7 = Label(win_insert, text = '体育一:').grid(row = 3, column = 0)
        ent7 = Entry(win_insert, width = 3)
        ent7.grid(row = 3, column = 1)
        lbl8 = Label(win_insert, text = '心理健康教育:').grid(row = 3, column = 2)
        ent8 = Entry(win_insert, width = 3)
        ent8.grid(row = 3, column = 3)
        lbl9 = Label(win_insert, text = '大学英语二:').grid(row = 3, column = 4)
        ent9 = Entry(win_insert, width = 3)
        ent9.grid(row = 3, column = 5)
        lbl10 = Label(win_insert, text = '程序设计实践一:').grid(row = 4, column = 0)
        ent10 = Entry(win_insert, width = 3)
        ent10.grid(row = 4, column = 1)
        lbl11 = Label(win_insert, text = '体育二:').grid(row = 4, column = 2)
        ent11 = Entry(win_insert, width = 3)
        ent11.grid(row = 4, column = 3)
        lbl12 = Label(win_insert, text = '高等数学二:').grid(row = 4, column = 4)
        ent12 = Entry(win_insert, width = 3)
        ent12.grid(row = 4, column = 5)
        lbl13 = Label(win_insert, text = '离散数学:').grid(row = 5, column = 0)
        ent13 = Entry(win_insert, width = 3)
        ent13.grid(row = 5, column = 1)
        lbl14 = Label(win_insert, text = '军事理论与训练:').grid(row = 5, column = 2)
        ent14 = Entry(win_insert, width = 3)
        ent14.grid(row = 5, column = 3)
        lbl15 = Label(win_insert, text = '思想道德修养:').grid(row = 5, column = 4)
        ent15 = Entry(win_insert, width = 3)
        ent15.grid(row = 5, column = 5)
        lbl16 = Label(win_insert, text = '计算机科学导论:').grid(row = 6, column = 0)
        ent16 = Entry(win_insert, width = 3)
        ent16.grid(row = 6, column = 1)
        lbl17 = Label(win_insert, text = '程序设计基础二:').grid(row = 6, column = 2)
        ent17 = Entry(win_insert, width = 3)
        ent17.grid(row = 6, column = 3)
        lbl18 = Label(win_insert, text = '程序设计实践二:').grid(row = 6, column = 4)
        ent18 = Entry(win_insert, width = 3)
        ent18.grid(row = 6, column = 5)
        lbl19 = Label(win_insert, text = 'GPA:').grid(row = 7, column = 1)
        ent19 = Entry(win_insert, width = 5)
        ent19.grid(row = 7, column = 2, sticky = W)
        btn0 = Button(win_insert, text = '增加学生成绩', command = Ready).grid(row = 8, column = 0, columnspan = 6)
        
        win_insert.mainloop()

    def ChangePasswordUI():
        def Ready():
            admin_table.Update(adminID, entNewPw.get())
            showinfo(title = '', message = '修改成功！')
        win_adminupdate = Tk()
        lblTip = Label(win_adminupdate, text = '新密码:').grid(row = 0, column = 0)
        entNewPw = Entry(win_adminupdate, width = 15)
        btnUpdate = Button(win_adminupdate, text = '修改', command = Ready).grid(row = 1, column = 0)
        entNewPw.grid(row = 0, column = 1)
        win_adminupdate.mainloop()


    def SelectGradeUI():
        def Ready():
            if grade_table.Exist(entID.get()) == False:
                showinfo(title = '', message = '学号输入错误!')
            else:
                b = grade_table.Select(grade_table.table, entID.get())
                ShowGradeUI(b)
        win_enter = Tk()
        lbl0 = Label(win_enter, text = '请输入学生学号:')
        entID = Entry(win_enter, width = 15)
        btnEnter = Button(win_enter, text = '查看成绩', command = Ready)
        lbl0.grid(row = 0, column = 0)
        entID.grid(row = 1, column = 0)
        btnEnter.grid(row = 2, column = 0)
        win_enter.mainloop()

    def DeleteGradeUI():
        def Ready():
            if grade_table.Exist(entID.get()) == False:
                showinfo(title = '', message = '学号输入错误!')
            else:
                b = grade_table.Delete(grade_table.table, entID.get())
                showinfo(title = '', message = '删除成功!')
        win_enter = Tk()
        lbl0 = Label(win_enter, text = '请输入学生学号:')
        entID = Entry(win_enter, width = 15)
        btnEnter = Button(win_enter, text = '删除成绩', command = Ready)
        lbl0.grid(row = 0, column = 0)
        entID.grid(row = 1, column = 0)
        btnEnter.grid(row = 2, column = 0)
        win_enter.mainloop()

    
        
    def UpdateOne():
        win_update = Tk()
        def Ready():
            if grade_table.Exist(ent0.get()) == False:
                showinfo(title = '', message = '学号输入错误!')
            else:
                grade_table.Update(ent0.get(), ent20.get(), ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get(), 
                                   ent7.get(), ent8.get(), ent9.get(), ent10.get(), ent11.get(), ent12.get(), 
                                   ent13.get(), ent14.get(), ent15.get(), ent16.get(), ent17.get(), ent18.get(), ent19.get())
                showinfo(title = '', message = '成功!')
                b = grade_table.Select(grade_table.table, ent0.get())
                ShowGradeUI(b)

        lbl0 = Label(win_update, text = '学号:').grid(row = 0, column = 1)
        ent0 = Entry(win_update, width = 12)
        ent0.grid(row = 0, column = 2)
        lbl20 = Label(win_update, text = '姓名:').grid(row = 0, column = 3)
        ent20 = Entry(win_update, width = 8)
        ent20.grid(row = 0, column = 4)
        lbl1 = Label(win_update, text = '大学物理一:').grid(row = 1, column = 0)
        ent1 = Entry(win_update, width = 3)
        ent1.grid(row = 1, column = 1)
        lbl2 = Label(win_update, text = '职业生涯规划:').grid(row = 1, column = 2)
        ent2 = Entry(win_update, width = 3)
        ent2.grid(row = 1, column = 3)
        lbl3 = Label(win_update, text = '大学英语一:').grid(row = 1, column = 4)
        ent3 = Entry(win_update, width = 3)
        ent3.grid(row = 1, column = 5)
        lbl4 = Label(win_update, text = '程序设计基础一:').grid(row = 2, column = 0)
        ent4 = Entry(win_update, width = 3)
        ent4.grid(row = 2, column = 1)
        lbl5 = Label(win_update, text = '中国近代史纲要:').grid(row = 2, column = 2)
        ent5 = Entry(win_update, width = 3)
        ent5.grid(row = 2, column = 3)
        lbl6 = Label(win_update, text = '高等数学一:').grid(row = 2, column = 4)
        ent6 = Entry(win_update, width = 3)
        ent6.grid(row = 2, column = 5)
        lbl7 = Label(win_update, text = '体育一:').grid(row = 3, column = 0)
        ent7 = Entry(win_update, width = 3)
        ent7.grid(row = 3, column = 1)
        lbl8 = Label(win_update, text = '心理健康教育:').grid(row = 3, column = 2)
        ent8 = Entry(win_update, width = 3)
        ent8.grid(row = 3, column = 3)
        lbl9 = Label(win_update, text = '大学英语二:').grid(row = 3, column = 4)
        ent9 = Entry(win_update, width = 3)
        ent9.grid(row = 3, column = 5)
        lbl10 = Label(win_update, text = '程序设计实践一:').grid(row = 4, column = 0)
        ent10 = Entry(win_update, width = 3)
        ent10.grid(row = 4, column = 1)
        lbl11 = Label(win_update, text = '体育二:').grid(row = 4, column = 2)
        ent11 = Entry(win_update, width = 3)
        ent11.grid(row = 4, column = 3)
        lbl12 = Label(win_update, text = '高等数学二:').grid(row = 4, column = 4)
        ent12 = Entry(win_update, width = 3)
        ent12.grid(row = 4, column = 5)
        lbl13 = Label(win_update, text = '离散数学:').grid(row = 5, column = 0)
        ent13 = Entry(win_update, width = 3)
        ent13.grid(row = 5, column = 1)
        lbl14 = Label(win_update, text = '军事理论与训练:').grid(row = 5, column = 2)
        ent14 = Entry(win_update, width = 3)
        ent14.grid(row = 5, column = 3)
        lbl15 = Label(win_update, text = '思想道德修养:').grid(row = 5, column = 4)
        ent15 = Entry(win_update, width = 3)
        ent15.grid(row = 5, column = 5)
        lbl16 = Label(win_update, text = '计算机科学导论:').grid(row = 6, column = 0)
        ent16 = Entry(win_update, width = 3)
        ent16.grid(row = 6, column = 1)
        lbl17 = Label(win_update, text = '程序设计基础二:').grid(row = 6, column = 2)
        ent17 = Entry(win_update, width = 3)
        ent17.grid(row = 6, column = 3)
        lbl18 = Label(win_update, text = '程序设计实践二:').grid(row = 6, column = 4)
        ent18 = Entry(win_update, width = 3)
        ent18.grid(row = 6, column = 5)
        lbl19 = Label(win_update, text = 'GPA:').grid(row = 7, column = 1)
        ent19 = Entry(win_update, width = 5)
        ent19.grid(row = 7, column = 2, sticky = W)
        lbl21 = Label(win_update, text = '--------请输入学生的全部成绩信息--------')
        btn0 = Button(win_update, text = '修改学生成绩', command = Ready).grid(row = 9, column = 0, columnspan = 6)
        
        win_update.mainloop()

    # 这里有很大问题，子函数没有封装好，把所有情况全写了一遍。主要是不会用按钮传参数，只能写不带参数的函数。
    def SelectAll():
        def select_1(): # 注意字符串和整数转换
            grade_list = []   # 存有所有人 dw1_grade 的列表
            b_grade = grade_table.Select1(1)
            for i in b_grade:
                grade_list.append(i['dw1_grade']) # i 是 b_dw1 字典中的每一行
            print(grade_list)
            grade = np.zeros(101) # 考 i 分的有 grade[i] 人
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'r-')
            plt.show()
        def select_2(): 
            grade_list = []   
            b_grade = grade_table.Select1(2)
            for i in b_grade:
                grade_list.append(i['sygh_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'b-')
            plt.show()
        def select_3(): 
            grade_list = []   
            b_grade = grade_table.Select1(3)
            for i in b_grade:
                grade_list.append(i['dy1_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'y-')
            plt.show()
        def select_4(): 
            grade_list = []   
            b_grade = grade_table.Select1(4)
            for i in b_grade:
                grade_list.append(i['cxjc1_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'g-')
            plt.show()
        def select_5(): 
            grade_list = []   
            b_grade = grade_table.Select1(5)
            for i in b_grade:
                grade_list.append(i['jds_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'k-')
            plt.show()
        def select_6(): 
            grade_list = []   
            b_grade = grade_table.Select1(6)
            for i in b_grade:
                grade_list.append(i['gs1_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'r-')
            plt.show()
        def select_7(): 
            grade_list = []   
            b_grade = grade_table.Select1(7)
            for i in b_grade:
                grade_list.append(i['ty1_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'b-')
            plt.show()
        def select_8(): 
            grade_list = []   
            b_grade = grade_table.Select1(8)
            for i in b_grade:
                grade_list.append(i['xljk_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'y-')
            plt.show()
        def select_9(): 
            grade_list = []   
            b_grade = grade_table.Select1(9)
            for i in b_grade:
                grade_list.append(i['dy2_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'g-')
            plt.show()
        def select_10(): 
            grade_list = []   
            b_grade = grade_table.Select1(10)
            for i in b_grade:
                grade_list.append(i['cxsj1_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'k-')
            plt.show()
        def select_11(): 
            grade_list = []   
            b_grade = grade_table.Select1(11)
            for i in b_grade:
                grade_list.append(i['ty2_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'r-')
            plt.show()
        def select_12(): 
            grade_list = []   
            b_grade = grade_table.Select1(12)
            for i in b_grade:
                grade_list.append(i['gs2_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'b-')
            plt.show()
        def select_13(): 
            grade_list = []   
            b_grade = grade_table.Select1(13)
            for i in b_grade:
                grade_list.append(i['ls_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'y-')
            plt.show()
        def select_14(): 
            grade_list = []   
            b_grade = grade_table.Select1(14)
            for i in b_grade:
                grade_list.append(i['jx_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'g-')
            plt.show()
        def select_15(): 
            grade_list = []   
            b_grade = grade_table.Select1(15)
            for i in b_grade:
                grade_list.append(i['sx_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'k-')
            plt.show()
        def select_16(): 
            grade_list = []   
            b_grade = grade_table.Select1(16)
            for i in b_grade:
                grade_list.append(i['dl_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'r-')
            plt.show()
        def select_17(): 
            grade_list = []   
            b_grade = grade_table.Select1(17)
            for i in b_grade:
                grade_list.append(i['cxjc2_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'b-')
            plt.show()
        def select_18(): 
            grade_list = []   
            b_grade = grade_table.Select1(18)
            for i in b_grade:
                grade_list.append(i['cxsj2_grade'])
            print(grade_list)
            grade = np.zeros(101)
            for i in range (-1, 101):
                grade[i] = grade_list.count(str(i))
            #print(grade)
            i = np.arange(-1, 101, 1)
            plt.plot(i, grade[i], 'y')
            plt.show()

        win_selectall = Tk()
        lbl0 = Label(win_selectall, text = '您要查看哪门课的成绩情况？').grid(row = 0, column = 0, columnspan = 3)
        btn1 = Button(win_selectall, text = '大学物理一', command = select_1).grid(row = 1, column = 0)
        btn2 = Button(win_selectall, text = '职业生涯规划', command = select_2).grid(row = 1, column = 1)
        btn3 = Button(win_selectall, text = '大学英语一', command = select_3).grid(row = 1, column = 2)
        btn4 = Button(win_selectall, text = '程序设计基础一', command = select_4).grid(row = 2, column = 0)
        btn5 = Button(win_selectall, text = '中国近代史纲要', command = select_5).grid(row = 2, column = 1)
        btn6 = Button(win_selectall, text = '高等数学一', command = select_6).grid(row = 2, column = 2)
        btn7 = Button(win_selectall, text = '体育一', command = select_7).grid(row = 3, column = 0)
        btn8 = Button(win_selectall, text = '心理健康教育', command = select_8).grid(row = 3, column = 1)
        btn9 = Button(win_selectall, text = '大学英语二', command = select_9).grid(row = 3, column = 2)
        btn10 = Button(win_selectall, text = '程序设计实践一', command = select_10).grid(row = 4, column = 0)
        btn11 = Button(win_selectall, text = '体育二', command = select_11).grid(row = 4, column = 1)
        btn12 = Button(win_selectall, text = '高等数学二', command = select_12).grid(row = 4, column = 2)
        btn13 = Button(win_selectall, text = '离散数学', command = select_13).grid(row = 5, column = 0)
        btn14 = Button(win_selectall, text = '军事理论与训练', command = select_14).grid(row = 5, column = 1)
        btn15 = Button(win_selectall, text = '思想道德修养', command = select_15).grid(row = 5, column = 2)
        btn16 = Button(win_selectall, text = '计算机科学导论', command = select_16).grid(row = 6, column = 0)
        btn17 = Button(win_selectall, text = '程序设计基础二', command = select_17).grid(row = 6, column = 1)
        btn18 = Button(win_selectall, text = '程序设计实践二', command = select_18).grid(row = 6, column = 2)
        win_selectall.mainloop()

    lblTip = Label(win_admin, text = '欢迎您，管理员%s'%adminID)
    btnSelectOne = Button(win_admin, text = '查询学生成绩', command = SelectGradeUI)
    btnSelectAll = Button(win_admin, text = '查看成绩分布', command = SelectAll)
    btnUpdateOne = Button(win_admin, text = '修改学生成绩', command = UpdateOne)
    btnUpdatePw = Button(win_admin, text = '修改登陆密码', command = ChangePasswordUI)
    btnDelete = Button(win_admin, text = '删除学生成绩', command = DeleteGradeUI)
    btnInsert = Button(win_admin, text = '增加学生成绩', command = InsertGradeUI)

    lblTip.grid(row = 0, column = 0, columnspan = 2, pady = 5)
    btnInsert.grid(row = 1, column = 0, padx = 5, pady = 5)
    btnDelete.grid(row = 1, column = 1, padx = 5, pady = 5)
    btnSelectOne.grid(row = 2, column = 0, padx = 5, pady = 5)
    btnSelectAll.grid(row = 2, column = 1, padx = 5, pady = 5)
    btnUpdateOne.grid(row = 3, column = 0, padx = 5, pady = 5)
    btnUpdatePw.grid(row = 3, column = 1, padx = 5, pady = 5)
    win_admin.mainloop()
  


    