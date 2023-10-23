from tkinter import *
from random import *

root = Tk()
root.title('Камень ножницы бумага')
root.geometry('600x400')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def What():
    knb = ['Камень', 'Ножницы', 'Бумага']
    value = choice(knb)
    labels.configure(text=value)


labels = Label(root, text='', fg='white', font=('Ariel', 20), bg='black')
labels.pack()

stone = Button(root, text='Камень', bg='white', command=What, font=('Ariel', 20, 'bold'))
stone.place(x=370, y=200)

scissros = Button(root, text='Ножницы', bg='white', command=What, font=('Ariel', 20, 'bold'))
scissros.place(x=270, y=200)

paper = Button(root, text='Бумага', bg='white', command=What, font=('Ariel', 20, 'bold'))
paper.place(x=170, y=200)

root.mainloop()