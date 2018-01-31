"""
0. 实现牛顿法求根：
1. 构造出 y=x^2-a 这个函数
2. 取 x=a 得到 y
3. 如果 y==0 则成功，否则 进入4
4. 得到 k=y'(a) ，构造直线 y-y(a)=k(x-a)，令 y=0 得到 x，使 a=x，并进入 步骤2
"""

from tkinter import *
import tkinter.messagebox as messagebox
import numpy as np
import matplotlib.pyplot as plt
import time


def plot_fuck(num):
    # 画出函数图
    plt.figure(1)
    x = np.linspace(0, num * 1.3, 1000)
    y = [i * i - num for i in x]
    ax1.plot(x, y)
    ax1.plot(x, x * 0, 'k')
    fig.show()


def plot_line(a, num):
    x = np.linspace(a, a, 100)
    y = np.linspace(0, a*a - num, 100)
    ax1.plot(x, y, 'r-')
    fig.show()


# 画切线
def plot_tangent(x0, x1, k):
    x = np.linspace(x0, x1, 100)
    y = k * (x - x0)
    ax1.plot(x, y, 'r')
    fig.show()


def fuck(num):
    ax1.cla()
    plot_fuck(num)

    res = num
    last_res = -1
    plot_line(res, num)
    count = 0
    while abs(last_res - res) > 1.0e-5:
        last_res = res
        res = (res + num / res) / 2

        plot_tangent(res, last_res, 2 * last_res)
        plot_line(res, num)
        time.sleep(0.3)
        count += 1
        # if nn % 1000 == 0:
        #     print (nn, ' ', a)
    print(count)
    return res

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='运算', command=self.hello)
        self.alertButton.pack(side = LEFT)
        self.quitButton = Button(self, text='退出', command=self.quit)
        self.quitButton.pack(side = LEFT)

    def hello(self):
        num = float(self.nameInput.get())
        result = fuck(num)
        messagebox.showinfo('结果: ', result)






if __name__ == '__main__':
    # initial the figure.
    fig = plt.figure(1)

    ax1 = fig.add_subplot(111)
    ax1.set_title('ewton\'s method')

    app = Application()
    # 设置窗口标题:
    app.master.title('开根号')
    # 主消息循环:
    app.mainloop()