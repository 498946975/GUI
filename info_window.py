import tkinter as tk


class MyDialog(tk.Toplevel):
    def __init__(self, userinfo):
        super().__init__()
        self.title('显示用户信息')
        # 弹窗界面
        self.userinfo = userinfo
        self.setup_UI()

    def setup_UI(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='id：', width=10).pack(side=tk.LEFT)
        self.id = tk.StringVar(value=self.userinfo[0])
        tk.Entry(row1, textvariable=self.id, width=20).pack(side=tk.LEFT)

        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='用户名：', width=10).pack(side=tk.LEFT)
        self.username = tk.StringVar(value=self.userinfo[1])
        tk.Entry(row2, textvariable=self.username, width=20).pack(side=tk.LEFT)

        row3 = tk.Frame(self)
        row3.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row3, text='部门编号：', width=10).pack(side=tk.LEFT)
        self.dep_id = tk.StringVar(value=self.userinfo[2])
        tk.Entry(row3, textvariable=self.dep_id, width=20).pack(side=tk.LEFT)

        row4 = tk.Frame(self)
        row4.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row4, text='用户状态：', width=10).pack(side=tk.LEFT)
        self.state = tk.StringVar(value=self.userinfo[3])
        tk.Entry(row4, textvariable=self.state, width=20).pack(side=tk.LEFT)

        row5 = tk.Frame(self)
        row5.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row5, text='最后登陆日期：', width=10).pack(side=tk.LEFT)
        self.last_login_date = tk.StringVar(value=self.userinfo[4])
        tk.Entry(row5, textvariable=self.last_login_date, width=20).pack(side=tk.LEFT)

        row6 = tk.Frame(self)
        row6.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row6, text='IP：', width=10).pack(side=tk.LEFT)
        self.ip = tk.StringVar(value=self.userinfo[5])
        tk.Entry(row6, textvariable=self.ip, width=20).pack(side=tk.LEFT)

        row7 = tk.Frame(self)
        row7.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row7, text='是否删除：', width=10).pack(side=tk.LEFT)
        self.is_delete = tk.StringVar(value=self.userinfo[6])
        tk.Entry(row7, textvariable=self.is_delete, width=20).pack(side=tk.LEFT)

        row8 = tk.Frame(self)
        row8.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row8, text='创建时间：', width=10).pack(side=tk.LEFT)
        self.create_time = tk.StringVar(value=self.userinfo[7])
        tk.Entry(row8, textvariable=self.create_time, width=20).pack(side=tk.LEFT)

        row9 = tk.Frame(self)
        row9.pack(fill="x")
        tk.Button(row9, text="关闭", command=self.cancel).pack(side=tk.RIGHT)

    def cancel(self):
        self.userinfo = None  # 空！
        self.destroy()
