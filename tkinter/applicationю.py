from tkinter import *
from tkinter import ttk

def finish():
    root.destroy()
    print('Закрытие окна')

root = Tk()
root.title('Приложение на Tkinter')
root.geometry('300x250+400+200')

label = Label(text='Hello User')
label.pack()

# root.update_idletasks()
# print(root.geometry())


# root.resizable(False,False)

root.protocol('WM_DELETE_WINDOW', finish)

# root.attributes('-fullscreen', True)
# root.attributes('-alpha', 0.5)
# root.attributes('-toolwindow', False)


btn = ttk.Button(text='Click')
btn.pack()
def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   "*depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth+1)

root.update()     # обновляем информацию о виджетах
print_info(root)

root.mainloop() 