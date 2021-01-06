"""
@ encoding:utf-8
@ author:nxc
@ GitHub:
@ 搜索引擎主函数
@ 借助MySQL的正则模糊检索方式
@ 代码仅用于学习
"""
import tkinter as tk
import tkinter.messagebox
from setMySQL import MySQLData
from setSearchData import get_html
import webbrowser
DataBase = MySQLData()


class ConTextWindow:
    def __init__(self, href, text):
        self.href = href
        self.window = tk.Tk()
        self.source = get_html(href)
        self.text = text

    def callback(self, event):
        webbrowser.open_new(self.href)

    def start(self):
        self.window.title('检索文本概要（附超链接查看原文）')
        self.window.geometry('800x681+200+100')
        self.window.resizable(False, False)
        text = tk.Text(self.window, font="宋体 12 bold")
        text.pack()
        text.insert(tk.INSERT, self.text)
        link = tk.Label(self.window, text="阅读原文", fg="blue", cursor="hand2", font="宋体 12 bold")
        link.pack()
        link.bind("<Button-1>", self.callback)
        tk.mainloop()


class ListGUI:
    def __init__(self, message):
        self.window = tk.Tk()
        self.message = message
        self.searchList = DataBase.search(self.message)
        self.listLen = len(self.searchList)
        self.point = 0

    def page_up(self):
        print(self.point)
        if self.point % 5 != 0:
            text = self.point % 5
            self.point = self.point-5-text
        else:
            self.point -= 10
        print(self.point)
        self.window.destroy()
        self.window = tk.Tk()
        self.start()

    def page_down(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.start()

    def contextWindow1(self):
        if self.point % 5 != 0:
            text = self.point % 5
            num = self.point - text
        else:
            num = self.point - 5
        href = self.searchList[num][1]
        text = self.searchList[num][3]
        ConTextWindow(href, text).start()

    def contextWindow2(self):
        if self.point % 5 != 0:
            text = self.point % 5
            num = self.point - text
        else:
            num = self.point - 5
        href = self.searchList[num + 1][1]
        text = self.searchList[num + 1][3]
        ConTextWindow(href, text).start()

    def contextWindow3(self):
        if self.point % 5 != 0:
            text = self.point % 5
            num = self.point - text
        else:
            num = self.point - 5
        href = self.searchList[num + 2][1]
        text = self.searchList[num + 2][3]
        ConTextWindow(href, text).start()

    def contextWindow4(self):
        if self.point % 5 != 0:
            text = self.point % 5
            num = self.point - text
        else:
            num = self.point - 5
        href = self.searchList[num + 3][1]
        text = self.searchList[num + 3][3]
        ConTextWindow(href, text).start()

    def contextWindow5(self):
        if self.point % 5 != 0:
            text = self.point % 5
            num = self.point - text
        else:
            num = self.point - 5
        href = self.searchList[num + 4][1]
        text = self.searchList[num + 4][3]
        ConTextWindow(href, text).start()

    def start(self):
        if self.listLen == 0:
            tk.messagebox.showinfo("Tips!", "未检索到相关内容")
            self.window.destroy()
            return
        self.window.title('检索内容:'+self.message)
        self.window.geometry('1200x681+200+100')
        self.window.resizable(False, False)
        button_1 = tk.Button(self.window, text=self.searchList[self.point][2]+'\n'+self.searchList[self.point][4]+'\n'+self.searchList[self.point][5], font="宋体 12 bold", command=self.contextWindow1)
        button_1.place(x=40, y=10, width=1100, height=80)
        self.point += 1
        if self.point != self.listLen:
            button_2 = tk.Button(self.window, text=self.searchList[self.point][2]+'\n'+self.searchList[self.point][4] + '\n' + self.searchList[self.point][5], font="宋体 12 bold", command=self.contextWindow2)
            button_2.place(x=40, y=110, width=1100, height=80)
            self.point += 1
            if self.point != self.listLen:
                button_3 = tk.Button(self.window, text=self.searchList[self.point][2] + '\n' + self.searchList[self.point][4] + '\n' + self.searchList[self.point][5], font="宋体 12 bold", command=self.contextWindow3)
                button_3.place(x=40, y=210, width=1100, height=80)
                self.point += 1
                if self.point != self.listLen:
                    button_4 = tk.Button(self.window, text=self.searchList[self.point][2] + '\n' + self.searchList[self.point][4] + '\n' +self.searchList[self.point][5], font="宋体 12 bold", command=self.contextWindow4)
                    button_4.place(x=40, y=310, width=1100, height=80)
                    self.point += 1
                    if self.point != self.listLen:
                        button_5 = tk.Button(self.window, text=self.searchList[self.point][2] + '\n' + self.searchList[self.point][4] + '\n' +self.searchList[self.point][5], font="宋体 12 bold", command=self.contextWindow5)
                        button_5.place(x=40, y=410, width=1100, height=80)
                        self.point += 1

        if self.point > 5:
            button_6 = tk.Button(self.window, text="上一页", font="宋体 12 bold", command=self.page_up)
            button_6.place(x=350, y=580, width=200, height=80)
        if self.point < self.listLen:
            button_7 = tk.Button(self.window, text="下一页", font="宋体 12 bold", command=self.page_down)
            button_7.place(x=750, y=580, width=200, height=80)
        self.window.mainloop()
        

class MainGUI:
    def __init__(self):
        self.window = tk.Tk()

    def start(self):
        self.window.title('DUT搜索引擎之国务院文件检索')
        self.window.geometry('1068x681+200+100')
        self.window.resizable(False, False)
        # 黑色微透明窗口
        self.window["bg"] = "black"
        self.window.attributes("-alpha", 0.9)
        image_1 = tk.PhotoImage(file='img2.png')
        image_2 = tk.PhotoImage(file='img1.png')
        imgLabel_1 = tk.Label(self.window, image=image_1)
        imgLabel_1.place(x=20, y=200)
        imgLabel_2 = tk.Label(self.window, image=image_2)
        entry_1 = tk.Entry(self.window, show=None, highlightcolor='red', bg='grey', font="仿宋 18 bold")
        entry_1.place(x=200, y=400, width=500, height=50)

        def listWindow():
            ListGUI(entry_1.get()).start()
        button_1 = tk.Button(self.window, text='检索！', font="仿宋 18 bold", command=listWindow)
        button_1.place(x=750, y=400, width=120, height=50)
        self.window.mainloop()


def main():
    windows = MainGUI()
    windows.start()
    DataBase.down_connect()


if __name__ == '__main__':
    main()
