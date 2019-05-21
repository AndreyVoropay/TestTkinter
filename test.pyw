from tkinter import *
from tkinter.ttk import *

root = Tk()
root.state('zoomed')
root.grid_columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

table = Treeview(show='headings', columns=('fio', 'dr', 'adres'))
table.heading('fio', text='fio')
table.heading('dr', text='dr')
table.heading('adres', text='adres')
table.grid(row=1, sticky=N+S+E+W) #row=1, column=0, columnspan=2

root.mainloop()