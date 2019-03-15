import tkinter as tk
from tkinter import ttk
from cvxopt import solvers, matrix, spdiag, log


root = tk.Tk()
root.title('Convex Optimization Market Maker Simulation')

app = ttk.Frame(root)
app.pack()

resetformframe = ttk.Frame(app)
resetformframe.pack(side='left')

fundingframe = ttk.LabelFrame(app, text='funding')
fundingframe.pack()
funding = tk.StringVar()
fundingentry = ttk.Entry(fundingframe, textvariable=funding)
fundingentry.pack()
resetbtn = ttk.Button(fundingframe, text='Reset',
                      command=lambda: print('reset with', funding.get()))
resetbtn.pack()

conditionsframe = ttk.LabelFrame(app, text='conditions')
conditionsframe.pack(side='left')
newconditionquestionlabel = ttk.Label(conditionsframe, text='question:')
newconditionquestionlabel.pack()
newconditionquestion = tk.StringVar()
newconditionquestionentry = ttk.Entry(
    conditionsframe, textvariable=newconditionquestion)
newconditionquestionentry.pack()
newconditionoutcomeslabel = ttk.Label(conditionsframe, text='outcomes:')
newconditionoutcomeslabel.pack()
newconditionoutcomes = tk.StringVar()
newconditionoutcomesentry = ttk.Entry(
    conditionsframe, textvariable=newconditionoutcomes)
newconditionoutcomesentry.pack()
addconditionbtn = ttk.Button(
    conditionsframe,
    text='Add condition',
    command=lambda: print(
        'add condition',
        newconditionquestion.get(),
        'with outcomes',
        newconditionoutcomes.get()
    )
)
addconditionbtn.pack()
conditionsview = ttk.Treeview(conditionsframe, show='tree')
conditionsview.pack()
conditionsview.heading('#0', text='conditions')
cond1id = conditionsview.insert('', 'end', text='Fav letter?')
conditionsview.insert(cond1id, 'end', text='a')
conditionsview.insert(cond1id, 'end', text='b')
conditionsview.insert(cond1id, 'end', text='c')
cond2id = conditionsview.insert('', 'end', text='How to ...?')
conditionsview.insert(cond2id, 'end', text='d')
conditionsview.insert(cond2id, 'end', text='e')
conditionsview.insert(cond2id, 'end', text='f')
cond3id = conditionsview.insert('', 'end', text='Wat')
conditionsview.insert(cond3id, 'end', text='x')
conditionsview.insert(cond3id, 'end', text='y')
conditionsview.insert(cond3id, 'end', text='z')
conditionsview.insert(cond3id, 'end', text='w')

outcomesframe = ttk.LabelFrame(app, text='outcomes')
outcomesframe.pack(side='right')
outcomesview = ttk.Treeview(outcomesframe, show='tree')
outcomesview.pack()


app.mainloop()
