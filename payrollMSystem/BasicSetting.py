import tkinter
import tkinter.ttk
import tkinter.messagebox
import pyotp
import qrcode
from PIL import Image, ImageTk
import hashlib
import Conn
import idgenerator
import login


class BasicSettingsForm:

    def __init__(self):

        self.otp = None

# ------------------------------Area for creating window ------------------------START---------------------------#

        self.master = tkinter.Tk()
        self.master.geometry("1300x750+100+10")
        self.master.title("Payroll Management System")

        # change the icon of window
        img = Image.open("icon/iconwin.png")
        ImageLabel = ImageTk.PhotoImage(img)
        self.master.iconphoto(True, ImageLabel)

        self.master.resizable(False, False)
        self.master.bind("<Destroy>", self.on_close)

# ------------------Area for creating window -----------------------------------------END------------------------#

# -----------------Create From ------------------------------------------------Start ----------------------------#

        self.Title_label = tkinter.Label(self.master, text=". . . Welcome to Payroll Management System . . .", fg="blue",bg="#d3e0c9",
                                width=90, font=("bookman old style", 20, "underline","bold"))
        self.Title_label.place(x=0, y=0)

        self.Sub_Title_label = tkinter.Label(self.master, text="There are some Basic Settings of this Software . . .",
                                         fg="blue", bg="#d3e0c9",
                                         width=90, font=("bookman old style", 20, "underline", "bold"))
        self.Sub_Title_label.place(x=0, y=50)

# ---------------First Frame -------------------------
        self.FirstFrame = tkinter.Frame(self.master,  width=1500, height=700,  bg="#d3e0c9")
        self.FirstFrame.place(x=0, y=100)

        self.User_Img = Image.open("images/payrollimage.webp").resize((150,150),Image.BOX)
        self.User_PhotoImage = ImageTk.PhotoImage(self.User_Img)

        self.UserImage_Label = tkinter.Label(self.FirstFrame, image=self.User_PhotoImage, bg="#d3e0c9")
        self.UserImage_Label.place(x=190, y=10)

        self.OwnerName_Label = tkinter.Label(self.FirstFrame, text="Owner Name", font=("bookman old style", 15),
                                            bg="#d3e0c9")
        self.OwnerName_Label.place(x=20, y=180)

        self.OwnerName_Entry = tkinter.Entry(self.FirstFrame, font=("bookman old style", 15), width=20)
        self.OwnerName_Entry.place(x=300, y=180)
        self.OwnerName_Entry.focus_set()
        self.OwnerName_Entry.bind("<Return>", self.onEnterOwnerName)

        self.CompanyName_Label = tkinter.Label(self.FirstFrame, text="Company Name",font=("bookman old style",15), bg="#d3e0c9")
        self.CompanyName_Label.place(x=20, y=220)

        self.CompanyName_Entry = tkinter.Entry(self.FirstFrame, font=("bookman old style", 15), width=20)
        self.CompanyName_Entry.place(x=300, y=220)
        self.CompanyName_Entry.bind("<Return>", self.onEnterCompanyName)

        self.MaxEmployee_Label = tkinter.Label(self.FirstFrame, text="Maximum no of Employee", font=("bookman old style", 15),
                                               bg="#d3e0c9")
        self.MaxEmployee_Label.place(x=20, y=260)

        self.MaxEmployee_Entry = tkinter.Entry(self.FirstFrame, font=("bookman old style", 15), width=20)
        self.MaxEmployee_Entry.place(x=300, y=260)
        self.MaxEmployee_Entry.bind("<Return>", self.onEnterMaxEmployee)

        self.MaxStudents_Label = tkinter.Label(self.FirstFrame, text="Maximum no of Students",
                                               font=("bookman old style", 15),
                                               bg="#d3e0c9")
        self.MaxStudents_Label.place(x=20, y=300)

        self.MaxStudents_Entry = tkinter.Entry(self.FirstFrame, font=("bookman old style", 15), width=20)
        self.MaxStudents_Entry.place(x=300, y=300)
        self.MaxStudents_Entry.bind("<Return>", self.onEnterMaxStudent)

        self.UserType_Label = tkinter.Label(self.FirstFrame, text="User Type", font=("bookman old style", 15),
                                            bg="#d3e0c9")
        self.UserType_Label.place(x=20, y=340)

        self.UserType_Combobox = tkinter.ttk.Combobox(self.FirstFrame, width=28,values=["Owner"],font=("bookman old style",10))
        self.UserType_Combobox.place(x=300, y=340)
        self.UserType_Combobox.bind("<Return>", self.on_enter_UTypeCombobox)

        self.User_Agreement_Label = tkinter.Label(self.FirstFrame, text="Terms and Conditions",font=("bookman old style",15), bg="#d3e0c9")
        self.User_Agreement_Label.place(x=700, y=20)

        self.UserName_Label = tkinter.Label(self.FirstFrame, text="User Name",font=("bookman old style",15), bg="#d3e0c9")
        self.UserName_Label.place(x=20, y=380)

        self.UserName_Entry = tkinter.Entry(self.FirstFrame, font=("bookman old style",15), width=20)
        self.UserName_Entry.place(x=300, y=380)
        self.UserName_Entry.bind("<Return>", self.on_enter_UserName)

        self.Terms_And_Condition_TextArea = tkinter.Text(self.FirstFrame, width=80, height=30,
                                                         font=("bookman old style", 10))
        self.Terms_And_Condition_TextArea.place(x=600, y=60)

        self.Terms_And_Condition_TextArea.insert(1.200, "**User Agreement for Payroll Management System**\n")
        self.Terms_And_Condition_TextArea.insert(2.200, "**1. Introduction**\n")
        self.Terms_And_Condition_TextArea.insert(3.200, "This User Agreement ('Agreement') governs the use of the Payroll Management System provided by [XYZ Company], here in after referred to as 'Provider'. By accessing or using the System, you agree to be bound by the terms and conditions of this Agreement.\n")
        self.Terms_And_Condition_TextArea.insert(4.200, "**2. Access and Use**\n")
        self.Terms_And_Condition_TextArea.insert(5.200, "2.1 **Eligibility**: You must be at least 18 years old and have the legal capacity to enter into this Agreement to use the System.\n")
        self.Terms_And_Condition_TextArea.insert(6.200, "2.2 **Authorized Use**: You agree to use the System solely for the purpose of managing payroll information for your business or organization.\n")
        self.Terms_And_Condition_TextArea.insert(7.200, "2.3 **Account Security**: You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account. Notify Provider immediately of any unauthorized use of your account.\n")
        self.Terms_And_Condition_TextArea.insert(8.200, "**3. Data Protection and Privacy**\n")
        self.Terms_And_Condition_TextArea.insert(9.200, "3.1 **Data Collection**: Provider may collect and process personal data in accordance with its Privacy Policy.\n")
        self.Terms_And_Condition_TextArea.insert(10.200, "3.2 **Data Security**: Provider implements industry-standard security measures to protect your data; however, you acknowledge that no method of transmission over the internet or electronic storage is 100% secure.\n")
        self.Terms_And_Condition_TextArea.insert(11.200, "3.3 **Data Ownership**: You retain ownership of all data uploaded or entered into the System. Provider may use aggregated and anonymized data for analytics and improvement purposes.\n")
        self.Terms_And_Condition_TextArea.insert(12.200, "**4. Fees and Payments**\n")
        self.Terms_And_Condition_TextArea.insert(13.200, "4.1 **Subscription Fees**: Your use of the System may be subject to subscription fees, as outlined in the pricing plan chosen by you.\n")
        self.Terms_And_Condition_TextArea.insert(14.200, "4.2 **Payment Terms**: You agree to pay all applicable fees in a timely manner, as per the payment terms specified by Provider.\n")
        self.Terms_And_Condition_TextArea.insert(15.200, "**5. Intellectual Property**\n")
        self.Terms_And_Condition_TextArea.insert(16.200, "5.1 **Ownership**: The System and all related intellectual property rights belong to Provider.\n")
        self.Terms_And_Condition_TextArea.insert(17.200, "5.2 **License**: Provider grants you a limited, non-exclusive, non-transferable license to use the System for the duration of this Agreement.\n")
        self.Terms_And_Condition_TextArea.insert(18.200, "**6. Termination**\n")
        self.Terms_And_Condition_TextArea.insert(19.200, "6.1 **Termination**: Provider may suspend or terminate your access to the System at any time for violation of this Agreement or for any other reason.\n")
        self.Terms_And_Condition_TextArea.insert(20.200, "6.2 **Effect of Termination**: Upon termination, you must cease all use of the System, and Provider may delete all data associated with your account.\n")
        self.Terms_And_Condition_TextArea.insert(21.200, "**7. Limitation of Liability**\n")
        self.Terms_And_Condition_TextArea.insert(22.200, "7.1 **Disclaimer**: The System is provided 'as is' without warranty of any kind, and Provider shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of or in any way connected with the use of the System.\n")
        self.Terms_And_Condition_TextArea.insert(23.200, "**8. Miscellaneous**\n")
        self.Terms_And_Condition_TextArea.insert(24.200, "8.1 **Governing Law**: This Agreement shall be governed by and construed in accordance with the laws of [Jurisdiction].\n")
        self.Terms_And_Condition_TextArea.insert(25.200, "8.2 **Entire Agreement**: This Agreement constitutes the entire agreement between you and Provider regarding the use of the System and supersedes all prior or contemporaneous understandings and agreements.\n")
        self.Terms_And_Condition_TextArea.insert(26.200, "By using the System, you acknowledge that you have read, understood, and agree to be bound by this Agreement.\n")

        self.Password_Label = tkinter.Label(self.FirstFrame, text="Password",font=("bookman old style",15), bg="#d3e0c9")
        self.Password_Label.place(x=20, y=420)

        self.PasswordEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",15), width=20)
        self.PasswordEntry.place(x=300, y=420)
        self.PasswordEntry.bind('<Return>',self.on_enter_Pass)

        self.RePassword_Label = tkinter.Label(self.FirstFrame, text="Re-Password",font=("bookman old style",15), bg="#d3e0c9")
        self.RePassword_Label.place(x=20,y=460)

        self.RePasswordEntry = tkinter.Entry(self.FirstFrame, font=("bookman old style",15), width=20)
        self.RePasswordEntry.place(x=300,y=460)
        self.RePasswordEntry.bind("<Return>", self.on_enter_RePass)

        self.Check_var = tkinter.IntVar()
        self.User_Agreement_CheckBox = tkinter.Checkbutton(self.FirstFrame, text="Accept Terms and Condition",
                                                           font=("bookman old style",15), bg="#d3e0c9",
                                                           variable = self.Check_var, command=self.Action_UserAgreementCheckBox)
        self.User_Agreement_CheckBox.place(x=233, y=500)

        self.Cancel_Btn_img = Image.open("icon/cancel13.png").resize((30,30),Image.BOX)
        self.Cancel_Btn_PhotoImage = ImageTk.PhotoImage(self.Cancel_Btn_img)

        self.resetButton = tkinter.Button(self.master, text="Reset", width=113,bg="#FF7575", height=30,
                                          image=self.Cancel_Btn_PhotoImage,compound=tkinter.RIGHT,
                                          font=("bookman old style", 15),command=self.resetallfield)
        self.resetButton.place(x=300, y=660)

        self.Submit_Btn_img = Image.open("icon/save1.png").resize((30, 30), Image.BOX)
        self.Submit_Btn_PhotoImage = ImageTk.PhotoImage(self.Submit_Btn_img)

        self.SubmitButton = tkinter.Button(self.master, text="Submit",height=30, width=113,bg="#ceffcf",
                                          image=self.Submit_Btn_PhotoImage, compound=tkinter.RIGHT,
                                           font=("bookman old style", 15),command=self.submit_Mouse)
        self.SubmitButton.place(x=423, y=660)
        self.SubmitButton.config(state=tkinter.DISABLED)
        self.SubmitButton.bind("<Return>", self.on_enter_submit)

        self.master.mainloop()

# -----------------Create From -------------------------------END ----------------------------#

    def on_close(self, event):
        self.master.quit()

    def onEnterOwnerName(self,event):
        if self.OwnerName_Entry.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Enter Owner Name")
            self.OwnerName_Entry.focus_set()

        else:
            self.CompanyName_Entry.focus_set()

    def onEnterCompanyName(self,event):
        if self.CompanyName_Entry.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Enter Company Name")
            self.CompanyName_Entry.focus_set()

        else:
            self.MaxEmployee_Entry.focus_set()

    def onEnterMaxEmployee(self,event):
        if self.MaxEmployee_Entry.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Enter Maximum Employees")
            self.MaxEmployee_Entry.focus_set()

        elif int(self.MaxEmployee_Entry.get()) == 0:
            tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
            self.MaxEmployee_Entry.focus_set()

        else:
            self.MaxStudents_Entry.focus_set()

    def onEnterMaxStudent(self,event):
        if self.MaxStudents_Entry.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Enter Maximum Student")
            self.MaxStudents_Entry.focus_set()

        elif int(self.MaxStudents_Entry.get()) == 0:
            tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
            self.MaxStudents_Entry.focus_set()

        else:
            self.UserType_Combobox.focus_set()

    def on_enter_UTypeCombobox(self, event):
        if self.UserType_Combobox.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Select User Type")
            self.UserType_Combobox.focus_set()

        else:
            self.UserName_Entry.focus_set()

    def on_enter_UserName(self,event):
        if self.UserName_Entry.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Enter User Name")
            self.UserName_Entry.focus_set()

        else:
            self.PasswordEntry.focus_set()

    def on_enter_Pass(self, event):
        if self.PasswordEntry.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Enter Password")
            self.PasswordEntry.focus_set()

        else:
            import passwordValidation
            passwordValidation.passValidation.password_passfield_validation(passwordValidation,self.PasswordEntry.get())
            self.RePasswordEntry.focus_set()

    def on_enter_RePass(self, event):
        if self.RePasswordEntry.get() == "":
            tkinter.messagebox.showerror("Field Blank", "Please Enter Password Again")
            self.RePasswordEntry.focus_set()

        elif self.PasswordEntry.get() != self.RePasswordEntry.get():
            tkinter.messagebox.showerror("Error", "Password not match")
            self.RePasswordEntry.focus_set()

        elif self.PasswordEntry.get() == self.RePasswordEntry.get():
            self.User_Agreement_CheckBox.focus_set()

    def Action_UserAgreementCheckBox(self):
        if self.Check_var.get() == 0:
            tkinter.messagebox.showerror("Field Blank", "Please Check User Agreement")
            self.SubmitButton.config(state=tkinter.DISABLED)
        else:
            self.SubmitButton.config(state=tkinter.ACTIVE, font=("bookman old style",15), bg="#d3e0c9")
            self.SubmitButton.focus_set()


# ------------------------------reset all fields ---------------------------------------------------------------#
    def resetallfield(self):
        self.OwnerName_Entry.delete(0, tkinter.END)
        self.CompanyName_Entry.delete(0, tkinter.END)
        self.MaxEmployee_Entry.delete(0, tkinter.END)
        self.MaxStudents_Entry.delete(0, tkinter.END)
        self.UserName_Entry.delete(0,tkinter.END)
        self.UserType_Combobox.current(0)
        self.PasswordEntry.delete(0,tkinter.END)
        self.RePasswordEntry.delete(0,tkinter.END)
        self.Check_var.set(0)
        self.SubmitButton.config(state=tkinter.DISABLED)
        self.OwnerName_Entry.focus_set()

    def on_enter_submit(self,event):
        self.submit()

    def submit_Mouse(self):
        self.submit()

    def submit(self):

        u1 = self.OwnerName_Entry.get().lower()
        u2 = self.CompanyName_Entry.get().lower()
        u3 = self.MaxEmployee_Entry.get()
        u4 = self.MaxStudents_Entry.get()
        u5 = self.UserName_Entry.get().lower()
        u6 = self.UserType_Combobox.get().lower()
        u7 = self.PasswordEntry.get()

 #----------Encryption applied ---------------------------------#
        uep = hashlib.sha256(u7.encode()).hexdigest()

        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()

# ----------check user name present in the table or not -----------------------------------#
            q = f"select username from login where username='{u5}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchone()

            if row == None:

                q = f"insert into login (ownerName, compName, maxEmp, maxStd, username,utype, pass) values ('{u1}','{u2}','{u3}','{u4}','{u5}','{u6}','{uep}');"

                self.mycursor.execute(q)
                self.myconnect.commit()

                idgenerator.empNoGenerator(u3)
                idgenerator.stdRollNoGenerator(u4)

                tkinter.messagebox.showinfo("Saving . . . ", "Data saved successfully")
                login.main()

            else:
                tkinter.messagebox.showinfo("Message . . .","User Exists please login")

        except Exception as e:
            print(str(e))

        finally:
            self.mycursor.close()
            self.myconnect.close()
            self.resetallfield()

if __name__=="__main__":
    BasicSettingsForm()
