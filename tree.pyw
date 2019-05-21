from tkinter import *
from tkinter.ttk import *

class MainWindow(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent)   
        self.parent = parent        
        self.buildUI()

    def buildUI(self):

        # window title

        self.parent.title("test")

        # window config

        self.parent.minsize(width=600, height=320)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=1)
        self.parent.geometry("600x320")

        # menu bar (Settings, About, Exit)

        self.menubar = Menu(self.parent)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="Settings")
        self.filemenu.add_command(label="About")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)

        self.parent.config(menu=self.menubar)

        # entry search

        self.entrySearch = Entry(self.parent)
        self.entrySearch.grid(row=0, column=0, sticky=W+E)

        # button search

        self.buttonSearch = Button(text="Search")
        self.buttonSearch.grid(row=0, column=1)

        # results table

        self.resultsTable = Treeview(self.parent)
        self.resultsTable["columns"] = ("title", "artist", "length", "bitrate", "status")
        self.resultsTable["show"] = "headings" # remove first empty column (id)
        self.resultsTable.heading("title", text="Title")
        self.resultsTable.heading("artist", text="Artist")
        self.resultsTable.heading("length", text="Length")
        self.resultsTable.heading("bitrate", text="Bitrate")
        self.resultsTable.heading("status", text="Status")
        self.resultsTable.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)

        # bottom status bar

        self.statusBar = Label(self.parent, text="Ready")
        self.statusBar.grid(row=2, column=0, sticky=W)

def main():

    root = Tk()
    app = MainWindow(root)
    root.mainloop()  

if __name__ == '__main__':
    main()