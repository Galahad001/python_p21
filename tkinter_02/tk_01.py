# Импорт модуля
from tkinter import *

# Создать обьект класса 
root = Tk()

# ЗАголовок окна
root.title('Проект')

# Задать окну размер
root.geometry('400x400')

# Цвет приложения
root.config(bg='black')

# Чтобы окно не расширялось
# root.resizable(width=False, height=False)
root['bg']='black'


def click():
    print('Привет')
# Создать кнопку
btn = Button(root, text='Кнопка', command=click, bg='lime', activebackground='red', activeforeground='white', font=('Ariel', 20, 'bold'), fg='blue')
btn.pack()

label = Label(root, text='Текст', bg='blue', font=('Ariel', 30, 'bold'), fg='red')
label.pack()

img = PhotoImage(file='edit.png')
l_logo = Label(root, image=img)
l_logo.pack()

root.mainloop()