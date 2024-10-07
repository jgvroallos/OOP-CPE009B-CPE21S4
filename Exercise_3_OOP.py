from tkinter import *


class MyWindow:
    def __init__(self, win):

        win.config(bg="#1E1F22")

        self.Label1 = Label(win, fg="Blue", text="Standard Calculator")
        self.Label1.place(x=155, y=25)

        self.Label2 = Label(win, fg="Green", text="Number 1: ")
        self.Label2.place(x=100, y=80)

        self.Entry1 = Entry(win, bd=3)
        self.Entry1.place(x=192, y=80)

        self.Label3 = Label(win, fg="Green", text="Number 2: ")
        self.Label3.place(x=100, y=105)

        self.Entry2 = Entry(win, bd=3)
        self.Entry2.place(x=192, y=105)

        self.Label4 = Label(win, fg="Red", text="Result: ")
        self.Label4.place(x=100, y=130)

        self.Entry3 = Entry(win, bd=3)
        self.Entry3.place(x=192, y=130)

        self.Button1 = Button(win, fg="BLACK", text="Add (+)", command=self.add)
        self.Button1.place(x=100, y=175)

        self.Button2 = Button(win, fg="BLACK", text="Sub (-)", command=self.subtract)
        self.Button2.place(x=160, y=175)

        self.Button3 = Button(win, fg="BLACK", text="Mul (x)", command=self.multiply)
        self.Button3.place(x=215, y=175)

        self.Button4 = Button(win, fg="BLACK", text="Div (÷)", command=self.divide)
        self.Button4.place(x=273, y=175)

        self.Button5 = Button(win, fg="BLACK", text="CLEAR", height=1, width=30, command=self.clear)
        self.Button5.place(x=100, y=225)
        self.Button5.bind('<Button-1>', self.clear)

    def add(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def subtract(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multiply(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def divide(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))

    def clear(self):
        self.Entry1.delete(0, 'end')
        self.Entry2.delete(0, 'end')
        self.Entry3.delete(0, 'end')


window = Tk()
MyWin = MyWindow(window)
window.geometry("400x300+25+250")
window.title("Standard Calculator")
window.mainloop()
