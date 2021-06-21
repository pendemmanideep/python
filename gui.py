import tkinter as tk
from tkinter import END

t=tk.Tk()
def func():
    print(e.get())
def click(Label):
    e.delete(0,END)
l=tk.Label(t, text='SWETHA', fg='red', bg='blue', font=('TimesNewRoman', 50, 'bold', 'underline', 'italic'))
l.pack()
e= tk.Entry(t)
e.insert(0,'User name')
e.place(x=30,y=10,height=30,width=4000)
e.bind('<Button-1>',click)

b=tk.Button(t, text='print', command=func, fg='white',
             bg='black', height=5, width=50, activebackground='yellow',
            font=('TimesNewRoman',50,'bold','underline','italic'))

b.place(x=30,y=100)
t.mainloop()
