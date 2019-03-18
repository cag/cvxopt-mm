import tkinter as tk
from tkinter import ttk
from cvxopt import solvers, matrix, spdiag, log


root = tk.Tk()
root.title('Convex Optimization Market Maker Simulation')

app = ttk.Frame(root)
app.pack()

lhsframe = ttk.Frame(app)
lhsframe.pack(side='left')

liquidityparamframe = ttk.LabelFrame(lhsframe, text='liquidity parameter')
liquidityparamframe.pack()
liquidityparam = tk.StringVar()
liquidityparamentry = ttk.Entry(
    liquidityparamframe, textvariable=liquidityparam)
liquidityparamentry.pack()
resetbtn = ttk.Button(
    liquidityparamframe,
    text='Reset',
    command=lambda: print('reset with', liquidityparam.get()),
)
resetbtn.pack()
lossboundframe = ttk.LabelFrame(liquidityparamframe, text='loss bound')
lossboundframe.pack()
lossbound = tk.StringVar()
lossboundlabel = ttk.Label(
    lossboundframe, textvariable=lossbound)
lossboundlabel.pack()

conditionsframe = ttk.LabelFrame(lhsframe, text='conditions')
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

outcomesframe = ttk.LabelFrame(app, text='outcomes')
outcomesframe.pack()
outcomesview = ttk.Treeview(outcomesframe, show='tree')
outcomesview.pack()

tradeframe = ttk.LabelFrame(outcomesframe, text='trade')
tradeselectedoutcomeframe = ttk.LabelFrame(tradeframe, text='selected outcome')
tradeselectedoutcomeframe.pack()
tradeselectedoutcome = tk.StringVar()
tradeselectedoutcomelabel = ttk.Label(
    tradeselectedoutcomeframe, textvariable=tradeselectedoutcome)
tradeselectedoutcomelabel.pack()
tradeframe.pack()
tradeamt = tk.StringVar()
tradeamtentry = ttk.Entry(tradeframe, textvariable=tradeamt)
tradeamtentry.pack()
tradecostframe = ttk.LabelFrame(tradeframe, text='cost')
tradecostframe.pack()
tradecost = tk.StringVar()
tradecostlabel = ttk.Label(tradecostframe, textvariable=tradecost)
tradecostlabel.pack()
tradebtn = ttk.Button(tradeframe, text='Trade',
                      command=lambda: print('trade', tradeamt.get()))
tradebtn.pack()


app.mainloop()
