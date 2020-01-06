import tkinter
from tkinter import ttk
#
# root = tkinter.Tk()
#
# #设置按钮
# tkinter.Button(root, text='Click me').pack()
# ttk.Button(root, text='Click me').pack()

#设置标签
#label = tkinter.Label(root, text='kello world')
#label.pack()


def startup_dialog(labeltext):
    result = None
    rooty_dialog = tkinter.Tk()
    #框架控件；在屏幕上显示一个矩形区域，多用来作为容器
    big_frame = ttk.Frame(rooty_dialog)
    big_frame.pack(fill='both', expand=True)

    # result is left to None if the dialog is closed without clicking OK
    def on_ok():
        # usually 'result = entry.get()' creates a local variable called
        # result, but this thing makes it also appear outside on_ok()
        nonlocal result

        result = entry.get()
        rooty_dialog.destroy()   # stops rooty_dialog.mainloop()

    label = ttk.Label(big_frame, text=labeltext)
    #确定位置
    label.place(relx=0.5, rely=0.3, anchor='center')
    #输入控件；用于显示简单的文本内容
    entry = ttk.Entry(big_frame)
    entry.place(relx=0.5, rely=0.5, anchor='center')
    okbutton = ttk.Button(big_frame, text="OK", command=on_ok)
    okbutton.place(relx=0.5, rely=0.8, anchor='center')
    # 设定窗口的大小(长 * 宽)
    rooty_dialog.geometry('250x150')
    rooty_dialog.mainloop()

    # now the dialog's mainloop has stopped, so the dialog doesn't exist
    # anymore and creating another root window is ok
    return result


name = startup_dialog("Enter your name:")
if name is not None:      # the user clicked OK
    root = tkinter.Tk()
    big_frame = ttk.Frame(root)
    big_frame.pack(fill='both', expand=True)

    label = ttk.Label(big_frame, text=("Hello %s!" % name))
    label.pack()
    root.mainloop()


