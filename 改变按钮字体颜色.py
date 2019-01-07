import tkinter

class App:
    def __init__(self, master):
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示
        frame = tkinter.Frame(master)
        frame.pack()
        #创建两个button，并作为frame的一部分
        self.button = tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=tkinter.LEFT) #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        self.hi_there = tkinter.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)

    def say_hi(self):
        print ("hi there, this is a class example!"  )

win = tkinter.Tk()
app = App(win)
win.mainloop()