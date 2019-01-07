import tkinter as tk
root = tk.Tk()

#创建三个 Label 分别添加到root窗体中
#Label是一种用来显示文字或者图片的组件
tk.Label(root,text = 'pack1',bg = 'red').pack()
tk.Label(root, text = 'pack2', bg = 'blue').pack()
tk.Label(root, text = 'pack3', bg = 'green').pack()

root.mainloop()