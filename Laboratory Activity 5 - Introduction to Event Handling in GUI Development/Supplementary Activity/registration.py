from tkinter import *
from tkinter import messagebox
import csv

class MainWindow:
    def __init__(self, win):

        # Labels of text input boxes

        self.progName_lbl = Label(win, fg="Black", text="Account Registration", font=("Times New Roman", 22))
        self.progName_lbl.place(x=82, y=10)

        self.firstname_lbl = Label(win, fg="Black", text="First Name: ")
        self.firstname_lbl.place(x=100, y=60)

        self.lastname_lbl = Label(win, fg="Black", text="Last Name: ")
        self.lastname_lbl.place(x=100, y=90)

        self.username_lbl = Label(win, fg="Black", text="User Name: ")
        self.username_lbl.place(x=98, y=120)

        self.password_lbl = Label(win, fg="Black", text="Password: ")
        self.password_lbl.place(x=106, y=150)

        self.emailAdd_lbl = Label(win, fg="Black", text="Email Address: ")
        self.emailAdd_lbl.place(x=83, y=180)

        self.contactNum_lbl = Label(win, fg="Black", text="Contact Number: ")
        self.contactNum_lbl.place(x=69, y=210)

        # Text input boxes

        self.firstname_txt = Entry(win, bd=3)
        self.firstname_txt.place(x=180, y=60)

        self.lastname_txt = Entry(win, bd=3)
        self.lastname_txt.place(x=180, y=90)

        self.username_txt = Entry(win, bd=3)
        self.username_txt.place(x=180, y=120)

        self.password_txt = Entry(win, bd=3, show='*')
        self.password_txt.place(x=180, y=150)

        self.emailAdd_txt = Entry(win, bd=3)
        self.emailAdd_txt.place(x=180, y=180)

        self.contactNum_txt = Entry(win, bd=3)
        self.contactNum_txt.place(x=180, y=210)

        # Submit Button

        self.submit_btn = Button(win, fg="BLACK", text="Submit", height=1, width=15, command=self.submission)
        self.submit_btn.place(x=82, y=250)

        self.clear_btn = Button(win, fg="BLACK", text="Clear", height=1, width=15, command=self.clear)
        self.clear_btn.place(x=208, y=250)

    def submission(self):
        firstname = str(self.firstname_txt.get())
        lastname = str(self.lastname_txt.get())
        username = str(self.username_txt.get())
        password = str(self.password_txt.get())
        emailAdd = str(self.emailAdd_txt.get())
        contactNum = str(self.contactNum_txt.get())
        self.clear()

        dataComp = [firstname, lastname, username, password, emailAdd, contactNum]

        for data in dataComp:
            if data:
                complete = True
            else:
                messagebox.showwarning("Input Error", "User Input is Incomplete, Please try again.")
                complete = False
                self.clear()
                break

        if complete == True:
            messagebox.showinfo("Input Successful", "User Input is Complete, Submission successful.")
            self.csvEntry(dataComp)

    def csvEntry(self, dataComp):
        with open('reg_details.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            field = ["First Name", "Last Name", "User Name", "Password", "Email", "Contact Number"]
            writer.writerow(field)
            writer.writerow(dataComp)

    def clear(self):
        self.firstname_txt.delete(0, 'end')
        self.lastname_txt.delete(0, 'end')
        self.username_txt.delete(0, 'end')
        self.password_txt.delete(0, 'end')
        self.emailAdd_txt.delete(0, 'end')
        self.contactNum_txt.delete(0, 'end')
