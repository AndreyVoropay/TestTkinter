import tkinter
from tkinter import ttk

class Main(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()        


    def init_main(self):
        toolbar = tkinter.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tkinter.TOP, fill=tkinter.X)

        self.add_img = tkinter.PhotoImage(file='add.gif')
        btn_open_dialog = tkinter.Button(toolbar, text='Add position',
                                         command=self.open_dialog,
                                         bg='#d7d8e0', bd=0,
                                         compound=tkinter.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tkinter.LEFT)

        self.tree = ttk.Treeview(self, selectmode = 'extended',
                                 columns=('id', 'description', 'costs', 'total'),
                                 show='headings')
        self.tree.column('id',          width= 30, anchor=tkinter.CENTER)
        self.tree.column('description', width=100, anchor=tkinter.CENTER)
        self.tree.column('costs',       width= 30, anchor=tkinter.CENTER)
        self.tree.column('total',       width= 30, anchor=tkinter.CENTER)

        self.tree.heading('id',          text='id')
        self.tree.heading('description', text='название')
        self.tree.heading('costs',       text='статья')
        self.tree.heading('total',       text='всего')

        self.tree.pack(fill='both', expand=True)
    
    def open_dialog(self):
        Chield()


class Chield(tkinter.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        

    def init_child(self):
        form_width  = 400
        form_height = 200
        self.title('Add')
        w = root.winfo_screenwidth()  // 2
        h = root.winfo_screenheight() // 2
        w=w-(form_width  // 2)
        h=h-(form_height // 2)
        self.geometry('{}x{}+{}+{}'.format(form_width, form_height, w, h))
        self.resizable(False, False)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk
        
        self.grab_set()
        self.focus_set()


if __name__ == '__main__':
    root = tkinter.Tk()
    app  = Main(root)
    app.pack()
    root.title('Test 1')
    #root.geometry('650x450+100+100')
    root.state('zoomed')
    root.resizable(True, True)
    root.mainloop()
