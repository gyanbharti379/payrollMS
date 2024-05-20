import tkinter
import tkinter.ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from random import random, randint,randrange


def main():
    ForgetPassword()

class ForgetPassword:

    def __init__(self):

# ------------------------------Area for creating window -------------------------------------------------#

        self.master = tkinter.Tk()
        self.master.geometry("500x390+450+150")
        self.master.title("Electricity Billing Management System")

        img = Image.open("icon/iconwin.png")
        ImageLabel = ImageTk.PhotoImage(img)
        self.master.iconphoto(True, ImageLabel)
        self.master.resizable(False, False)
        self.master.bind("<Destroy>", self.on_close)

# ------------------------------Area for creating window --------------------END-----------------------------#

# ------------------------------Area for Creating Form -------------------------------------------------#

        self.frame = tkinter.Frame(self.master)
        self.frame.configure(bg="#d3e0c9")
        self.frame.pack()

        self.Title_label = tkinter.Label(self.frame, text="Forget Form", fg="blue",bg="#d3e0c9",
                                         font=("bookman old style", 25, "underline","bold"))
        self.Title_label.grid(row=0, column=0)

# ---------------First Frame -------------------------
        self.FirstFrame = tkinter.LabelFrame(self.frame, text="User information",font=("bookman old style", 15), bg="#d3e0c9")
        self.FirstFrame.grid(row=1,column=0, sticky="news", padx=20, pady=12)

        self.EmpID_Label = tkinter.Label(self.FirstFrame,padx=50,  text="Employee ID",font=("bookman old style",12), bg="#d3e0c9")
        self.EmpID_Label.grid(row=0, column=0, sticky="w")

        self.EmpIDEntry = tkinter.Entry(self.FirstFrame,   font=("bookman old style", 10), width=25)
        self.EmpIDEntry.grid(row=0, column=1, sticky="w")
        self.EmpIDEntry.focus_set()
        self.EmpIDEntry.bind("<Return>", self.on_enter_empid)

        self.Name_Label = tkinter.Label(self.FirstFrame, padx=50, text="Name",font=("bookman old style",12), bg="#d3e0c9")
        self.Name_Label.grid(row=1,column=0, sticky="w")

        self.NameEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style", 10), width=25)
        self.NameEntry.grid(row=1, column=1, sticky="w")
        self.NameEntry.bind("<Return>", self.on_enter_Name)

        self.UserName_Label = tkinter.Label(self.FirstFrame, padx=50, text="User ID",font=("bookman old style",12), bg="#d3e0c9")
        self.UserName_Label.grid(row=2, column=0, sticky="w")

        self.UserNameEntry = tkinter.Entry(self.FirstFrame,   font=("bookman old style",10), width=25)
        self.UserNameEntry.grid(row=2, column=1, sticky="w")
        self.UserNameEntry.bind("<Return>", self.on_enter_userName)

        self.UserType_Label = tkinter.Label(self.FirstFrame, padx=50, text="User Type",font=("bookman old style",12), bg="#d3e0c9")
        self.UserType_Label.grid(row=3, column=0, sticky="w")

        self.UserType_Combobox = tkinter.ttk.Combobox(self.FirstFrame, values=["", "Admin", "User"],
                                                      font=("bookman old style", 10))
        self.UserType_Combobox.grid(row=3, column=1, sticky="w")
        self.UserType_Combobox.configure(width=22)
        self.UserType_Combobox.bind("<Return>", self.on_enter_UTypeCombobox)

        self.NewPassword_Label = tkinter.Label(self.FirstFrame,padx=50,  text="Password",font=("bookman old style",12), bg="#d3e0c9")
        self.NewPassword_Label.grid(row=4, column=0, sticky="w")

        self.NewPasswordEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style", 10), width=25)
        self.NewPasswordEntry.grid(row=4, column=1, sticky="w")
        self.NewPasswordEntry.bind('<Return>', self.on_enter_NewPass)

        self.RePassword_Label = tkinter.Label(self.FirstFrame,padx=50,  text="Re-Password",font=("bookman old style",12), bg="#d3e0c9")
        self.RePassword_Label.grid(row=5, column=0, sticky="w")

        self.RePasswordEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",10), width=25)
        self.RePasswordEntry.grid(row=5, column=1, sticky="w")
        self.RePasswordEntry.bind("<Return>", self.on_enter_RePass)

        for widget in self.FirstFrame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

# ----------Button Frame ----------------------------
        self.ButtonFrame = tkinter.LabelFrame(self.frame, bg="#d3e0c9")
        self.ButtonFrame.grid(row=2, column=0, sticky="news", padx=20, pady=12)

        self.resetButton = tkinter.Button(self.ButtonFrame, text="Reset", width=22,bg="#FF7575", height=2,
                                          font=("bookman old style", 12),command=self.resetallfield)
        self.resetButton.grid(row=0, column=0)

        self.SubmitButton = tkinter.Button(self.ButtonFrame, text="Submit",height=2, width=23,bg="#ceffcf",
                                           font=("bookman old style", 12),command=self.submit_Mouse)
        self.SubmitButton.grid(row=0, column=2)
        self.SubmitButton.bind("<Return>", self.on_enter_submit)

        self.master.mainloop()

# ------------------------------Area for creating Form ----------------End---------------------------------#

# generate employee id with random number
    def on_enter_empid(self, event):
        self.NameEntry.focus_set()

    def on_close(self, event):
        self.master.quit()

    def on_enter_Name(self, event):
        self.UserNameEntry.focus_set()

    def on_enter_userName(self, event):
        self.UserType_Combobox.focus_set()

    def on_enter_UTypeCombobox(self, event):
        self.NewPasswordEntry.focus_set()

    def on_enter_NewPass(self, event):
        import passwordValidation
        passwordValidation.passValidation.password_passfield_validation(passwordValidation, self.NewPasswordEntry.get())
        self.RePasswordEntry.focus_set()

    def on_enter_RePass(self, event):
        if self.NewPasswordEntry.get() == self.RePasswordEntry.get():
            self.NewPasswordEntry.focus_set()
        else:
            tkinter.messagebox.showerror("Error", "Password not match")
            self.RePasswordEntry.focus_set()


    # reset all fields
    def resetallfield(self):
        self.EmpIDEntry.delete(0,tkinter.END)
        self.NameEntry.delete(0,tkinter.END)
        self.UserNameEntry.delete(0,tkinter.END)
        self.UserType_Combobox.current(0)
        self.NewPasswordEntry.delete(0,tkinter.END)
        self.RePasswordEntry.delete(0, tkinter.END)


    def on_enter_submit(self,event):
        self.submit()

    def submit_Mouse(self):
        self.submit()


    def submit(self):

        u1 = self.EmpIDEntry.get().lower()
        u2 = self.NameEntry.get().lower()
        u3 = self.UserNameEntry.get().lower()

        u5 = self.NewPasswordEntry.get()

        try:

            import Conn
            self.myconnect = Conn.Conn.makeConnection(Conn)

            self.mycursor = self.myconnect.cursor()
            q = f"update login set uname = '{u3}', pass = '{u5}' where empid = '{u1}';"

            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showerror("Error", "Data update successfully")

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()
            self.resetallfield()



if __name__=="__main__":
    main()