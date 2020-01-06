import tkinter
from tkinter import ttk

root = tkinter.Tk()

#设置按钮
tkinter.Button(root, text='Click me').pack()
ttk.Button(root, text='Click me').pack()

#设置标签
#label = tkinter.Label(root, text='kello world')
#label.pack()


root.mainloop()
