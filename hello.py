# Requirements
# A label with the program name
# A entry field and a button to send messages
# A text widget for the chat history

from tkinter import *
from tkinter import ttk
from turtle import bgcolor


root = Tk()         #GUI "Tk"
root.title("CHAT")


# def the Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

CHATROOM = Label(root, bg="IndianRed", fg="black", text="CHATROOM", font="bold", pady=0, width=20, height=1).grid(
	row=0)

txt = Text(root, bg="pink", fg="black", width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="white", fg="black", font="font", width=55)
e.grid(row=2, column=0)

send = Button(root, text="SEND", font="bold", bg="IndianRed",
command=send).grid(row=2, column=1)

root.mainloop()