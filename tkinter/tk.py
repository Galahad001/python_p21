from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
clicks = 0

def click_btn():
    global clicks
    clicks += 1
    # Изиенить текст на кнопке
    btn['text'] = f'Нажал - {clicks}'

# стандартная кнопка
btn = ttk.Button(text="Нажми", command=click_btn)
btn.pack()

btn_dis = ttk.Button(text='Не рабочая', state=['disabled'])
btn_dis.pack()




def test():
    if btn4['state']=='normal':
        btn4['state']='disabled'
    else:
        btn4['state']='normal'
btn3 = ttk.Button(text='Test', command=test)
btn3.pack()
btn4 = Button(text='btn')
btn4.pack()
 
root.mainloop()