import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()

# from tkinter import *
# top = Tk()

# #修改窗口名字
top = tkinter.Tk(className="傻胖子")
top.geometry('400x200')
# top.mainloop()

# # 在窗口中加入标签
label = tkinter.Label(top)
label['text']='胖子是傻叉'
label.pack()
# top.mainloop()

# 在窗口中加入按钮
button = tkinter.Button(top)
button['text']='Ok'
button.pack()
# top.mainloop()

# #使按钮有意义
def on_click():
    label['text'] = '胖子不傻?'
    text.set('别逗了')
    top2 = tkinter.Tk(className='真傻')
    top2.geometry('400x200')
    label2 = tkinter.Label(top2)
    label2['text'] = '真傻'
    label2.pack()
    print("胖子真的傻")

# # 添加按钮操作
button['command'] = on_click
button.pack()
# top.mainloop()
# # 添加可编辑文本
text = tkinter.StringVar()
text.set('胖纸是大傻叉')
entry = tkinter.Entry(top)
entry['textvariable'] = text
entry.pack()
top.mainloop()