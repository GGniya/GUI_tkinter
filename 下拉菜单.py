import tkinter as tk
root = tk.Tk()
root.geometry('400x200')
root.title("下拉菜单")
def hello():
    print('hello')

def about():
    print('我是开发者')

menubar = tk.Menu(root)

#创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#创建另一个下拉菜单Edit
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit",menu=editmenu)
#创建下拉菜单Help
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#显示菜单
root.config(menu=menubar)

tk.mainloop()