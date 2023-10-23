from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
# t_00 = Label(text='nw' )
# t_01 = Label(text='n' )
# t_02 = Label(text='ne' )
# t_03 = Label(text='w' )
# t_04 = Label(text='e' )
# t_05 = Label(text='sw' )
# t_06 = Label(text='s' )
# t_07 = Label(text='se' )

# t_00.pack(anchor="nw")
# t_01.pack(anchor="n")
# t_02.pack(anchor="ne")
# t_03.pack(anchor="w")
# t_04.pack(anchor="e")
# t_05.pack(anchor="sw")
# t_06.pack(anchor="s")
# t_07.pack(anchor="se")

btn = ttk.Button(text="Click me")
btn.pack(fill=BOTH, expand=True)
 
root.mainloop()