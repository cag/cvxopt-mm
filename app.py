import tkinter as tk
from tkinter import ttk
from cvxopt import solvers, matrix, spdiag, log


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lf = ttk.LabelFrame(self, text='thing')
        self.lf.pack()
        self.l1 = ttk.Label(self.lf, text='3.1415')
        self.l1.pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
