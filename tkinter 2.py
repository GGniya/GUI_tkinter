from tkinter import *
def H():
    print('胖子是大傻叉')
top = Tk()
top.title("傻胖子")
top.geometry('400x200')     #x 是(x ,y中的x)
btn = Button(top,text="不傻",command=H)   #这里的H是定义的button按钮单机时触发的事件
btn.pack(expand=YES,fill=BOTH) ##将按钮pack，充满整个窗体(只有pack的组件实例才能显示)

mainloop()

