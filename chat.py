from tkinter import *
from tkinter import ttk



root = Tk()      
frm = ttk.Frame(root,padding=10)
frm.grid()


ttk.Button(frm, tex="Quit", command=root.destroy).grid(column=2, row=1)
ttk.Label(frm, text="Hello world").grid(column=1, row=0)
ttk.Label(frm, text="Goodbye world").grid(column=0, row=0)


entry= ttk.Entry(frm)
entry.insert(END, "bbbbbbb")
entry.insert(0, "aaaaaa")
entry.grid(column=1,row=2)


'''
radioOn= ttk.Radiuobutton(frm, text="on", value=1).grid(row=2)
radioOff= ttk.Radiuobutton(frm, text="off", value=0).grid(row=3)
'''

root.mainloop()