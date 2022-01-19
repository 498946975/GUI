# -*-coding:utf-8-*-
import tkinter as tk
import datetime
import db
from info_window import MyDialog
from tkinter import *
from tkinter import ttk


class Window():
    def __init__(self, master=None):
        self.root = master
        self.window_width = self.root.winfo_screenwidth()
        self.window_height = self.root.winfo_screenheight()
        self.root.geometry('{0}x{1}+200+200'.format(int(self.window_width * 0.9), int(self.window_height * 0.6)))
        self.root.title('监控')
        self.frm1 = Frame(self.root)
        self.frm2 = Frame(self.root)
        self.frm3 = Frame(self.root)
        self.table = Frame(self.frm1)
        self.var_str = tk.StringVar()
        self.createpage()
        self.sort_band_table()
        self.root.after(1000, self.refreshText)
        self.root.mainloop()

    def init_table(self):
        self.columns = ["id", 'username', 'dep_id', 'state', 'last_login_date', "ip", "is_delete", "create_time"]
        self.sort_column = ["id", "create_time"]
        self.table = ttk.Treeview(
            master=self.frm1,  # 父容器
            height=20,  # 表格显示的行数,height行
            columns=self.columns,  # 显示的列
            show='headings',  #
        )
        self.table.bind('<Double-1>', self.double_select_one)
        self.table.heading(column='id', text='id', anchor='w',
                           command=lambda: print('id'))  # 定义表头
        self.table.heading('username', text='username', )  # 定义表头
        self.table.heading('dep_id', text='dep_id', )  # 定义表头
        self.table.heading('state', text='state', )  # 定义表头
        self.table.heading('last_login_date', text='last_login_date', )  # 定义表头
        self.table.heading('ip', text='ip', )  # 定义表头
        self.table.heading('is_delete', text='is_delete', )  # 定义表头
        self.table.heading('create_time', text='create_time', )  # 定义表头

        self.table.column('id', width=30, minwidth=10, anchor=S, )  # 定义列
        self.table.column('username', width=100, minwidth=100, anchor=S)  # 定义列
        self.table.column('dep_id', width=50, minwidth=10, anchor=S)  # 定义列
        self.table.column('state', width=30, minwidth=30, anchor=S)  # 定义列
        self.table.column('last_login_date', width=150, minwidth=100, anchor=S)  # 定义列
        self.table.column('ip', width=100, minwidth=100, anchor=S)  # 定义列
        self.table.column('is_delete', width=50, minwidth=50, anchor=S)  # 定义列
        self.table.column('create_time', width=150, minwidth=100, anchor=S)  # 定义列
        self.table.grid(row=1, column=0, padx=20, pady=10, sticky=W)

    def createpage(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label='测试1', menu=filemenu)
        filemenu.add_command(label='1')
        filemenu.add_command(label='2')
        filemenu.add_command(label='3')

        onemenu = Menu(menu)
        menu.add_cascade(label='测试2', menu=onemenu)
        onemenu.add_command(label='1')
        onemenu.add_command(label='2')
        onemenu.add_command(label='3')

        # self.frm1.config(height=500, width=800, bg='green')
        self.frm1.config(height=500, width=800, bg='lightgrey')
        self.frm1.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

        # self.frm2.config(height=100, width=580, bg='red')
        self.frm2.config(height=100, width=580, bg='lightgrey')
        self.frm2.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=10)

        self.frm3.config(height=500, width=760, bg='lightgrey')
        # self.frm3.config(height=500, width=760, bg='lightgrey')
        self.frm3.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

        # frm3下的控件
        # row1
        Label(self.frm3, text='当前时间', height=1).grid(row=0, column=0, padx=10, pady=3, sticky=E)
        var_time_now = tk.StringVar()  # 讲文本框的内容，定义为字符串类型
        var_time_now.set(datetime.datetime.now())
        self.now_time = Text(self.frm3, width=30, height=1)
        self.now_time.grid(row=0, column=1, padx=10, pady=30, sticky=W)
        Label(self.frm3, text='金额单位：万元', height=1).grid(row=0, column=2, padx=1, pady=3)

        # row2
        Label(self.frm3, text='现货总价值', height=1).grid(row=2, column=0, padx=10, pady=20, sticky=E)
        self.XianHuoZongShiZhi = Text(self.frm3, width=15, height=1).grid(row=2, column=1, padx=10, pady=20, sticky=W)
        Label(self.frm3, text='期货总价值', height=1).grid(row=2, column=2, padx=10, pady=20, sticky=E)
        self.QiHuoZongShiZhi = Text(self.frm3, width=15, height=1).grid(row=2, column=3, padx=10, pady=20, sticky=W)

        # row3
        Label(self.frm3, text='限售股市值', height=1).grid(row=3, column=0, padx=10, pady=20, sticky=E)
        self.XianShouGuShiZhi = Text(self.frm3, width=15, height=1).grid(row=3, column=1, padx=10, pady=20, sticky=W)
        Label(self.frm3, text='期货总价值', height=1).grid(row=3, column=2, padx=10, pady=20, sticky=E)
        self.QiHuoZongShiZhi = Text(self.frm3, width=15, height=1).grid(row=3, column=3, padx=10, pady=20, sticky=W)

        # row4
        Label(self.frm3, text='净敞口', height=1).grid(row=4, column=0, padx=10, pady=20, sticky=E)
        self.JingChangKou = Text(self.frm3, width=15, height=1).grid(row=4, column=1, padx=10, pady=20, sticky=W)
        Label(self.frm3, text='限售股比例', height=1).grid(row=4, column=2, padx=10, pady=20, sticky=E)
        self.XianShouGuBiLi = Text(self.frm3, width=15, height=1).grid(row=4, column=3, padx=10, pady=20, sticky=W)

        # row5
        Label(self.frm3, text='超出限额', height=1).grid(row=5, column=0, padx=10, pady=20, sticky=E)
        self.ChaoChuXianE = Text(self.frm3, width=15, height=1).grid(row=5, column=1, padx=10, pady=20, sticky=W)
        Label(self.frm3, text='风险限额', height=1).grid(row=5, column=2, padx=10, pady=20, sticky=E)
        self.FengXianXianE = Text(self.frm3, width=15, height=1).grid(row=5, column=3, padx=10, pady=20, sticky=W)

        # row6
        Label(self.frm3, text='需对冲期货', height=1).grid(row=6, column=0, padx=10, pady=20, sticky=E)
        self.XuDuiChongQiHuo = Text(self.frm3, width=35, height=1).grid(row=6, column=1, padx=10, pady=20, sticky=W)

        # row7
        Label(self.frm3, text='现货今日盈亏', height=1).grid(row=7, column=0, padx=10, pady=20, sticky=E)
        self.XianHuoJinRiYingKui = Text(self.frm3, width=15, height=1).grid(row=7, column=1, padx=10, pady=20, sticky=W)
        Label(self.frm3, text='期货今日盈亏', height=1).grid(row=7, column=2, padx=10, pady=20, sticky=E)
        self.QiHuoJinRiYingKui = Text(self.frm3, width=15, height=1).grid(row=7, column=3, padx=10, pady=20, sticky=W)

        # frm2下的控件
        Button(self.frm2, text='Start_Refresh', command=self.start, height=2).grid(row=0, column=0, padx=20, pady=10,
                                                                                    sticky=W)
        Button(self.frm2, text='Stop_Refresh', command=self.stop, height=2).grid(row=0, column=2, padx=20, pady=10,
                                                                                  sticky=W)
        Button(self.frm2, text='昨日融劵信息', command=self.zuo_ri_zheng_quan_xin_xi(), height=2, width=15).grid(row=2,
                                                                                                           column=0,
                                                                                                           padx=20,
                                                                                                           pady=10,
                                                                                                           sticky=W)
        Button(self.frm2, text='解禁情况', command=self.jie_jin_qing_kuang, height=2, width=15).grid(row=2, column=1,
                                                                                                 padx=20, pady=10,
                                                                                                 sticky=W)
        Button(self.frm2, text='解禁日期查询', command=self.jie_jin_ri_qi_cha_xun, height=2, width=15).grid(row=2, column=2,
                                                                                                      padx=20, pady=10,
                                                                                                      sticky=W)

        # frm1下的控件
        Label(self.frm1, text='期货持仓信息').grid(row=0, column=0, padx=20, pady=10, sticky=W)

        # Text(self.frm1).place(x=10, y=50, height=400, width=400)
        self.init_table()
        self.inser_data()
        Button(self.frm1, text='行业占比', command=self.hang_ye_zhan_bi, height=2, width=8).grid(row=2, column=0, padx=20,
                                                                                             pady=10,
                                                                                             sticky=W)
        Button(self.frm1, text='市值分布', command=self.shi_zhi_fen_bu, height=2, width=8).grid(row=2, column=0, padx=200,
                                                                                            pady=10,
                                                                                            sticky=W)
        Button(self.frm1, text='xxxx', command=self.start, height=2, width=8).grid(row=2, column=0, padx=380, pady=10,
                                                                                   sticky=W)

    def start(self):
        # todo start功能按钮
        pass

    def stop(self):
        # todo stop功能按钮
        pass

    def zuo_ri_zheng_quan_xin_xi(self):
        # todo 昨日融劵信息 功能按钮
        pass

    def jie_jin_qing_kuang(self):
        # todo 解禁情况 功能按钮
        pass

    def jie_jin_ri_qi_cha_xun(self):
        # todo 解禁日期查询 功能按钮
        pass

    def hang_ye_zhan_bi(self):
        # todo 行业占比 功能按钮
        pass

    def shi_zhi_fen_bu(self):
        # todo 市值分布 功能按钮
        pass

    def xxxx(self):
        # todo xxxx 功能按钮
        pass

    def inser_data(self):
        data = db.DB().get_all_users()
        for i, person in enumerate(data):
            self.table.insert('', i, values=person)

    def refreshText(self):
        i = datetime.datetime.now()
        self.now_time.delete(0.0, tk.END)
        self.now_time.insert(tk.INSERT, i)
        self.now_time.update()
        self.root.after(1000, self.refreshText)

    def treeview_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def sort_band_table(self):

        for col in self.sort_column:  # 绑定函数，使表头可排序
            self.table.heading(col, text=col,
                               command=lambda _col=col: self.treeview_sort_column(self.table, _col, False))

    def double_select_one(self, event):
        for item in self.table.selection():
            user_info = self.table.item(item, "values")
            print(user_info)  # 输出所选行的值
            res = self.show_userinfo(user_info)
            if res is None: return

    def show_userinfo(self, user_info):
        inputDialog = MyDialog(user_info)
        self.root.wait_window(inputDialog)
        return inputDialog.userinfo


if __name__ == '__main__':
    root = Tk()
    Window(root)
