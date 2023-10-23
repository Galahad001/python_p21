from tkinter import *
from tkinter import messagebox

root = Tk()

def click():
    login = loginInput.get()
    password_f = password.get()

    info_str = f'Данные: {str(login)}, {str(password_f)}'
    messagebox.showinfo(title='Название', message=info_str)

    # messagebox.showerror(title='', message='Error!')

root.title('Тест')
root.wm_attributes('-alpha', 0.9)
root.geometry('250x400')

root.resizable(width=False, height=False)

# Представляет чтото вроде вывода холста
canvas = Canvas(root, height=400, width=250, bg='black')
canvas.pack()

# Рамка что содержит в себе другие визуальные компоненты
frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)

# Для текста
title = Label(frame, text='Текст', bg='blue')
title.pack()
btn = Button(frame, text='Кнопка', bg='green', command=click)
btn.pack()

# Текстовое поле
loginInput = Entry(frame, bg='white')
loginInput.pack()
password = Entry(frame, bg='white', show='*')
password.pack()

root.mainloop()