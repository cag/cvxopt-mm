from itertools import combinations, product
from collections import namedtuple
import tkinter as tk
from tkinter import ttk
from cvxopt import solvers, matrix, spdiag, log


class Outcome:
    pass


Condition = namedtuple("Condition", ("question", "outcomeslots"))

liquidityparam = 1.0
conditions = []
outcomes = {}


def reset_liquidity_param():
    global liquidityparamvar, liquidityparam
    liquidityparam = float(liquidityparamvar.get())
    liquidityparamvar.set(str(liquidityparam))


def add_new_condition():
    global newconditionquestionvar, newconditionoutcomeslotsvar, conditions, conditionsview
    question = newconditionquestionvar.get()
    outcomeslots = [o.strip() for o in newconditionoutcomeslotsvar.get().split(",")]

    if len(outcomeslots) < 2:
        raise ValueError(
            "not enough outcome slots specified ({})".format(len(outcomeslots))
        )

    for n in range(len(conditions) + 1):
        for conds in combinations(conditions, n):
            for outcomeid in product(
                *(cond.outcomeslots for cond in conds), outcomeslots
            ):
                outcome = Outcome()
                outcomes[outcomeid] = outcome

    conditions.append(Condition(question, outcomeslots))

    cid = conditionsview.insert("", "end", text=question)
    for outcome in outcomeslots:
        conditionsview.insert(cid, "end", text=outcome)


root = tk.Tk()
root.title("Convex Optimization Market Maker Simulation")
app = ttk.Frame(root)
app.pack()

lhsframe = ttk.Frame(app)
lhsframe.pack(side="left")

liquidityparamframe = ttk.LabelFrame(lhsframe, text="liquidity parameter")
liquidityparamframe.pack()
liquidityparamvar = tk.StringVar()
liquidityparamentry = ttk.Entry(liquidityparamframe, textvariable=liquidityparamvar)
liquidityparamentry.pack()
resetbtn = ttk.Button(liquidityparamframe, text="Reset", command=reset_liquidity_param)
resetbtn.pack()
lossboundframe = ttk.LabelFrame(liquidityparamframe, text="loss bound")
lossboundframe.pack()
lossboundvar = tk.StringVar()
lossboundlabel = ttk.Label(lossboundframe, textvariable=lossboundvar)
lossboundlabel.pack()

conditionsframe = ttk.LabelFrame(lhsframe, text="conditions")
conditionsframe.pack(side="left")
newconditionquestionlabel = ttk.Label(conditionsframe, text="question:")
newconditionquestionlabel.pack()
newconditionquestionvar = tk.StringVar()
newconditionquestionentry = ttk.Entry(
    conditionsframe, textvariable=newconditionquestionvar
)
newconditionquestionentry.pack()
newconditionoutcomeslotslabel = ttk.Label(conditionsframe, text="outcomes:")
newconditionoutcomeslotslabel.pack()
newconditionoutcomeslotsvar = tk.StringVar()
newconditionoutcomeslotsentry = ttk.Entry(
    conditionsframe, textvariable=newconditionoutcomeslotsvar
)
newconditionoutcomeslotsentry.pack()
addconditionbtn = ttk.Button(
    conditionsframe, text="Add condition", command=add_new_condition
)
addconditionbtn.pack()
conditionsview = ttk.Treeview(conditionsframe, show="tree")
conditionsview.pack()


outcomesframe = ttk.LabelFrame(app, text="outcomes")
outcomesframe.pack()
outcomesview = ttk.Treeview(outcomesframe, show="tree")
outcomesview.pack()
outcomesview.insert("", "end", text="foo")
for sequence in (*outcomesview.event_info(), "<Button-1>"):
    outcomesview.bind(sequence, lambda e: print("something selected", e))

tradeframe = ttk.LabelFrame(outcomesframe, text="trade")
tradeselectedoutcomeframe = ttk.LabelFrame(tradeframe, text="selected outcome")
tradeselectedoutcomeframe.pack()
tradeselectedoutcome = tk.StringVar()
tradeselectedoutcomelabel = ttk.Label(
    tradeselectedoutcomeframe, textvariable=tradeselectedoutcome
)
tradeselectedoutcomelabel.pack()
tradeframe.pack()
tradeamt = tk.StringVar()
tradeamtentry = ttk.Entry(tradeframe, textvariable=tradeamt)
tradeamtentry.pack()
tradecostframe = ttk.LabelFrame(tradeframe, text="cost")
tradecostframe.pack()
tradecost = tk.StringVar()
tradecostlabel = ttk.Label(tradecostframe, textvariable=tradecost)
tradecostlabel.pack()
tradebtn = ttk.Button(
    tradeframe, text="Trade", command=lambda: print("trade", tradeamt.get())
)
tradebtn.pack()

app.mainloop()
