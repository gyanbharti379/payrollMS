import datetime
import math
import MySQLdb
import pywhatkit as kit
import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import Conn
import getIdNumber

def main():
    UserDashboard()

class UserDashboard():

    total_bill = 0
    total = 0
    userName = ""
    usertype = ""

    def __init__(self):

        self.itemlist = []
        self.stafflist = []
        self.stafflist.insert(0, "")

# ------------------Area for creating window --------------------------------------------START-------------------#
        self.master = tkinter.Tk()
        self.master.title("Payroll Management System")
        self.master.geometry("1800x950+20+20")
        self.master.resizable(False, False)
        self.master.bind("<Destroy>", self.on_close)

# ------------------Area for creating window --------------------------------------------END-----------------------#

# ---------------Create Menu Bar ------------------------------------------------------------START-----------------#

# --------------configuration of menu bar ---------------------------------------------START-----------------------#

        self.bg_menubar = "red"
        self.fg_menubar = "Black"
        self.active_bg_menubar = "#dedede"
        self.active_fg_menubar = "Black"
        self.bg_menus = "#f3f4f5"
        self.fg_menus = "Black"
        self.active_bg_menus = "#bcdff2"
        self.active_fg_menus = "Black"
        self.bg_app = "#1f1f1f"
        self.menubar = tkinter.Menu(self.master,border=5,font=("bookman old style", 15),borderwidth=15,activeborderwidth=0,relief=tkinter.FLAT,
                activeforeground=self.active_fg_menubar,activebackground=self.active_bg_menubar,foreground=self.fg_menubar,background=self.bg_menubar)
        self.master.config(menu=self.menubar)

#--------Staff Menu ----------------------------------------------------------------------------------

        self.Staff_Menu = tkinter.Menu(self.menubar, tearoff=0)
        self.Staff_Menu.Emp_Menu = tkinter.Menu(self.Staff_Menu)
        self.Staff_Menu.add_cascade(menu=self.Staff_Menu.Emp_Menu, label="Employee")

#------------------Employe Sub Menu  ------------------------------------------------------
        self.Staff_Menu.Emp_Menu.add_command(label="Add Employee", command=self.addNewEmployee)
        self.Staff_Menu.Emp_Menu.add_command(label="Update Employee", command=self.updateEmployee)
        self.Staff_Menu.Emp_Menu.add_command(label="Delete Employee", command=self.deleteEmployee)
        self.Staff_Menu.Emp_Menu.add_command(label="List of Employee", command=self.listEmployee)

        self.Staff_Menu.Sal_Menu = tkinter.Menu(self.Staff_Menu)
        self.Staff_Menu.add_cascade(menu=self.Staff_Menu.Sal_Menu, label="Salary")

#-------------------Salary Sub Menu  ------------------------------------------------------
        self.Staff_Menu.Sal_Menu.add_command(label="Create Salary of Employee", command=self.addNewSalary)
        self.Staff_Menu.Sal_Menu.add_command(label="Update Salary of Employee", command=self.updateSalary)
        self.Staff_Menu.Sal_Menu.add_command(label="Delete Salary of Employee", command=self.deleteSalary)
        self.Staff_Menu.Sal_Menu.add_command(label="Salary Details of Employee", command=self.salaryDetails)
        self.Staff_Menu.Sal_Menu.add_command(label="Generate PaySlip for Employee", command=self.generatePayslip)

        self.Staff_Menu.Notif_Menu = tkinter.Menu(self.Staff_Menu)
        self.Staff_Menu.add_cascade(menu=self.Staff_Menu.Notif_Menu, label="Notification")

#-------------------Notificatioin Sub Menu  ------------------------------------------------------
        self.Staff_Menu.Notif_Menu.add_command(label="Create Notification", command=self.createNotification)
        self.Staff_Menu.Notif_Menu.add_command(label="List of Notification", command=self.allNotification)

        self.menubar.add_cascade(label="Staff", menu = self.Staff_Menu)
        self.master.config(menu=self.menubar)

#--------Student Menu -----------------------------------------------------------------------------

        self.Student_Menu = tkinter.Menu(self.menubar, tearoff=0)
        self.Student_Menu.Std_Menu = tkinter.Menu(self.Student_Menu)
        self.Student_Menu.add_cascade(menu=self.Student_Menu.Std_Menu, label="Student")

#-------------------Student Sub Menu  ------------------------------------------------------
        self.Student_Menu.Std_Menu.add_command(label="Add Student", command=self.addNewStudent)
        self.Student_Menu.Std_Menu.add_command(label="Update Student", command=self.updateStudent)
        self.Student_Menu.Std_Menu.add_command(label="Delete Student", command=self.deleteStudent)
        self.Student_Menu.Std_Menu.add_command(label="List of Student", command=self.listStudent)

        self.Student_Menu.Fee_Menu = tkinter.Menu(self.Student_Menu)
        self.Student_Menu.add_cascade(menu=self.Student_Menu.Fee_Menu, label="Fee")

#-------------------Fee Sub Menu  ------------------------------------------------------
        self.Student_Menu.Fee_Menu.add_command(label="Create Fee of Student", command=self.addNewFee)
        self.Student_Menu.Fee_Menu.add_command(label="Update Fee of Student", command=self.updateFee)
        self.Student_Menu.Fee_Menu.add_command(label="Delete Fee of Student", command=self.deleteFee)
        self.Student_Menu.Fee_Menu.add_command(label="Total Fee Collected", command=self.totalFee)

        self.Student_Menu.Message_Menu = tkinter.Menu(self.Student_Menu)
        self.Student_Menu.add_cascade(menu=self.Student_Menu.Message_Menu, label="Message")

#-------------------Message Sub Menu  ------------------------------------------------------
        self.Student_Menu.Message_Menu.add_command(label="Send Message to Whatsapp", command=self.whatsappMessage)
        self.Student_Menu.Message_Menu.add_command(label="Send Message to Phone", command=self.smsMessage)
        self.Student_Menu.Message_Menu.add_command(label="Send Email", command=self.sendMail)
        self.Student_Menu.Message_Menu.add_command(label="Show All Messages", command=self.showAllMessages)

        self.menubar.add_cascade(label="Student", menu = self.Student_Menu)
        self.master.config(menu=self.menubar)

# --------Setting Menu -----------------------------------------------------------------------------

        self.Setting_Menu = tkinter.Menu(self.menubar, tearoff=0)
        self.Setting_Menu.Sub_Setting_Menu = tkinter.Menu(self.Student_Menu)
        self.Setting_Menu.add_cascade(label="Add User", command=self.addNewUser)
        self.Setting_Menu.add_cascade(label="Update User", command=self.updateUser)
        self.menubar.add_cascade(label="Setting", menu=self.Setting_Menu)
        self.master.config(menu=self.menubar)

#--------Logout Menu ----------------------------------------------------------------------------

        self.Logout_Menu = tkinter.Menu(self.menubar, tearoff=0)
        self.Logout_Menu.add_command(label="Logout", command=self.logout)
        self.Logout_Menu.add_command(label="Exit", command=self.master.quit)

        self.menubar.add_cascade(label="Logout", menu = self.Logout_Menu)
        self.master.config(menu=self.menubar)

# ------------------------------------------------------configuration of menu bar --------END--------------------#

# -----------------------------------------------Create Menu Bar -------------------------------END--------------#

# ------------------------------------------Dashboard background ----------------------START---------------------#

# --------------------------------Left Frame ----------------------------------------START ----------------------#

        self.Left_Frame = tkinter.Frame(self.master, bg="Blue", width=400, height=950)
        self.Left_Frame.place(x=0,y=0)

        self.Left_Back_Image = Image.open("icon/forgetpassword.png").resize((250, 250), Image.BOX)
        self.Left_Back_PhotoImage = ImageTk.PhotoImage(self.Left_Back_Image)

        self.Left_Back_Img_label = tkinter.Label(self.Left_Frame, image=self.Left_Back_PhotoImage)
        self.Left_Back_Img_label.place(x=65, y=500)

# Area for user Login Details -----------------------------Start-----------------------------------------------#

        self.userimage = Image.open("icon/payroll.jpg").resize((248, 250), Image.BOX)
        self.userPhotoImage = ImageTk.PhotoImage(self.userimage)

# Area for user Login Details -------------------------------End-----------------------------------------------#

# --------------------------------Left Frame ----------------------------------------END ------------------------#

# --------------------------------RIGHT Frame ----------------------------------------START ---------------------#
        self.Right_Frame = tkinter.Frame(self.master, bg="Red", width=1400, height=950)
        self.Right_Frame.place(x=400, y=0)

        self.Right_Back_Image = Image.open("images/backpayroll.jpg").resize((1400, 950), Image.BOX)
        self.Right_Back_PhotoImage = ImageTk.PhotoImage(self.Right_Back_Image)

        self.Right_Back_Label = tkinter.Label(self.Right_Frame, image=self.Right_Back_PhotoImage)
        self.Right_Back_Label.place(x=0, y=0)

# --------------------------------RIGHT Frame ----------------------------------------END -----------------------#

# Dashboard background image ----------End----------------------------------------------------------------------#

        self.userLogin()
        self.master.mainloop()
#--------------------------------------------- Area for Employee --------------------START----------------------#

    def logout(self):
        self.master.destroy()

        import login
        login.main()

    def userLogin(self):
        currentTime = datetime.datetime.now().strftime('%I:%M %p')

        self.userNameLabel = tkinter.Label(self.Left_Frame, text="" + self.userName.capitalize(),fg="white",font=("bookman old style", 15, "underline"), bg="blue")
        self.userNameLabel.place(x=5, y=800)

        self.userTypeLabel = tkinter.Label(self.Left_Frame, text="User Type: " + self.usertype.capitalize(),fg="white", font=("bookman old style", 15), bg="blue")
        self.userTypeLabel.place(x=5, y=840)

        self.loginTimeLabel = tkinter.Label(self.Left_Frame, text="Login at: " + str(currentTime),fg="white", font=("bookman old style", 15), bg="blue")
        self.loginTimeLabel.place(x=5, y=880)

        # ------------------------On Close -----------------------------------------------
    def on_close(self, event):
        self.master.quit()

    def addNewEmployee(self):

        self.Add_New_Employee = tkinter.Toplevel(self.master)
        self.Add_New_Employee.title("Add New Employee")
        self.Add_New_Employee.geometry("1100x750+420+85")
        self.Add_New_Employee.resizable(False, False)

        self.TitleAddEmployee_Label = tkinter.Label(self.Add_New_Employee, text="Employee Registration:", font=("bookman old style", 20, "underline","bold"))
        self.TitleAddEmployee_Label.place(x=400, y=20)

        self.Employee_No_Label = tkinter.Label(self.Add_New_Employee, text="Employee No: ", font=("bookman old style", 15))
        self.Employee_No_Label.place(x=150, y=90)

# ---------Get New Employee No ---------------------------------------------------START-------------#

        self.Employee_No_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.Employee_No_Entry.place(x=400, y=90)
        self.Employee_No_Entry.insert(0,getIdNumber.getEmpNoinEmployeeTable())
        self.Employee_No_Entry.config(state=tkinter.DISABLED)

# ---------Get New Employee No ---------------------------------------------------END-------------#

        self.Employee_Type_Label = tkinter.Label(self.Add_New_Employee, text="Employee Category: ",font=("bookman old style", 15))
        self.Employee_Type_Label.place(x=150, y=130)


        self.Employee_Type_Entry = tkinter.ttk.Combobox(self.Add_New_Employee, values=["","Admin","Employee","Other Employee"],font=("bookman old style", 15), width=36)
        self.Employee_Type_Entry.place(x=400, y=130)
        self.Employee_Type_Entry.focus_set()
        self.Employee_Type_Entry.bind("<Return>", self.onEnterEmployeeType)

        self.Employee_F_Name_Label = tkinter.Label(self.Add_New_Employee, text="First Name: ", font=("bookman old style", 15))
        self.Employee_F_Name_Label.place(x=150, y=170)

        self.Employee_F_Name_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.Employee_F_Name_Entry.place(x=400, y=170)
        self.Employee_F_Name_Entry.bind("<Return>", self.onEnterEmployeeFirstName)

        self.Employee_L_Name_Label = tkinter.Label(self.Add_New_Employee, text="Last Name: ",font=("bookman old style", 15))
        self.Employee_L_Name_Label.place(x=150, y=210)

        self.Employee_L_Name_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.Employee_L_Name_Entry.place(x=400, y=210)
        self.Employee_L_Name_Entry.bind("<Return>", self.onEnterEmployeeLastName)

        self.Gender_Label = tkinter.Label(self.Add_New_Employee, text="Gender: ", font=("bookman old style", 15))
        self.Gender_Label.place(x=150, y=250)

        self.Gender_Entry = tkinter.ttk.Combobox(self.Add_New_Employee, width=36, values=["","Male","Female","Other"],font=("bookman old style", 15))
        self.Gender_Entry.place(x=400, y=250)
        self.Gender_Entry.bind("<Return>", self.onEnterEmployeeGender)

        self.Phone_No_Label = tkinter.Label(self.Add_New_Employee, text="Phone No: ", font=("bookman old style", 15))
        self.Phone_No_Label.place(x=150, y=290)

        self.Phone_No_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.Phone_No_Entry.place(x=400, y=290)
        self.Phone_No_Entry.bind("<Return>", self.onEnterEmployeePhoneNo)

        self.EmaiId_Label = tkinter.Label(self.Add_New_Employee, text="Email Id: ", font=("bookman old style", 15))
        self.EmaiId_Label.place(x=150, y=330)

        self.EmailID_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.EmailID_Entry.place(x=400, y=330)
        self.EmailID_Entry.bind("<Return>", self.onEnterEmployeeEmail)

        self.Date_of_Joining_Label = tkinter.Label(self.Add_New_Employee, text="Date of Joining: ", font=("bookman old style", 15))
        self.Date_of_Joining_Label.place(x=150, y=370)

        self.Date_of_Joining_Entry = DateEntry(self.Add_New_Employee, selectmode="day", date_pattern="dd/mm/yyyy", sticky="w",font=("bookman old style", 15))
        self.Date_of_Joining_Entry.configure(width=36)
        self.Date_of_Joining_Entry.place(x=400, y=370)
        self.Date_of_Joining_Entry.bind("<Return>", self.onEnterEmployeeDateOfJoining)

        self.Date_of_Leave_Label = tkinter.Label(self.Add_New_Employee, text="Date of Leave: ", font=("bookman old style", 15))
        self.Date_of_Leave_Label.place(x=150, y=410)

        self.Date_of_Leave_Entry = DateEntry(self.Add_New_Employee, selectmode="day", date_pattern="dd/mm/yyyy",sticky="w",font=("bookman old style", 15))
        self.Date_of_Leave_Entry.configure(width=36)
        self.Date_of_Leave_Entry.place(x=400, y=410)
        self.Date_of_Leave_Entry.bind("<Return>", self.onEnterEmployeeDateOfLeave)

        self.Address_Label = tkinter.Label(self.Add_New_Employee, text="Address: ", font=("bookman old style", 15))
        self.Address_Label.place(x=150, y=450)

        self.Address_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.Address_Entry.place(x=400, y=450)
        self.Address_Entry.bind("<Return>", self.onEnterEmployeeAddress)

        self.City_Label = tkinter.Label(self.Add_New_Employee, text="City: ", font=("bookman old style", 15))
        self.City_Label.place(x=150, y=490)

        self.City_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.City_Entry.place(x=400, y=490)
        self.City_Entry.bind("<Return>", self.onEnterEmployeeCity)

        self.State_Label = tkinter.Label(self.Add_New_Employee, text="State: ", font=("bookman old style", 15))
        self.State_Label.place(x=150, y=530)

        self.State_Entry = tkinter.Entry(self.Add_New_Employee, width=38, font=("bookman old style", 15))
        self.State_Entry.place(x=400, y=530)
        self.State_Entry.bind("<Return>", self.onEnterEmployeeState)

        self.Emp_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Emp_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Emp_Cancel_img)

        self.Add_Emp_Cancel_Btn = tkinter.Button(self.Add_New_Employee, text="Cancel", width=225,height=30,font=("bookman old style", 15),
                        command=self.resetAddNewEmployeeForm, bg="#FF7575", fg="white",image=self.Emp_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Add_Emp_Cancel_Btn.place(x=400, y=570)

        self.Emp_Move_Img = Image.open("icon/move1.png").resize((26, 26), Image.BOX)
        self.Emp_Move_Img_PhotoImage = ImageTk.PhotoImage(self.Emp_Move_Img)

        self.Add_Emp_Move_Btn = tkinter.Button(self.Add_New_Employee, text="Move",width=225, height=30,font=("bookman old style", 15), bg="#FFFF99",
                                command=self.savedEmployData, image=self.Emp_Move_Img_PhotoImage, compound=tkinter.RIGHT)
        self.Add_Emp_Move_Btn.place(x=635, y=570)
        self.Add_Emp_Move_Btn.bind("<Return>",self.onEnterEmployeeMoveBtn)

# ----------------Add New Employee Data saved in Database ----------------------------------------------START ------#

    def onEnterEmployeeType(self,event):
        if self.Employee_Type_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field","Please Enter Employee Category")
            self.Employee_Type_Entry.focus_set()
        else:
            self.Employee_F_Name_Entry.focus_set()

    def onEnterEmployeeFirstName(self,event):
        if self.Employee_F_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field","Please Enter Employee First Name")
            self.Employee_F_Name_Entry.focus_set()
        else:
            self.Employee_L_Name_Entry.focus_set()

    def onEnterEmployeeLastName(self,event):
        if self.Employee_L_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field","Please Enter Employee Last Name")
            self.Employee_L_Name_Entry.focus_set()
        else:
            self.Gender_Entry.focus_set()

    def onEnterEmployeeGender(self,event):
        if self.Gender_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field","Please Enter Employee Gender")
            self.Gender_Entry.focus_set()
        else:
            self.Phone_No_Entry.focus_set()

    def onEnterEmployeePhoneNo(self,event):
        if self.Phone_No_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field","Please Enter Employee Phone No")
            self.Phone_No_Entry.focus_set()
        else:
            self.EmailID_Entry.focus_set()

    def onEnterEmployeeEmail(self,event):
        if self.EmailID_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field","Please Enter Employee Email Id")
            self.EmailID_Entry.focus_set()
        else:
            self.Date_of_Joining_Entry.focus_set()

    def onEnterEmployeeDateOfJoining(self,event):
        self.Date_of_Leave_Entry.focus_set()

    def onEnterEmployeeDateOfLeave(self,event):
        self.Address_Entry.focus_set()

    def onEnterEmployeeAddress(self,event):
        if self.Address_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee Address")
            self.Address_Entry.focus_set()
        else:
            self.City_Entry.focus_set()

    def onEnterEmployeeCity(self,event):
        if self.City_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee City")
            self.City_Entry.focus_set()
        else:
            self.State_Entry.focus_set()

    def onEnterEmployeeState(self,event):
        if self.State_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee State")
            self.State_Entry.focus_set()
        else:
            self.Add_Emp_Move_Btn.focus_set()


    def onEnterEmployeeMoveBtn(self,event):
        self.savedEmployData()

    def resetAddNewEmployeeForm(self):
        self.Employee_Type_Entry.current(0)
        self.Employee_F_Name_Entry.delete(0, tkinter.END)
        self.Employee_L_Name_Entry.delete(0, tkinter.END)
        self.Gender_Entry.delete(0, tkinter.END)
        self.Phone_No_Entry.delete(0, tkinter.END)
        self.EmailID_Entry.delete(0, tkinter.END)
        self.Date_of_Joining_Entry.delete(0, tkinter.END)
        self.Date_of_Leave_Entry.delete(0, tkinter.END)
        self.Address_Entry.delete(0, tkinter.END)
        self.City_Entry.delete(0, tkinter.END)
        self.State_Entry.delete(0, tkinter.END)
        self.Employee_No_Entry.focus_set()

    def savedEmployData(self):
        u1 = self.Employee_No_Entry.get().strip()
        u2 = self.Employee_Type_Entry.get().strip()
        u3 = self.Employee_F_Name_Entry.get().strip()
        u4 = self.Employee_L_Name_Entry.get().strip()
        u5 = self.Gender_Entry.get().strip()
        u6 = self.Phone_No_Entry.get().strip()
        u7 = self.EmailID_Entry.get().strip()
        u8 = self.Date_of_Joining_Entry.get().strip()
        u9 = self.Date_of_Leave_Entry.get().strip()
        u10 = self.Address_Entry.get().strip()
        u11 = self.City_Entry.get().strip()
        u12 = self.State_Entry.get().strip()

        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = (f"update employee set emp_type = '{u2}',f_name = '{u3}', l_name = '{u4}',gender = '{u5}', email_id = '{u7}', phone_no = '{u6}',"
                 f" date_of_joining = '{u8}', date_of_leave = '{u9}',address = '{u10}',city = '{u11}',state = '{u12}' where emp_no = '{u1}';")
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.Add_New_Employee.destroy()

        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)

        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)

        finally:
            self.mycursor.close()
            self.myconnect.close()

# -------------------saved data and call open salary form ----------------------------START -------------------#
        self.addNewSalary()
# -------------------saved data and call open salary form ----------------------------END -------------------#

    def updateEmployee(self):
        self.update_Employee_Window = tkinter.Toplevel(self.master)
        self.update_Employee_Window.title("Update . . .")
        self.update_Employee_Window.geometry("800x600+420+85")
        self.update_Employee_Window.resizable(False, False)

        self.Title_Update_Employee_Label = tkinter.Label(self.update_Employee_Window, text="Update Employee Records:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_Update_Employee_Label.place(x=250, y=20)

        self.Search_Update_Employee_Label = tkinter.Label(self.update_Employee_Window, text="Employee ID: ",font=("bookman old style", 15))
        self.Search_Update_Employee_Label.place(x=80, y=60)

        self.Search_Update_Employee_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Search_Update_Employee_Entry.place(x=250, y=60)
        self.Search_Update_Employee_Entry.focus_set()
        self.Search_Update_Employee_Entry.bind("<Return>",self.onEnterSearchEmployeeID)

        self.Update_Employee_F_Name_Label = tkinter.Label(self.update_Employee_Window, text="First Name: ",font=("bookman old style", 15))
        self.Update_Employee_F_Name_Label.place(x=80, y=100)

        self.Update_Employee_F_Name_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Update_Employee_F_Name_Entry.place(x=250, y=100)
        self.Update_Employee_F_Name_Entry.bind("<Return>", self.onEnterUpdateEmployeeFirstName)

        self.Update_Employee_L_Name_Label = tkinter.Label(self.update_Employee_Window, text="Last Name: ",font=("bookman old style", 15))
        self.Update_Employee_L_Name_Label.place(x=80, y=140)

        self.Update_Employee_L_Name_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Update_Employee_L_Name_Entry.place(x=250, y=140)
        self.Update_Employee_L_Name_Entry.bind("<Return>", self.onEnterUpdateEmployeeLastName)

        self.Update_Gender_Label = tkinter.Label(self.update_Employee_Window, text="Gender: ", font=("bookman old style", 15))
        self.Update_Gender_Label.place(x=80, y=180)

        self.Update_Gender_Entry = tkinter.ttk.Combobox(self.update_Employee_Window, width=36,values=["", "Male", "Female", "Other"],font=("bookman old style", 15))
        self.Update_Gender_Entry.place(x=250, y=180)
        self.Update_Gender_Entry.bind("<Return>", self.onEnterUpdateEmployeeGender)

        self.Update_Phone_No_Label = tkinter.Label(self.update_Employee_Window, text="Phone No: ", font=("bookman old style", 15))
        self.Update_Phone_No_Label.place(x=80, y=220)

        self.Update_Phone_No_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Update_Phone_No_Entry.place(x=250, y=220)
        self.Update_Phone_No_Entry.bind("<Return>", self.onEnterUpdateEmployeePhoneNo)

        self.Update_EmaiId_Label = tkinter.Label(self.update_Employee_Window, text="Email Id: ", font=("bookman old style", 15))
        self.Update_EmaiId_Label.place(x=80, y=260)

        self.Update_EmailID_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Update_EmailID_Entry.place(x=250, y=260)
        self.Update_EmailID_Entry.bind("<Return>", self.onEnterUpdateEmployeeEmail)

        self.Update_Date_of_Leave_Label = tkinter.Label(self.update_Employee_Window, text="Date of Leave: ",font=("bookman old style", 15))
        self.Update_Date_of_Leave_Label.place(x=80, y=300)

        self.Update_Date_of_Leave_Entry = DateEntry(self.update_Employee_Window, selectmode="day", date_pattern="dd/mm/yyyy",sticky="w", font=("bookman old style", 15))
        self.Update_Date_of_Leave_Entry.configure(width=36)
        self.Update_Date_of_Leave_Entry.place(x=250, y=300)
        self.Update_Date_of_Leave_Entry.bind("<Return>", self.onEnterUpdateEmployeeDateOfLeave)

        self.Update_Address_Label = tkinter.Label(self.update_Employee_Window, text="Address: ", font=("bookman old style", 15))
        self.Update_Address_Label.place(x=80, y=340)

        self.Update_Address_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Update_Address_Entry.place(x=250, y=340)
        self.Update_Address_Entry.bind("<Return>", self.onEnterUpdateEmployeeAddress)

        self.Update_City_Label = tkinter.Label(self.update_Employee_Window, text="City: ", font=("bookman old style", 15))
        self.Update_City_Label.place(x=80, y=380)

        self.Update_City_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Update_City_Entry.place(x=250, y=380)
        self.Update_City_Entry.bind("<Return>", self.onEnterUpdateEmployeeCity)

        self.Update_State_Label = tkinter.Label(self.update_Employee_Window, text="State: ", font=("bookman old style", 15))
        self.Update_State_Label.place(x=80, y=420)

        self.Update_State_Entry = tkinter.Entry(self.update_Employee_Window, width=38, font=("bookman old style", 15))
        self.Update_State_Entry.place(x=250, y=420)
        self.Update_State_Entry.bind("<Return>", self.onEnterUpdateEmployeeState)

        self.Update_Emp_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Update_Emp_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Update_Emp_Cancel_img)

        self.Update_Emp_Cancel_Btn = tkinter.Button(self.update_Employee_Window, text="Cancel", width=220, height=30,font=("bookman old style", 15),
                                command=self.Update_Emp_Cancel, bg="#FF7575", fg="white",image=self.Update_Emp_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Update_Emp_Cancel_Btn.place(x=250, y=460)

        self.Update_Emp_Move_Img = Image.open("icon/update.jpg").resize((26, 26), Image.BOX)
        self.Update_Emp_Move_Img_PhotoImage = ImageTk.PhotoImage(self.Update_Emp_Move_Img)

        self.Update_Emp_Move_Btn = tkinter.Button(self.update_Employee_Window, text="Update", width=220, height=30,font=("bookman old style", 15), bg="#FFFF99",
                                command=self.updateEmployData, image=self.Update_Emp_Move_Img_PhotoImage,compound=tkinter.RIGHT)
        self.Update_Emp_Move_Btn.place(x=480, y=460)
        self.Update_Emp_Move_Btn.bind("<Return>", self.onEnterUpdateEmployeeMoveBtn)

# ----------------update Employee Data saved in Database ----------------------------------------------START ------#
    def onEnterSearchEmployeeID(self, event):
        self.Update_Emp_Cancel()
        eid = self.Search_Update_Employee_Entry.get()

        if eid == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee ID")
            self.Search_Update_Employee_Entry.focus_set()
        else:
            try:
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"SELECT * FROM employee where emp_no = '{eid}';"
                self.mycursor.execute(q)
                row = self.mycursor.fetchall()

                if row == None:
                    tkinter.messagebox.showerror("Error", "Invalid details")
                    self.Search_Update_Employee_Entry.focus_set()
                elif len(row) == 0:
                    tkinter.messagebox.showerror("Error", "No Record Found")
                    self.Search_Update_Employee_Entry.focus_set()

                else:
                    for count in range(1):
                        name = row[count]
                        self.Update_Employee_F_Name_Entry.insert(0,name[3])
                        self.Update_Employee_L_Name_Entry.insert(0,name[4])
                        self.Update_Gender_Entry.insert(0,name[5])
                        self.Update_Phone_No_Entry.insert(0,name[7])
                        self.Update_EmailID_Entry.insert(0,name[6])
                        self.Update_Date_of_Leave_Entry.insert(0,name[9])
                        self.Update_Address_Entry.insert(0,name[10])
                        self.Update_City_Entry.insert(0,name[11])
                        self.Update_State_Entry.insert(0,name[12])

            except Exception as ee:
                print(str(ee))

            finally:
                self.mycursor.close()
                self.myconnect.close()

            self.Update_Employee_F_Name_Entry.focus_set()

    def onEnterUpdateEmployeeFirstName(self, event):
        if self.Update_Employee_F_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee First Name")
            self.Update_Employee_F_Name_Entry.focus_set()
        else:
            self.Update_Employee_L_Name_Entry.focus_set()

    def onEnterUpdateEmployeeLastName(self, event):
        if self.Update_Employee_L_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee Last Name")
            self.Update_Employee_L_Name_Entry.focus_set()
        else:
            self.Update_Gender_Entry.focus_set()

    def onEnterUpdateEmployeeGender(self, event):
        if self.Update_Gender_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee Gender")
            self.Update_Gender_Entry.focus_set()
        else:
            self.Update_Phone_No_Entry.focus_set()

    def onEnterUpdateEmployeePhoneNo(self, event):
        if self.Update_Phone_No_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee Phone No")
            self.Update_Phone_No_Entry.focus_set()
        else:
            self.Update_EmailID_Entry.focus_set()

    def onEnterUpdateEmployeeEmail(self, event):
        if self.Update_EmailID_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee Email Id")
            self.Update_EmailID_Entry.focus_set()
        else:
            self.Update_Date_of_Leave_Entry.focus_set()

    def onEnterUpdateEmployeeDateOfLeave(self, event):
        self.Update_Address_Entry.focus_set()

    def onEnterUpdateEmployeeAddress(self, event):
        if self.Update_Address_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee Address")
            self.Update_Address_Entry.focus_set()
        else:
            self.Update_City_Entry.focus_set()

    def onEnterUpdateEmployeeCity(self, event):
        if self.Update_City_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee City")
            self.Update_City_Entry.focus_set()
        else:
            self.Update_State_Entry.focus_set()

    def onEnterUpdateEmployeeState(self, event):
        if self.Update_State_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee State")
            self.Update_State_Entry.focus_set()
        else:
            self.Update_Emp_Move_Btn.focus_set()

    def onEnterUpdateEmployeeMoveBtn(self, event):
        self.updateEmployData()

    def Update_Emp_Cancel(self):
        self.Update_Employee_F_Name_Entry.delete(0,tkinter.END)
        self.Update_Employee_L_Name_Entry.delete(0,tkinter.END)
        self.Update_Gender_Entry.delete(0,tkinter.END)
        self.Update_Phone_No_Entry.delete(0,tkinter.END)
        self.Update_EmailID_Entry.delete(0,tkinter.END)
        self.Update_Date_of_Leave_Entry.delete(0,tkinter.END)
        self.Update_Address_Entry.delete(0,tkinter.END)
        self.Update_City_Entry.delete(0,tkinter.END)
        self.Update_State_Entry.delete(0,tkinter.END)
        self.Update_Employee_F_Name_Entry.focus_set()

    def updateEmployData(self):
        u1 = self.Search_Update_Employee_Entry.get().strip()
        u2 = self.Update_Employee_F_Name_Entry.get().strip()
        u3 = self.Update_Employee_L_Name_Entry.get().strip()
        u4 = self.Update_Gender_Entry.get().strip()
        u5 = self.Update_Phone_No_Entry.get().strip()
        u6 = self.Update_EmailID_Entry.get().strip()
        u7 = self.Update_Date_of_Leave_Entry.get().strip()
        u8 = self.Update_Address_Entry.get().strip()
        u9 = self.Update_City_Entry.get().strip()
        u10 = self.Update_State_Entry.get().strip()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = (f"update employee set f_name = '{u2}', l_name = '{u3}',gender = '{u4}', email_id = '{u6}', phone_no = '{u5}',"
                f" date_of_leave = '{u7}',address = '{u8}',city = '{u9}',state = '{u10}' where emp_no = '{u1}';")
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.update_Employee_Window.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

#--------------------------------------Update Employee record -----------------------------END -------------------#

# --------------------------------------Delete Employee record -----------------------------START -------------------#
    def deleteEmployee(self):
        self.Find_Employee_Window = tkinter.Toplevel(self.master)
        self.Find_Employee_Window.title("Find Employee")
        self.Find_Employee_Window.geometry("600x260+420+85")
        self.Find_Employee_Window.resizable(False, False)

        self.Title_Find_Employee_Label = tkinter.Label(self.Find_Employee_Window, text="_____Find Details____",font=("bookman old style", 20, "bold"))
        self.Title_Find_Employee_Label.place(x=130, y=20)

        self.Employee_Find_Frame = tkinter.LabelFrame(self.Find_Employee_Window, bg="#EDF5F4")
        self.Employee_Find_Frame.place(x=20, y=70, height=160, width=550)

        self.Employee_ID_Label = tkinter.Label(self.Employee_Find_Frame, text="Employee ID: ", font=("bookman old style", 15))
        self.Employee_ID_Label.place(x=20, y=20)

        self.Employee_ID_Entry = tkinter.Entry(self.Employee_Find_Frame, width=26, font=("bookman old style", 15))
        self.Employee_ID_Entry.place(x=180, y=20)
        self.Employee_ID_Entry.focus_set()
        self.Employee_ID_Entry.bind("<Return>",self.onEnterEmployeeIDEntry)

        self.Employee_Find_Cancel_Img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Employee_Find_Cancel_PhotoImage = ImageTk.PhotoImage(self.Employee_Find_Cancel_Img)

        self.Employee_Find_Cancel_Btn = tkinter.Button(self.Employee_Find_Frame, text="Cancel", width=148, height=30,font=("bookman old style", 15),
                                                image=self.Employee_Find_Cancel_PhotoImage, compound=tkinter.LEFT)
        self.Employee_Find_Cancel_Btn.place(x=180, y=60)
        self.Employee_Find_Cancel_Btn.bind("<Return>", self.resetEmployeeFindBtn)

        self.Employee_Find_Img = Image.open("icon/find2.jpg").resize((26, 26), Image.BOX)
        self.Employee_Find_PhotoImage = ImageTk.PhotoImage(self.Employee_Find_Img)

        self.Employee_Find_Btn = tkinter.Button(self.Employee_Find_Frame, text="Find", width=148, height=30,font=("bookman old style", 15), command=self.empFind,
                                       image=self.Employee_Find_PhotoImage, compound=tkinter.LEFT)
        self.Employee_Find_Btn.place(x=335, y=60)
        self.Employee_Find_Btn.bind("<Return>",self.onEnterEmployeeFindBTN)

        self.Employee_Delete_Img = Image.open("icon/delete.jpg").resize((30, 30), Image.BOX)
        self.Employee_Delete_PhotoImage = ImageTk.PhotoImage(self.Employee_Delete_Img)

        self.Employee_Delete_Btn = tkinter.Button(self.Employee_Find_Frame, text="Delete", width=301, height=30,font=("bookman old style", 15), command=self.empDelete,
                                                image=self.Employee_Delete_PhotoImage, compound=tkinter.LEFT)
        self.Employee_Delete_Btn.place(x=180, y=100)
        self.Employee_Delete_Btn.bind("<Return>", self.onEnterEmployeeDeleteBtn)

# ------------------------Find Form Function ----------------------------------END-------------------------------#

# ----------- all functions ------------------------
    def onEnterEmployeeIDEntry(self, event):
        if self.Employee_ID_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee ID")
            self.Employee_ID_Entry.focus_set()
        else:
            self.Employee_Find_Btn.focus_set()

    def resetEmployeeFindBtn(self, event):
        self.Employee_ID_Entry.delete(0, tkinter.END)
        self.Employee_ID_Entry.focus_set()

    def onEnterEmployeeFindBTN(self, event):
        self.empFind()

    def onEnterEmployeeDeleteBtn(self,event):
        self.empDelete()

    def empFind(self):
        empid = self.Employee_ID_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM employee where emp_no = '{empid}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
                self.Employee_ID_Entry.focus_set()
            elif len(row) == 0:
                tkinter.messagebox.showerror("Error", "Record Not Found")
                self.Employee_ID_Entry.focus_set()
            else:
                tkinter.messagebox.showinfo("Success", "Record Found")
                self.Employee_Delete_Btn.focus_set()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def empDelete(self):
        empid = self.Employee_ID_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = (f"update employee set emp_type = NULL, f_name = NULL, l_name = NULL,gender = NULL, email_id = NULL, phone_no = NULL,"
                f"date_of_joining = NULL,date_of_leave = NULL,address = NULL,city = NULL,state = NULL where emp_no = '{empid}';")
            self.mycursor.execute(q)
            self.myconnect.commit()

            q = f"update salary set ta = NULL, hra = NULL,da = NULL,med = NULL,pf = NULL,basic_salary = NULL, total_sal = NULL where emp_no = '{empid}';"
            self.mycursor.execute(q)
            self.myconnect.commit()

            tkinter.messagebox.showinfo("Success", "Delete successfully")
            self.Find_Employee_Window.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def listEmployee(self):

# ---------------List of all Employye in the Staff -----------------------------------START-------------------#

        self.Employee_All_List_Window = tkinter.Toplevel(self.master)
        self.Employee_All_List_Window.title("List of all Employees . . .")
        self.Employee_All_List_Window.geometry("1200x800+120+85")
        self.Employee_All_List_Window.resizable(False, False)

        self.Title_Employee_All_List_Label = tkinter.Label(self.Employee_All_List_Window,text="List of all Staff:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_Employee_All_List_Label.place(x=400, y=20)

        self.Employee_All_List_TextArea = tkinter.Text(self.Employee_All_List_Window, width=95, height=30,font=("bookman old style", 15))
        self.Employee_All_List_TextArea.place(x=25, y=70)

        try:
            self.itemlist.clear()
            self.Employee_All_List_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 3
            s3 = " " * 5
            s4 = " " * 9
            s5 = " " * 11
            s6 = " " * 13
            ItemHead = f"Sno.{s2}Employee Id{s4}Employee Type{s3}Name\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = "SELECT * FROM employee;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    if name[3] == None:
                        data = (f"{s1}\nTotal Employees registered -> {count}\n{s1}")
                        self.itemlist.append(data)
                        break
                    else:
                        data = (f"{name[0]}.{s4}{name[1]}{s5}{name[2]}{s6}{name[3]} {name[4]}\n")
                        self.itemlist.append(data)
                for item in self.itemlist:
                    self.Employee_All_List_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

# -----------------List of all Employee in the Staff--------------------------------END-------------------#

# ----------------------------------------------- Area for Employee -----------------------END----------------------#

# ------------------------- Area for Salary Structure for Employee ----------------------START----------------------#
    def addNewSalary(self):
        self.Add_New_Salary = tkinter.Toplevel(self.master)
        self.Add_New_Salary.title("Register Salary")
        self.Add_New_Salary.geometry("950x500+420+85")
        self.Add_New_Salary.resizable(False, False)

        self.Title_Salary_Label = tkinter.Label(self.Add_New_Salary, text="Salary Form:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_Salary_Label.place(x=400, y=20)

        self.EmpNo_Label = tkinter.Label(self.Add_New_Salary, text="Employee No: ",font=("bookman old style", 15))
        self.EmpNo_Label.place(x=110, y=90)

# ---------Get New Employee No ---------------------------------------------------START-------------#

        self.EmpNo_Entry = tkinter.Entry(self.Add_New_Salary, width=27, font=("bookman old style", 15))
        self.EmpNo_Entry.place(x=500, y=90)
        self.EmpNo_Entry.insert(0,getIdNumber.getEmpNoinSalaryTable())
        self.EmpNo_Entry.config(state=tkinter.DISABLED)

# ---------Get New Employee No ---------------------------------------------------END-------------#

        self.TA_Label = tkinter.Label(self.Add_New_Salary, text="Travel Allowance (TA): ",font=("bookman old style", 15))
        self.TA_Label.place(x=110, y=130)

        self.TA_Entry = tkinter.Entry(self.Add_New_Salary, width=27, font=("bookman old style", 15))
        self.TA_Entry.place(x=500, y=130)
        self.TA_Entry.focus_set()
        self.TA_Entry.bind("<Return>", self.onEnterTAEntry)

        self.DA_Label = tkinter.Label(self.Add_New_Salary, text="Dearness Allowance (DA): ",font=("bookman old style", 15))
        self.DA_Label.place(x=110, y=170)

        self.DA_Entry = tkinter.Entry(self.Add_New_Salary, width=27,font=("bookman old style", 15))
        self.DA_Entry.place(x=500, y=170)
        self.DA_Entry.bind("<Return>", self.onEnterDAEntry)

        self.HRA_Label = tkinter.Label(self.Add_New_Salary, text="House Rent Allowance (HRA): ",font=("bookman old style", 15))
        self.HRA_Label.place(x=110, y=210)

        self.HRA_Entry = tkinter.Entry(self.Add_New_Salary, width=27, font=("bookman old style", 15))
        self.HRA_Entry.place(x=500, y=210)
        self.HRA_Entry.bind("<Return>", self.onEnterHRAEntry)

        self.MED_Label = tkinter.Label(self.Add_New_Salary, text="Medical Allowance (MED): ",font=("bookman old style", 15))
        self.MED_Label.place(x=110, y=250)

        self.MED_Entry = tkinter.Entry(self.Add_New_Salary, width=27, font=("bookman old style", 15))
        self.MED_Entry.place(x=500, y=250)
        self.MED_Entry.bind("<Return>", self.onEnterMEDEntry)

        self.PF_Label = tkinter.Label(self.Add_New_Salary, text="Provident Fund (PF): ", font=("bookman old style", 15))
        self.PF_Label.place(x=110, y=290)

        self.PF_Entry = tkinter.Entry(self.Add_New_Salary, width=27,font=("bookman old style", 15))
        self.PF_Entry.place(x=500, y=290)
        self.PF_Entry.bind("<Return>", self.onEnterPFEntry)

        self.Basic_Salary_Label = tkinter.Label(self.Add_New_Salary, text="Basic Salary: ", font=("bookman old style", 15))
        self.Basic_Salary_Label.place(x=110, y=330)

        self.Basic_Salary_Entry = tkinter.Entry(self.Add_New_Salary, width=27, font=("bookman old style", 15))
        self.Basic_Salary_Entry.place(x=500, y=330)
        self.Basic_Salary_Entry.bind("<Return>", self.onEnterBasicSalaryEntry)

        self.Total_Salary_Label = tkinter.Label(self.Add_New_Salary, text="Total Salary: ", font=("bookman old style", 15))
        self.Total_Salary_Label.place(x=110, y=370)

        self.Total_Salary_Entry = tkinter.Entry(self.Add_New_Salary, width=27, font=("bookman old style", 15))
        self.Total_Salary_Entry.place(x=500, y=370)
        self.Total_Salary_Entry.bind("<Return>", self.onEnterTotalSalaryEntry)

        self.Emp_Sal_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Emp_Sal_Cancel_PhotoImg = ImageTk.PhotoImage(self.Emp_Sal_Cancel_img)

        self.Salary_Cancel_Btn = tkinter.Button(self.Add_New_Salary, text="Cancel", width=152, height=30,font=("bookman old style", 15),command=self.resetNewSalaryForm, bg="#FF7575", fg="white",
                        image=self.Emp_Sal_Cancel_PhotoImg, compound=tkinter.RIGHT)
        self.Salary_Cancel_Btn.place(x=500, y=410)

        self.Emp_Sal_Submit_img = Image.open("icon/save1.png").resize((26, 26), Image.BOX)
        self.Emp_Sal_Submit_PhotoImage = ImageTk.PhotoImage(self.Emp_Sal_Submit_img)

        self.Salary_Submit_Btn = tkinter.Button(self.Add_New_Salary, text="Submit", width=152, height=30, bg="#ceffcf",font=("bookman old style", 15), command=self.submitEmployeeAllData,
                                        image=self.Emp_Sal_Submit_PhotoImage, compound=tkinter.RIGHT)
        self.Salary_Submit_Btn.place(x=663, y=410)

# ----------------Add Salary for New Employee Data saved in Database ----------------------------------------------START ------#

    def onEnterTAEntry(self, event):
        try:
            if self.TA_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter TA")
                self.TA_Entry.focus_set()
            elif int(self.TA_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.TA_Entry.focus_set()
            else:
                self.DA_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error","Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error",str(e))
    def onEnterDAEntry(self, event):
        try:
            if self.DA_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter DA")
                self.DA_Entry.focus_set()
            elif int(self.DA_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.DA_Entry.focus_set()
            else:
                self.HRA_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterHRAEntry(self, event):
        try:
            if self.HRA_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter HRA")
                self.HRA_Entry.focus_set()
            elif int(self.HRA_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.HRA_Entry.focus_set()
            else:
                self.MED_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterMEDEntry(self, event):
        try:
            if self.MED_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter MED")
                self.MED_Entry.focus_set()
            elif int(self.MED_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.MED_Entry.focus_set()
            else:
                self.PF_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterPFEntry(self, event):
        try:
            if self.PF_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter PF")
                self.PF_Entry.focus_set()
            elif int(self.PF_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.PF_Entry.focus_set()
            else:
                self.Basic_Salary_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))
    def onEnterBasicSalaryEntry(self, event):
        try:
            if self.Basic_Salary_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Basic Salary")
                self.Basic_Salary_Entry.focus_set()
            elif int(self.Basic_Salary_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Basic_Salary_Entry.focus_set()
            else:
                ta = int(self.TA_Entry.get())
                da = int(self.DA_Entry.get())
                hra = int(self.HRA_Entry.get())
                medical = int(self.MED_Entry.get())
                PPF = int(self.PF_Entry.get())
                BS = int(self.Basic_Salary_Entry.get())
 
                total_allow = ta + da + hra + medical
                GS = total_allow + BS
                PT = math.floor(0.03 * BS)
                HEALTHINS = math.floor(0.05 * BS)
                TDS = math.floor(0.1 * BS)
                Other_Deduction = math.floor(0.01 * BS)
                total_Deduction = PPF + PT + HEALTHINS + TDS + Other_Deduction
                sum = GS - total_Deduction
                self.Total_Salary_Entry.insert(0, str(sum))
                self.Total_Salary_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterTotalSalaryEntry(self, event):
        try:
            if self.Total_Salary_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Total Salary")
                self.Total_Salary_Entry.focus_set()
            elif int(self.Total_Salary_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Total_Salary_Entry.focus_set()
            else:
                self.Salary_Submit_Btn.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def resetNewSalaryForm(self):
        self.TA_Entry.delete(0, tkinter.END)
        self.DA_Entry.delete(0, tkinter.END)
        self.HRA_Entry.delete(0, tkinter.END)
        self.MED_Entry.delete(0, tkinter.END)
        self.PF_Entry.delete(0, tkinter.END)
        self.Basic_Salary_Entry.delete(0, tkinter.END)
        self.Total_Salary_Entry.delete(0, tkinter.END)
        self.TA_Entry.focus_set()

    def submitEmployeeAllData(self):
        u1 = int(self.TA_Entry.get())
        u2 = int(self.DA_Entry.get())
        u3 = int(self.HRA_Entry.get())
        u4 = int(self.MED_Entry.get())
        u5 = int(self.PF_Entry.get())
        u6 = int(self.Basic_Salary_Entry.get())
        u7 = int(self.Total_Salary_Entry.get())
        u9 = self.EmpNo_Entry.get()

        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"update salary set ta = '{u1}', hra = '{u3}',da = '{u2}',med = '{u4}',pf = '{u5}',basic_salary = '{u6}', total_sal = '{u7}' where emp_no = '{u9}';"
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.Add_New_Salary.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        finally:
            self.mycursor.close()
            self.myconnect.close()

# -------------------saved data  ------------------------------------------------END ----------------------#

    def updateSalary(self):
        self.update_Salary_window = tkinter.Toplevel(self.master)
        self.update_Salary_window.title("Update Salary")
        self.update_Salary_window.geometry("950x500+420+85")
        self.update_Salary_window.resizable(False, False)

        self.Title_Update_Salary_Label = tkinter.Label(self.update_Salary_window, text="Update Salary Form:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Update_Salary_Label.place(x=400, y=20)

        self.Update_Salary_EmpNo_Label = tkinter.Label(self.update_Salary_window, text="Employee No: ", font=("bookman old style", 15))
        self.Update_Salary_EmpNo_Label.place(x=110, y=90)

        self.Update_Salary_EmpNo_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_Salary_EmpNo_Entry.place(x=500, y=90)
        self.Update_Salary_EmpNo_Entry.focus_set()
        self.Update_Salary_EmpNo_Entry.bind("<Return>", self.onEnterSearchUpdateSalaryEmployeeID)

        self.Update_TA_Label = tkinter.Label(self.update_Salary_window, text="Travel Allowance (TA): ",font=("bookman old style", 15))
        self.Update_TA_Label.place(x=110, y=130)

        self.Update_TA_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_TA_Entry.place(x=500, y=130)
        self.Update_TA_Entry.bind("<Return>", self.onEnterUpdateTAEntry)

        self.Update_DA_Label = tkinter.Label(self.update_Salary_window, text="Dearness Allowance (DA): ",font=("bookman old style", 15))
        self.Update_DA_Label.place(x=110, y=170)

        self.Update_DA_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_DA_Entry.place(x=500, y=170)
        self.Update_DA_Entry.bind("<Return>", self.onEnterUpdateDAEntry)

        self.Update_HRA_Label = tkinter.Label(self.update_Salary_window, text="House Rent Allowance (HRA): ", font=("bookman old style", 15))
        self.Update_HRA_Label.place(x=110, y=210)

        self.Update_HRA_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_HRA_Entry.place(x=500, y=210)
        self.Update_HRA_Entry.bind("<Return>", self.onEnterUpdateHRAEntry)

        self.Update_MED_Label = tkinter.Label(self.update_Salary_window, text="Medical Allowance (MED): ",font=("bookman old style", 15))
        self.Update_MED_Label.place(x=110, y=250)

        self.Update_MED_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_MED_Entry.place(x=500, y=250)
        self.Update_MED_Entry.bind("<Return>", self.onEnterUpdateMEDEntry)

        self.Update_PF_Label = tkinter.Label(self.update_Salary_window, text="Provident Fund (PF): ", font=("bookman old style", 15))
        self.Update_PF_Label.place(x=110, y=290)

        self.Update_PF_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_PF_Entry.place(x=500, y=290)
        self.Update_PF_Entry.bind("<Return>", self.onEnterUpdatePFEntry)

        self.Update_Basic_Salary_Label = tkinter.Label(self.update_Salary_window, text="Basic Salary: ", font=("bookman old style", 15))
        self.Update_Basic_Salary_Label.place(x=110, y=330)

        self.Update_Basic_Salary_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_Basic_Salary_Entry.place(x=500, y=330)
        self.Update_Basic_Salary_Entry.bind("<Return>", self.onEnterUpdateBasicSalaryEntry)

        self.Update_Total_Salary_Label = tkinter.Label(self.update_Salary_window, text="Total Salary: ",font=("bookman old style", 15))
        self.Update_Total_Salary_Label.place(x=110, y=370)

        self.Update_Total_Salary_Entry = tkinter.Entry(self.update_Salary_window, width=27, font=("bookman old style", 15))
        self.Update_Total_Salary_Entry.place(x=500, y=370)
        self.Update_Total_Salary_Entry.bind("<Return>", self.onEnterUpdateTotalSalaryEntry)

        self.Update_Emp_Sal_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Update_Emp_Sal_Cancel_PhotoImg= ImageTk.PhotoImage(self.Update_Emp_Sal_Cancel_img)

        self.Update_Salary_Cancel_Btn = tkinter.Button(self.update_Salary_window, text="Cancel", width=152, height=30,font=("bookman old style", 15), command=self.resetUpdateSalaryForm,
                                    bg="#FF7575", fg="white",image=self.Update_Emp_Sal_Cancel_PhotoImg, compound=tkinter.RIGHT)
        self.Update_Salary_Cancel_Btn.place(x=500, y=410)

        self.Update_Salary_Submit_img = Image.open("icon/save1.png").resize((26, 26), Image.BOX)
        self.Update_Salary_Submit_PhotoImg = ImageTk.PhotoImage(self.Update_Salary_Submit_img)

        self.Update_Salary_Submit_Btn = tkinter.Button(self.update_Salary_window, text="Submit", width=152, height=30, bg="#ceffcf",
                                    font=("bookman old style", 15), command=self.UpdateSalaryAllData,image=self.Update_Salary_Submit_PhotoImg, compound=tkinter.RIGHT)
        self.Update_Salary_Submit_Btn.place(x=663, y=410)

        # ----------------Add Salary for New Employee Data saved in Database ----------------------------------------------START ------#

    def onEnterSearchUpdateSalaryEmployeeID(self, event):
        self.resetUpdateSalaryForm()
        eid = self.Update_Salary_EmpNo_Entry.get()
        if eid == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee ID")
            self.Update_Salary_EmpNo_Entry.focus_set()
        else:
            try:
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"SELECT * FROM salary where emp_no = '{eid}';"
                self.mycursor.execute(q)
                row = self.mycursor.fetchall()
                if row == None:
                    tkinter.messagebox.showerror("Error", "Invalid details")
                    self.Update_Salary_EmpNo_Entry.focus_set()
                elif len(row) == 0:
                    tkinter.messagebox.showerror("Error", "No Record Found")
                    self.Update_Salary_EmpNo_Entry.focus_set()
                else:
                    for count in range(1):
                        name = row[count]
                        self.Update_TA_Entry.insert(0, name[2])
                        self.Update_DA_Entry.insert(0, name[4])
                        self.Update_HRA_Entry.insert(0, name[3])
                        self.Update_MED_Entry.insert(0, name[5])
                        self.Update_PF_Entry.insert(0, name[6])
                        self.Update_Basic_Salary_Entry.insert(0, name[7])
            except Exception as ee:
                print(str(ee))
            finally:
                self.mycursor.close()
                self.myconnect.close()
            self.Update_TA_Entry.focus_set()

    def onEnterUpdateTAEntry(self, event):
        try:
            if self.Update_TA_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter TA")
                self.Update_TA_Entry.focus_set()
            elif int(self.Update_TA_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_TA_Entry.focus_set()
            else:
                self.Update_DA_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateDAEntry(self, event):
        try:
            if self.Update_DA_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter DA")
                self.Update_DA_Entry.focus_set()
            elif int(self.Update_DA_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_DA_Entry.focus_set()
            else:
                self.Update_HRA_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateHRAEntry(self, event):
        try:
            if self.Update_HRA_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter HRA")
                self.Update_HRA_Entry.focus_set()
            elif int(self.Update_HRA_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_HRA_Entry.focus_set()
            else:
                self.Update_MED_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateMEDEntry(self, event):
        try:
            if self.Update_MED_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter MED")
                self.Update_MED_Entry.focus_set()
            elif int(self.Update_MED_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_MED_Entry.focus_set()
            else:
                self.Update_PF_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdatePFEntry(self, event):
        try:
            if self.Update_PF_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter PF")
                self.Update_PF_Entry.focus_set()
            elif int(self.Update_PF_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_PF_Entry.focus_set()
            else:
                self.Update_Basic_Salary_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateBasicSalaryEntry(self, event):
        try:
            if self.Update_Basic_Salary_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Basic Salary")
                self.Update_Basic_Salary_Entry.focus_set()
            elif int(self.Update_Basic_Salary_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Basic_Salary_Entry.focus_set()
            else:
                ta = int(self.Update_TA_Entry.get())
                da = int(self.Update_DA_Entry.get())
                hra = int(self.Update_HRA_Entry.get())
                medical = int(self.Update_MED_Entry.get())
                PPF = int(self.Update_PF_Entry.get())
                BS = int(self.Update_Basic_Salary_Entry.get())
                
                total_allow = ta + da + hra + medical
                GS = total_allow + BS
                PT = math.floor(0.03 * BS)
                HEALTHINS = math.floor(0.05 * BS)
                TDS = math.floor(0.1 * BS)
                Other_Deduction = math.floor(0.01 * BS)
                total_Deduction = PPF + PT + HEALTHINS + TDS + Other_Deduction
                sum = GS - total_Deduction

                self.Update_Total_Salary_Entry.delete(0,tkinter.END)
                self.Update_Total_Salary_Entry.insert(0, str(sum))
                self.Update_Total_Salary_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")

        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateTotalSalaryEntry(self, event):
        try:
            if self.Update_Total_Salary_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Total Salary")
                self.Update_Total_Salary_Entry.focus_set()
            elif int(self.Update_Total_Salary_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Total_Salary_Entry.focus_set()
            else:
                self.Update_Salary_Submit_Btn.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def resetUpdateSalaryForm(self):
        self.Update_TA_Entry.delete(0, tkinter.END)
        self.Update_DA_Entry.delete(0, tkinter.END)
        self.Update_HRA_Entry.delete(0, tkinter.END)
        self.Update_MED_Entry.delete(0, tkinter.END)
        self.Update_PF_Entry.delete(0, tkinter.END)
        self.Update_Basic_Salary_Entry.delete(0, tkinter.END)
        self.Update_Total_Salary_Entry.delete(0, tkinter.END)
        self.Update_TA_Entry.focus_set()

    def UpdateSalaryAllData(self):

        u1 = int(self.Update_TA_Entry.get())
        u2 = int(self.Update_DA_Entry.get())
        u3 = int(self.Update_HRA_Entry.get())
        u4 = int(self.Update_MED_Entry.get())
        u5 = int(self.Update_PF_Entry.get())
        u6 = int(self.Update_Basic_Salary_Entry.get())
        u7 = int(self.Update_Total_Salary_Entry.get())
        u8 = self.Update_Salary_EmpNo_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"update salary set ta = '{u1}', hra = '{u3}',da = '{u2}',med = '{u4}',pf = '{u5}',basic_salary = '{u6}', total_sal = '{u7}' where emp_no = '{u8}';"
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.update_Salary_window.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        finally:
            self.mycursor.close()
            self.myconnect.close()

# --------------------------------------Update Employee Salary record -----------------------------END -------------------#

    def deleteSalary(self):
        self.Find_Delete_salary_Window = tkinter.Toplevel(self.master)
        self.Find_Delete_salary_Window.title("Find Employee")
        self.Find_Delete_salary_Window.geometry("600x260+420+85")
        self.Find_Delete_salary_Window.resizable(False, False)

        self.Title_Find_Salary_Label = tkinter.Label(self.Find_Delete_salary_Window, text="_____Find Details____", font=("bookman old style", 20, "bold"))
        self.Title_Find_Salary_Label.place(x=130, y=20)

        self.Delete_Salary_Find_Frame = tkinter.LabelFrame(self.Find_Delete_salary_Window, bg="#EDF5F4")
        self.Delete_Salary_Find_Frame.place(x=20, y=70, height=160, width=550)

        self.Delete_Salary_Employee_ID_Label = tkinter.Label(self.Delete_Salary_Find_Frame, text="Employee ID: ", font=("bookman old style", 15))
        self.Delete_Salary_Employee_ID_Label.place(x=20, y=20)

        self.Delete_Salary_Employee_ID_Entry = tkinter.Entry(self.Delete_Salary_Find_Frame, width=26, font=("bookman old style", 15))
        self.Delete_Salary_Employee_ID_Entry.place(x=180, y=20)
        self.Delete_Salary_Employee_ID_Entry.focus_set()
        self.Delete_Salary_Employee_ID_Entry.bind("<Return>", self.onEnterDeleteSalaryEmployeeIDEntry)

        self.Delete_Salary_Employee_Find_Cancel_Img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Delete_Salary_Employee_Find_Cancel_PhotoImage = ImageTk.PhotoImage(self.Delete_Salary_Employee_Find_Cancel_Img)

        self.Delete_Salary_Employee_Find_Cancel_Btn = tkinter.Button(self.Delete_Salary_Find_Frame, text="Cancel", width=148, height=30, font=("bookman old style", 15), command=self.restDeleteSalayBTN,
                                    image=self.Delete_Salary_Employee_Find_Cancel_PhotoImage,compound=tkinter.LEFT)
        self.Delete_Salary_Employee_Find_Cancel_Btn.place(x=180, y=60)
        self.Delete_Salary_Employee_Find_Cancel_Btn.bind("<Return>", self.resetDeleteSalaryEmployeeFindBtn)

        self.Delete_Salary_Employee_Find_Img = Image.open("icon/find2.jpg").resize((26, 26), Image.BOX)
        self.Delete_Salary_Employee_Find_PhotoImage = ImageTk.PhotoImage(self.Delete_Salary_Employee_Find_Img)

        self.Delete_Salary_Employee_Find_Btn = tkinter.Button(self.Delete_Salary_Find_Frame, text="Find", width=148, height=30,font=("bookman old style", 15), command=self.empSalFind,
                                                image=self.Delete_Salary_Employee_Find_PhotoImage, compound=tkinter.LEFT)
        self.Delete_Salary_Employee_Find_Btn.place(x=335, y=60)
        self.Delete_Salary_Employee_Find_Btn.bind("<Return>", self.onEnterDeleteSalaryEmployeeFindBTN)

        self.Delete_Salary_Employee_Delete_Img = Image.open("icon/delete.jpg").resize((30, 30), Image.BOX)
        self.Delete_Salary_Employee_Delete_PhotoImage = ImageTk.PhotoImage(self.Delete_Salary_Employee_Delete_Img)

        self.Delete_Salary_Employee_Delete_Btn = tkinter.Button(self.Delete_Salary_Find_Frame, text="Delete", width=301, height=30, font=("bookman old style", 15), command=self.empSalaryDelete,
                                                  image=self.Delete_Salary_Employee_Delete_PhotoImage, compound=tkinter.LEFT)
        self.Delete_Salary_Employee_Delete_Btn.place(x=180, y=100)
        self.Delete_Salary_Employee_Delete_Btn.bind("<Return>", self.onEnterSalaryEmployeeDeleteBtn)

        # ------------------------Find Form Function ----------------------------------END-------------------------------#

        # ----------- all functions ------------------------
    def onEnterDeleteSalaryEmployeeIDEntry(self, event):
        if self.Delete_Salary_Employee_ID_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee ID")
            self.Delete_Salary_Employee_ID_Entry.focus_set()
        else:
            self.Delete_Salary_Employee_Find_Btn.focus_set()

    def resetDeleteSalaryEmployeeFindBtn(self, event):
        self.restDeleteSalayBTN()

    def restDeleteSalayBTN(self):
        self.Delete_Salary_Employee_ID_Entry.delete(0, tkinter.END)
        self.Delete_Salary_Employee_Find_Cancel_Btn.focus_set()

    def onEnterDeleteSalaryEmployeeFindBTN(self, event):
        self.empSalFind()

    def onEnterSalaryEmployeeDeleteBtn(self, event):
        self.empSalaryDelete()

    def empSalFind(self):
        empid = self.Delete_Salary_Employee_ID_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM salary where emp_no = '{empid}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
                self.Delete_Salary_Employee_ID_Entry.focus_set()

            elif len(row) == 0:
                tkinter.messagebox.showerror("Error", "Record Not Found")
                self.Delete_Salary_Employee_ID_Entry.focus_set()
            else:
                tkinter.messagebox.showinfo("Success", "Record Found")
                self.Delete_Salary_Employee_Delete_Btn.focus_set()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def empSalaryDelete(self):
        empid = self.Delete_Salary_Employee_ID_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"update salary set ta = NULL, hra = NULL,da = NULL,med = NULL,pf = NULL,basic_salary = NULL, total_sal = NULL where emp_no = '{empid}';"
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Delete successfully")
            self.Find_Delete_salary_Window.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def salaryDetails(self):
        self.totalSalaryGiven = 0
# ---------------List of total Salary Given to Employees ----------------------------------START-------------------#
        self.EmployeeSalary_All_List_Window = tkinter.Toplevel(self.master)
        self.EmployeeSalary_All_List_Window.title("List of Total Salary Given to Employee ....")
        self.EmployeeSalary_All_List_Window.geometry("1200x800+120+85")
        self.EmployeeSalary_All_List_Window.resizable(False, False)

        self.Title_EmployeeSalary_All_List_Label = tkinter.Label(self.EmployeeSalary_All_List_Window,text="List of all Salary Given to Employees:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_EmployeeSalary_All_List_Label.place(x=250, y=20)

        self.EmployeeSalary_All_List_TextArea = tkinter.Text(self.EmployeeSalary_All_List_Window, width=95, height=30,font=("bookman old style", 15))
        self.EmployeeSalary_All_List_TextArea.place(x=25, y=70)

        try:
            self.itemlist.clear()
            self.EmployeeSalary_All_List_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 5
            s3 = " " * 10
            s4 = " " * 10
            s5 = " " * 11
            s6 = " " * 13
            s7 = " " * 9
            s8 = " " * 16
            s9 = " " * 8
            ItemHead = f"Sno.{s2}Employee ID{s4}Total Amount\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = "SELECT * FROM salary;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    if name[3] == None:
                        break
                    else:
                        self.totalSalaryGiven += int(name[8])
                        data = (f"{name[0]}.{s7}{name[1]}{s8}Rs.{name[8]}\n")
                        self.itemlist.append(data)
                data = (f"{s1}\nTotal Salary Given to Employee -> Rs.{self.totalSalaryGiven}\n{s1}")
                self.itemlist.append(data)
                for item in self.itemlist:
                    self.EmployeeSalary_All_List_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))

        finally:
            self.mycursor.close()
            self.myconnect.close()

    # --------------List of total Salary Given to Employees ---------------------------------END-------------------#
    def generatePayslip(self):
        self.generatePaySlip_Window = tkinter.Toplevel(self.master)
        self.generatePaySlip_Window.title("Pay Slip . . .")
        self.generatePaySlip_Window.geometry("1200x800+120+85")
        self.generatePaySlip_Window.resizable(False, False)

        self.Title_Generate_PaySlip_Label = tkinter.Label(self.generatePaySlip_Window,text="Generate Pay Slip:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_Generate_PaySlip_Label.place(x=350, y=20)

        self.Generate_PaySlip_Employee_No_Label = tkinter.Label(self.generatePaySlip_Window, text="Employee ID: ",font=("bookman old style", 15))
        self.Generate_PaySlip_Employee_No_Label.place(x=20, y=60)

        self.Generate_Payslip_Employee_ID_Entry = tkinter.Entry(self.generatePaySlip_Window, width=26,font=("bookman old style", 15))
        self.Generate_Payslip_Employee_ID_Entry.place(x=180, y=60)
        self.Generate_Payslip_Employee_ID_Entry.focus_set()
        self.Generate_Payslip_Employee_ID_Entry.bind("<Return>", self.onEnterGeneratePaySlipEmployeeIDEntry)

        self.Generate_Payslip_Cancel_img = Image.open("icon/cancel13.png").resize((20, 20), Image.BOX)
        self.Generate_Payslip_Cancel_Photoimg = ImageTk.PhotoImage(self.Generate_Payslip_Cancel_img)

        self.Generate_Payslip_Cancel_Btn = tkinter.Button(self.generatePaySlip_Window, text="Cancel", width=210, height=20,font=("bookman old style", 15), command=self.resetGeneratePayslip,
                                bg="#FF7575", fg="white", image=self.Generate_Payslip_Cancel_Photoimg,compound=tkinter.RIGHT)
        self.Generate_Payslip_Cancel_Btn.place(x=500, y=60)

        self.Generate_Payslip_Show_img = Image.open("icon/show.png").resize((40, 40), Image.BOX)
        self.Generate_Payslip_Show_PhotoImage = ImageTk.PhotoImage(self.Generate_Payslip_Show_img)

        self.Generate_Payslip_Show_Btn = tkinter.Button(self.generatePaySlip_Window, text="Show", width=210, height=20, bg="#ceffcf",font=("bookman old style", 15), command=self.recordFoundorNot,
                                             image=self.Generate_Payslip_Show_PhotoImage, compound=tkinter.RIGHT)
        self.Generate_Payslip_Show_Btn.place(x=700, y=60)

        self.Generate_PaySlip_TextArea = tkinter.Text(self.generatePaySlip_Window, width=96, height=29,font=("bookman old style", 15))
        self.Generate_PaySlip_TextArea.place(x=20, y=100)

    def onEnterGeneratePaySlipEmployeeIDEntry(self,event):
        self.recordFoundorNot()

    def recordFoundorNot(self):
        empid = self.Generate_Payslip_Employee_ID_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()

            q = f"SELECT * FROM employee where emp_no = '{empid}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()

            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
                self.Generate_Payslip_Employee_ID_Entry.focus_set()

            elif len(row) == 0:
                tkinter.messagebox.showerror("Error", "Record Not Found")
                self.Generate_Payslip_Employee_ID_Entry.focus_set()
            else:
                for count in range(len(row)):
                    name = row[count]
                    if name[3] == None:
                        self.Generate_Payslip_Employee_ID_Entry.focus_set()
                        tkinter.messagebox.showerror("Error", "Employee Details not Found")
                        self.Generate_PaySlip_TextArea.delete("1.0", tkinter.END)
                        break
                    else:
                        self.generatePaySlip()

        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def resetGeneratePayslip(self):
        self.Generate_Payslip_Employee_ID_Entry.delete(0,tkinter.END)
        self.Generate_PaySlip_TextArea.delete("1.0", tkinter.END)
        self.Generate_Payslip_Employee_ID_Entry.focus_set()

    def generatePaySlip(self):
        try:
            emp_no = self.Generate_Payslip_Employee_ID_Entry.get()
            self.Generate_PaySlip_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 135
            s2 = " " * 23
            s3 = " " * 60
            s4 = " " * 19
            s5 = " " * 35
            s6 = " " * 16
            s7 = " " * 11
            s8 = " " * 36
            s9 = " " * 13
            s10 = " " * 23
            s11 = " " * 18
            s12 = " " * 36
            s13 = " " * 34
            s14 = " " * 39
            s15 = " " * 14
            s16 = " " * 7
            s17 = " " * 17
            s18 = " " * 26
            s19 = " " * 18
            s20 = " " * 16
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()

            q = f"SELECT f_name,l_name, date_of_joining,address, city, state from employee where emp_no ='{emp_no}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                name = row[0]
                data = (f"{s1}\n{s3}Employee Details\n{s1}\n"
                        f"Employee ID: {s2}{emp_no}\n"
                        f"Employee Name: {s11}{name[0].upper()} {name[1].upper()}\n"
                        f"Date of Joining: {s4}{name[2]}\n"
                        f"Place: {s5}{name[3].upper()},{name[4].upper()},{name[5].upper()}\n"
                        f"{s1}\n")
                self.Generate_PaySlip_TextArea.insert(tkinter.END, str(data))
            q = f"SELECT * from salary where emp_no ='{emp_no}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                    tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                name = row[0]
                ta = int(name[2])
                da = int(name[4])
                hra = int(name[3])
                medical = int(name[5])
                total_allow = ta + da + hra + medical
                BS = int(name[7])
                GS = total_allow + BS
                PPF = int(name[6])
                PT =  math.floor(0.03 * BS)
                HEALTHINS =  math.floor(0.05 * BS)
                TDS = math.floor(0.1 * BS)
                Other_Deduction = math.floor(0.01 * BS)
                total_Deduction = PPF + PT + HEALTHINS + TDS + Other_Deduction
                nt = GS - total_Deduction
                data = (f"Travel Allowance: {s6}Rs. {name[2]}\n"
                     f"Dearness Allowance: {s7}Rs. {name[4]}\n"
                     f"HRA: {s8}Rs. {name[3]}\n"
                     f"Medical Allowance: {s9}Rs. {name[5]}\n"
                     f"{s1}\nTotal Allowance: {s19}Rs. {total_allow}\n{s1}\n"
                     f"Basic Salary: {s10}Rs. {name[7]}\n"
                     f"Gross Salary: {s10}Rs. {GS}\n{s1}\n"
                     f"Public Provident Fund: {s16}Rs. {name[6]}\n"
                     f"PT: {s14}Rs. {PT}\n"
                     f"TDS: {s12}Rs. {TDS}\n"
                     f"Health Insurance: {s15}Rs. {HEALTHINS}\n"
                     f"Other Deduction: {s20}Rs. {Other_Deduction}\n"
                     f"{s1}\nTotal Deduction: {s17}Rs. {total_Deduction}\n{s1}\n"
                     f"Net Salary: {s18}Rs. {nt}\n{s1}\n")
                self.Generate_PaySlip_TextArea.insert(tkinter.END, str(data))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()
# ------------------------------------ Area for Salary Structure for Employee -----------END----------------------#

# --------------------------Create Notification Area ------------------------------------START--------------------#
    def createNotification(self):
        self.Create_Notif_Message = tkinter.Toplevel(self.master)
        self.Create_Notif_Message.title("Notification . . .")
        self.Create_Notif_Message.geometry("800x500+420+85")
        self.Create_Notif_Message.resizable(False, False)

        self.Title_Create_Notif_Label = tkinter.Label(self.Create_Notif_Message, text="Create Notification:",
                                             font=("bookman old style", 20, "underline", "bold"))
        self.Title_Create_Notif_Label.place(x=250, y=20)

        self.Choose_User_Label = tkinter.Label(self.Create_Notif_Message, text="Select User: ",
                                               font=("bookman old style", 15))
        self.Choose_User_Label.place(x=110, y=90)

        self.Choose_User_Combobox = tkinter.ttk.Combobox(self.Create_Notif_Message, values=["","Staff","Student"],
                                                         width=34, font=("bookman old style", 15))
        self.Choose_User_Combobox.place(x=250, y=90)
        self.Choose_User_Combobox.focus_set()

        self.Notif_Message_Label = tkinter.Label(self.Create_Notif_Message, text="Message: ",
                                              font=("bookman old style", 15))
        self.Notif_Message_Label.place(x=110, y=130)
        self.Notif_Message_TextArea = tkinter.Text(self.Create_Notif_Message, width=36,height=10, font=("bookman old style", 15))
        self.Notif_Message_TextArea.place(x=250, y=130)

        self.Notif_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Notif_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Notif_Cancel_img)

        self.Notif_Cancel_Btn = tkinter.Button(self.Create_Notif_Message, text="Cancel", width=210, height=30,
                                             font=("bookman old style", 15), command=self.resetcreateNotification,
                              bg="#FF7575", fg="white",image=self.Notif_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Notif_Cancel_Btn.place(x=250, y=373)

        self.Notif_Send_img = Image.open("icon/send.png").resize((50, 50), Image.BOX)
        self.Notif_Send_PhotoImage = ImageTk.PhotoImage(self.Notif_Send_img)

        self.Notif_Send_Btn = tkinter.Button(self.Create_Notif_Message, text="Send", width=210, height=30, bg="#ceffcf",
                                          font=("bookman old style", 15), command=self.sendNotif,
                                          image=self.Notif_Send_PhotoImage, compound=tkinter.RIGHT)
        self.Notif_Send_Btn.place(x=470, y=373)

    def resetcreateNotification(self):
        self.Choose_User_Combobox.set(0)
        self.Notif_Message_TextArea.delete(1.0, tkinter.END)
        self.Choose_User_Combobox.focus_set()

    def sendNotif(self):

        if self.Choose_User_Combobox.get() == "":
            tkinter.messagebox.showerror("Error", "Please Select User Type")
        elif self.Notif_Message_TextArea.get(1.0, tkinter.END) == "":
            tkinter.messagebox.showerror("Error", "Please Write Message")
        else:
            u1, u2, u3, u4 = 1, "", "", "pending"
            try:
                u2 = self.Choose_User_Combobox.get()
                u3 = self.Notif_Message_TextArea.get(1.0, tkinter.END)
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"insert into notif (utype, notif_msg, notif_status) values ('{u2}','{u3}', '{u4}');"
                self.mycursor.execute(q)
                self.myconnect.commit()
                tkinter.messagebox.showinfo("Success", "Notification Send successfully")
                self.resetcreateNotification()
                self.Create_Notif_Message.destroy()
            except MySQLdb.Error as e:
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            finally:
                self.mycursor.close()
                self.myconnect.close()

# --------------------------Create Notification Area ------------------------------------END--------------------#

# -------------------------AREA for show all notification -------------------------------START -------------------#
    def allNotification(self):

# ---------------List of all Notification send to Staff -----------------------------------START-------------------#

        self.Staff_All_List_Window = tkinter.Toplevel(self.master)
        self.Staff_All_List_Window.title("Notification List . . .")
        self.Staff_All_List_Window.geometry("1200x800+120+85")
        self.Staff_All_List_Window.resizable(False, False)

        self.Title_Staff_All_List_Label = tkinter.Label(self.Staff_All_List_Window, text="List of all Notification send to Staff:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Staff_All_List_Label.place(x=250, y=20)

        self.Staff_All_List_SearchBox_TextArea = tkinter.Text(self.Staff_All_List_Window, width=95, height=30,
                                                           font=("bookman old style", 15))
        self.Staff_All_List_SearchBox_TextArea.place(x=25, y=70)
        try:
            self.itemlist.clear()
            self.Staff_All_List_SearchBox_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 3
            s3 = " " * 5
            s4 = " " * 3
            s5 = " " * 3
            ItemHead = f"ID.{s2}Status{s3}Message\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM notif where utype='Staff';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    data = (f"{name[0]}.{s4}{name[3]}{s5}{name[2]}")
                    self.itemlist.append(data)
                for item in self.itemlist:
                    self.Staff_All_List_SearchBox_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

# ---------------List of all Notification send to Staff ---------------------------------END-------------------#

# ----------------List of all Notification send to Student -----------------------------------START-----------#
        self.STD_All_List_Window = tkinter.Toplevel(self.master)
        self.STD_All_List_Window.title("Notification List . . .")
        self.STD_All_List_Window.geometry("1200x800+220+185")
        self.STD_All_List_Window.resizable(False, False)

        self.Title_STD_All_List_Label = tkinter.Label(self.STD_All_List_Window, text="List of all Notification send to Student:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_STD_All_List_Label.place(x=250, y=20)

        self.STD_All_List_SearchBox_TextArea = tkinter.Text(self.STD_All_List_Window, width=95, height=30,font=("bookman old style", 15))
        self.STD_All_List_SearchBox_TextArea.place(x=25, y=70)

        try:
            self.itemlist.clear()
            self.STD_All_List_SearchBox_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 3
            s3 = " " * 5
            s4 = " " * 3
            s5 = " " * 3
            ItemHead = f"ID.{s2}Status{s3}Message\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM notif where utype='Student';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    data = (f"{name[0]}.{s4}{name[3]}{s5}{name[2]}")
                    self.itemlist.append(data)
                for item in self.itemlist:
                    self.STD_All_List_SearchBox_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

# ----------------List of all Notification send to Student -----------------------------------END-----------------#

# -------------------------AREA for show all notification -------------------------------END -------------------#

# --------------------------------------------- Area for Student ----------------------START----------------------#
    def addNewStudent(self):
        self.Add_New_Student = tkinter.Toplevel(self.master)
        self.Add_New_Student.title("Add New Student")
        self.Add_New_Student.geometry("1000x700+420+85")
        self.Add_New_Student.resizable(False, False)

        self.Title_New_Student_Label = tkinter.Label(self.Add_New_Student, text="Student Admission Form:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_New_Student_Label.place(x=250, y=20)

# ---------Get New Student Roll No -----------------------------------------------------------START-------------#

        self.Student_Roll_No_Label = tkinter.Label(self.Add_New_Student, text="Student Roll No: ",font=("bookman old style", 15))
        self.Student_Roll_No_Label.place(x=150, y=90)

        self.Student_Roll_No_Entry = tkinter.Entry(self.Add_New_Student, width=38, font=("bookman old style", 15))
        self.Student_Roll_No_Entry.place(x=400, y=90)
        self.Student_Roll_No_Entry.insert(0, getIdNumber.getRollNoinStudentTable())
        self.Student_Roll_No_Entry.config(state=tkinter.DISABLED)

#--------Get New Student Roll No -----------------------------------------------------------END-------------#

        self.Class_Label = tkinter.Label(self.Add_New_Student, text="Class: ", font=("bookman old style", 15))
        self.Class_Label.place(x=150, y=130)

        self.Class_Entry = tkinter.ttk.Combobox(self.Add_New_Student, width=36, values=["", "Class 1", "Class 2", "Class 3",
                     "Class 4","Class 5","Class 6","Class 7","Class 8","Class 9","Class 10"],font=("bookman old style", 15))
        self.Class_Entry.place(x=400, y=130)
        self.Class_Entry.focus_set()
        self.Class_Entry.bind("<Return>",self.onEnterStudentClassType)

        self.Student_F_Name_Label = tkinter.Label(self.Add_New_Student, text="First Name: ", font=("bookman old style", 15))
        self.Student_F_Name_Label.place(x=150, y=170)

        self.Student_F_Name_Entry = tkinter.Entry(self.Add_New_Student, width=38, font=("bookman old style", 15))
        self.Student_F_Name_Entry.place(x=400, y=170)
        self.Student_F_Name_Entry.bind("<Return>", self.onEnterStudentFirstName)

        self.Student_L_Name_Label = tkinter.Label(self.Add_New_Student, text="Last Name: ", font=("bookman old style", 15))
        self.Student_L_Name_Label.place(x=150, y=210)

        self.Student_L_Name_Entry = tkinter.Entry(self.Add_New_Student, width=38, font=("bookman old style", 15))
        self.Student_L_Name_Entry.place(x=400, y=210)
        self.Student_L_Name_Entry.bind("<Return>", self.onEnterStudentLastName)

        self.Student_Gender_Label = tkinter.Label(self.Add_New_Student, text="Gender: ", font=("bookman old style", 15))
        self.Student_Gender_Label.place(x=150, y=250)

        self.Student_Gender_Entry = tkinter.ttk.Combobox(self.Add_New_Student, width=36, values=["", "Male", "Female", "Other"],font=("bookman old style", 15))
        self.Student_Gender_Entry.place(x=400, y=250)
        self.Student_Gender_Entry.bind("<Return>", self.onEnterStudentGender)

        self.Guardian_Phone_No_Label = tkinter.Label(self.Add_New_Student, text="Guardian Phone No: ",font=("bookman old style", 15))
        self.Guardian_Phone_No_Label.place(x=150, y=290)

        self.Guardian_Phone_No_Entry = tkinter.Entry(self.Add_New_Student, width=38, font=("bookman old style", 15))
        self.Guardian_Phone_No_Entry.place(x=400, y=290)
        self.Guardian_Phone_No_Entry.bind("<Return>", self.onEnterStudentPhoneNo)

        self.Date_of_Admission_Label = tkinter.Label(self.Add_New_Student, text="Date of Admission: ", font=("bookman old style", 15))
        self.Date_of_Admission_Label.place(x=150, y=330)

        self.Date_of_Admission_Entry = DateEntry(self.Add_New_Student, selectmode="day", date_pattern="dd/mm/yyyy", sticky="w", font=("bookman old style", 15))
        self.Date_of_Admission_Entry.configure(width=36)
        self.Date_of_Admission_Entry.place(x=400, y=330)
        self.Date_of_Admission_Entry.bind("<Return>",self.onEnterStudentDateOfJoining)

        self.Student_Address_Label = tkinter.Label(self.Add_New_Student, text="Address: ", font=("bookman old style", 15))
        self.Student_Address_Label.place(x=150, y=370)

        self.Student_Address_Entry = tkinter.Entry(self.Add_New_Student, width=38, font=("bookman old style", 15))
        self.Student_Address_Entry.place(x=400, y=370)
        self.Student_Address_Entry.bind("<Return>", self.onEnterStudentAddress)

        self.Student_City_Label = tkinter.Label(self.Add_New_Student, text="City: ", font=("bookman old style", 15))
        self.Student_City_Label.place(x=150, y=410)

        self.Student_City_Entry = tkinter.Entry(self.Add_New_Student, width=38, font=("bookman old style", 15))
        self.Student_City_Entry.place(x=400, y=410)
        self.Student_City_Entry.bind("<Return>", self.onEnterStudentCity)

        self.Student_State_Label = tkinter.Label(self.Add_New_Student, text="State: ", font=("bookman old style", 15))
        self.Student_State_Label.place(x=150, y=450)

        self.Student_State_Entry = tkinter.Entry(self.Add_New_Student, width=38, font=("bookman old style", 15))
        self.Student_State_Entry.place(x=400, y=450)
        self.Student_State_Entry.bind("<Return>", self.onEnterStudentState)

        self.Std_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Std_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Std_Cancel_img)

        self.Add_Std_Cancel_Btn = tkinter.Button(self.Add_New_Student, text="Cancel", width=225, height=30,font=("bookman old style", 15),command=self.resetAddNewStudentForm,
                            bg="#FF7575", fg="white",image=self.Std_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Add_Std_Cancel_Btn.place(x=400, y=490)

        self.Std_Move_img = Image.open("icon/move1.png").resize((26, 26), Image.BOX)
        self.Std_Move_img_PhotoImage = ImageTk.PhotoImage(self.Std_Move_img)

        self.Add_Std_Move_Btn = tkinter.Button(self.Add_New_Student, text="Move", width=225, height=30,font=("bookman old style", 15), bg="#FFFF99",
                            command=self.savedStudentData, image=self.Std_Move_img_PhotoImage,compound=tkinter.RIGHT)
        self.Add_Std_Move_Btn.place(x=635, y=490)
        self.Add_Std_Move_Btn.bind("<Return>", self.onEnterSaveBtn)

# ----------------Add New Student Data saved in Database ----------------------------------------------START ------#

    def onEnterStudentClassType(self, event):
        if self.Class_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Class")
            self.Class_Entry.focus_set()
        else:
            self.Student_F_Name_Entry.focus_set()

    def onEnterStudentFirstName(self, event):
        if self.Student_F_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student First Name")
            self.Student_F_Name_Entry.focus_set()
        else:
            self.Student_L_Name_Entry.focus_set()

    def onEnterStudentLastName(self, event):
        if self.Student_L_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Last Name")
            self.Student_L_Name_Entry.focus_set()
        else:
            self.Student_Gender_Entry.focus_set()

    def onEnterStudentGender(self, event):
        if self.Student_Gender_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Gender")
            self.Student_Gender_Entry.focus_set()
        else:
            self.Guardian_Phone_No_Entry.focus_set()

    def onEnterStudentPhoneNo(self, event):
        if self.Guardian_Phone_No_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Guardian Phone No")
            self.Guardian_Phone_No_Entry.focus_set()
        else:
            self.Date_of_Admission_Entry.focus_set()

    def onEnterStudentDateOfJoining(self, event):
        self.Student_Address_Entry.focus_set()

    def onEnterStudentAddress(self, event):
        if self.Student_Address_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Address")
            self.Student_Address_Entry.focus_set()
        else:
            self.Student_City_Entry.focus_set()

    def onEnterStudentCity(self, event):
        if self.Student_City_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student City")
            self.Student_City_Entry.focus_set()
        else:
            self.Student_State_Entry.focus_set()

    def onEnterStudentState(self, event):
        if self.Student_State_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student State")
            self.Student_State_Entry.focus_set()
        else:
            self.Add_Std_Move_Btn.focus_set()

    def onEnterSaveBtn(self,event):
        self.savedStudentData()

    def resetAddNewStudentForm(self):
        self.Class_Entry.current(0)
        self.Student_Roll_No_Entry.delete(0, tkinter.END)
        self.Student_F_Name_Entry.delete(0, tkinter.END)
        self.Student_L_Name_Entry.delete(0, tkinter.END)
        self.Student_Gender_Entry.delete(0, tkinter.END)
        self.Guardian_Phone_No_Entry.delete(0, tkinter.END)
        self.Student_Address_Entry.delete(0, tkinter.END)
        self.Student_City_Entry.delete(0, tkinter.END)
        self.Student_State_Entry.delete(0, tkinter.END)
        self.Class_Entry.focus_set()

    def savedStudentData(self):
        u1 = self.Student_Roll_No_Entry.get().strip()
        u2 = self.Class_Entry.get().strip()
        u3 = self.Student_F_Name_Entry.get().strip()
        u4 = self.Student_L_Name_Entry.get().strip()
        u5 = self.Student_Gender_Entry.get().strip()
        u6 = self.Guardian_Phone_No_Entry.get().strip()
        u7 = self.Date_of_Admission_Entry.get().strip()
        u8 = self.Student_Address_Entry.get().strip()
        u9 = self.Student_City_Entry.get().strip()
        u10 = self.Student_State_Entry.get().strip()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = (f"update student set adm_in_class = '{u2}',f_name = '{u3}', l_name = '{u4}',gender = '{u5}',gardian_Phone_no = '{u6}',"
                f"date_of_Admission = '{u7}', address = '{u8}',city = '{u9}',state = '{u10}' where roll_no = '{u1}';")
            self.mycursor.execute(q)
            self.myconnect.commit()

            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.Add_New_Student.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

# -------------------saved data and call open salary form ----------------------------START -------------------#
            self.addNewFee()
# -------------------saved data and call open Fee form ---------------------------------END -------------------#

    def updateStudent(self):
        self.update_Student_Window = tkinter.Toplevel(self.master)
        self.update_Student_Window.title("Update . . .")
        self.update_Student_Window.geometry("1000x600+420+85")
        self.update_Student_Window.resizable(False, False)

        self.Title_Update_Student_Label = tkinter.Label(self.update_Student_Window, text="Update Student Records:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Update_Student_Label.place(x=250, y=20)

        self.Update_Student_Roll_No_Label = tkinter.Label(self.update_Student_Window, text="Student Roll No: ", font=("bookman old style", 15))
        self.Update_Student_Roll_No_Label.place(x=150, y=90)

        self.Update_Student_Roll_No_Entry = tkinter.Entry(self.update_Student_Window, width=38, font=("bookman old style", 15))
        self.Update_Student_Roll_No_Entry.place(x=400, y=90)
        self.Update_Student_Roll_No_Entry.focus_set()
        self.Update_Student_Roll_No_Entry.bind("<Return>",self.onEnterSearchStudentRollNo)

        self.Update_Class_Label = tkinter.Label(self.update_Student_Window, text="Class: ", font=("bookman old style", 15))
        self.Update_Class_Label.place(x=150, y=130)

        self.Update_Class_Entry = tkinter.ttk.Combobox(self.update_Student_Window, width=36, values=["", "Class 1", "Class 2", "Class 3",
                         "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10"],font=("bookman old style", 15))
        self.Update_Class_Entry.place(x=400, y=130)
        self.Update_Class_Entry.focus_set()
        self.Update_Class_Entry.bind("<Return>", self.onEnterUpdateStudentClassType)

        self.Update_Student_F_Name_Label = tkinter.Label(self.update_Student_Window, text="First Name: ",font=("bookman old style", 15))
        self.Update_Student_F_Name_Label.place(x=150, y=170)

        self.Update_Student_F_Name_Entry = tkinter.Entry(self.update_Student_Window, width=38, font=("bookman old style", 15))
        self.Update_Student_F_Name_Entry.place(x=400, y=170)
        self.Update_Student_F_Name_Entry.bind("<Return>", self.onEnterUpdateStudentFirstName)

        self.Update_Student_L_Name_Label = tkinter.Label(self.update_Student_Window, text="Last Name: ",  font=("bookman old style", 15))
        self.Update_Student_L_Name_Label.place(x=150, y=210)

        self.Update_Student_L_Name_Entry = tkinter.Entry(self.update_Student_Window, width=38, font=("bookman old style", 15))
        self.Update_Student_L_Name_Entry.place(x=400, y=210)
        self.Update_Student_L_Name_Entry.bind("<Return>", self.onEnterUpdateStudentLastName)

        self.Update_Student_Gender_Label = tkinter.Label(self.update_Student_Window, text="Gender: ", font=("bookman old style", 15))
        self.Update_Student_Gender_Label.place(x=150, y=250)

        self.Update_Student_Gender_Entry = tkinter.ttk.Combobox(self.update_Student_Window, width=36, values=["", "Male", "Female", "Other"], font=("bookman old style", 15))
        self.Update_Student_Gender_Entry.place(x=400, y=250)
        self.Update_Student_Gender_Entry.bind("<Return>", self.onEnterUpdateStudentGender)

        self.Update_Guardian_Phone_No_Label = tkinter.Label(self.update_Student_Window, text="Guardian Phone No: ", font=("bookman old style", 15))
        self.Update_Guardian_Phone_No_Label.place(x=150, y=290)

        self.Update_Guardian_Phone_No_Entry = tkinter.Entry(self.update_Student_Window, width=38, font=("bookman old style", 15))
        self.Update_Guardian_Phone_No_Entry.place(x=400, y=290)
        self.Update_Guardian_Phone_No_Entry.bind("<Return>", self.onEnterUpdateStudentPhoneNo)

        self.Update_Student_Address_Label = tkinter.Label(self.update_Student_Window, text="Address: ",font=("bookman old style", 15))
        self.Update_Student_Address_Label.place(x=150, y=330)

        self.Update_Student_Address_Entry = tkinter.Entry(self.update_Student_Window, width=38, font=("bookman old style", 15))
        self.Update_Student_Address_Entry.place(x=400, y=330)
        self.Update_Student_Address_Entry.bind("<Return>", self.onEnterUpdateStudentAddress)

        self.Update_Student_City_Label = tkinter.Label(self.update_Student_Window, text="City: ", font=("bookman old style", 15))
        self.Update_Student_City_Label.place(x=150, y=370)

        self.Update_Student_City_Entry = tkinter.Entry(self.update_Student_Window, width=38, font=("bookman old style", 15))
        self.Update_Student_City_Entry.place(x=400, y=370)
        self.Update_Student_City_Entry.bind("<Return>", self.onEnterUpdateStudentCity)

        self.Update_Student_State_Label = tkinter.Label(self.update_Student_Window, text="State: ", font=("bookman old style", 15))
        self.Update_Student_State_Label.place(x=150, y=410)

        self.Update_Student_State_Entry = tkinter.Entry(self.update_Student_Window, width=38, font=("bookman old style", 15))
        self.Update_Student_State_Entry.place(x=400, y=410)
        self.Update_Student_State_Entry.bind("<Return>", self.onEnterUpdateStudentState)

        self.Update_Std_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Update_Std_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Update_Std_Cancel_img)

        self.Update_Add_Std_Cancel_Btn = tkinter.Button(self.update_Student_Window, text="Cancel", width=225, height=30,font=("bookman old style", 15), command=self.resetUpdateStudentForm,
                                 bg="#FF7575", fg="white", image=self.Update_Std_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Update_Add_Std_Cancel_Btn.place(x=400, y=450)

        self.Update_Std_Move_img = Image.open("icon/move1.png").resize((26, 26), Image.BOX)
        self.Update_Std_Move_img_PhotoImage = ImageTk.PhotoImage(self.Update_Std_Move_img)

        self.Update_Add_Std_Move_Btn = tkinter.Button(self.update_Student_Window, text="Move", width=225, height=30,font=("bookman old style", 15), bg="#FFFF99",
                              command=self.updateStudentData, image=self.Update_Std_Move_img_PhotoImage,compound=tkinter.RIGHT)
        self.Update_Add_Std_Move_Btn.place(x=635, y=450)
        self.Update_Add_Std_Move_Btn.bind("<Return>", self.onEnterUpdateStudentBtn)

        # ----------------Add New Student Data saved in Database ----------------------------------------------START ------#

    def onEnterSearchStudentRollNo(self,bind):
        self.resetUpdateStudentForm()
        rollno = self.Update_Student_Roll_No_Entry.get()
        if rollno == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Roll No")
            self.Update_Student_Roll_No_Entry.focus_set()
        else:
            try:
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"SELECT * FROM student where roll_no = '{rollno}';"
                self.mycursor.execute(q)
                row = self.mycursor.fetchall()
                if row == None:
                    tkinter.messagebox.showerror("Error", "Invalid details")
                    self.Update_Student_Roll_No_Entry.focus_set()
                elif len(row) == 0:
                    tkinter.messagebox.showerror("Error", "No Record Found")
                    self.Update_Student_Roll_No_Entry.focus_set()
                else:
                    for count in range(1):
                        name = row[count]
                        self.Update_Student_F_Name_Entry.insert(0, name[2])
                        self.Update_Student_L_Name_Entry.insert(0, name[3])
                        self.Update_Student_Gender_Entry.insert(0, name[4])
                        self.Update_Class_Entry.insert(0, name[5])
                        self.Update_Guardian_Phone_No_Entry.insert(0, name[7])
                        self.Update_Student_Address_Entry.insert(0, name[8])
                        self.Update_Student_City_Entry.insert(0, name[9])
                        self.Update_Student_State_Entry.insert(0, name[10])
            except Exception as ee:
                print(str(ee))
            finally:
                self.mycursor.close()
                self.myconnect.close()
            self.Update_Class_Entry.focus_set()

    def onEnterUpdateStudentClassType(self, event):
        if self.Update_Class_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Class")
            self.Update_Class_Entry.focus_set()
        else:
            self.Update_Student_F_Name_Entry.focus_set()

    def onEnterUpdateStudentFirstName(self, event):
        if self.Update_Student_F_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student First Name")
            self.Update_Student_F_Name_Entry.focus_set()
        else:
            self.Update_Student_L_Name_Entry.focus_set()

    def onEnterUpdateStudentLastName(self, event):
        if self.Update_Student_L_Name_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Last Name")
            self.Update_Student_L_Name_Entry.focus_set()
        else:
            self.Update_Student_Gender_Entry.focus_set()

    def onEnterUpdateStudentGender(self, event):
        if self.Update_Student_Gender_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Gender")
            self.Update_Student_Gender_Entry.focus_set()
        else:
            self.Update_Guardian_Phone_No_Entry.focus_set()

    def onEnterUpdateStudentPhoneNo(self, event):
        if self.Update_Guardian_Phone_No_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Guardian Phone No")
            self.Update_Guardian_Phone_No_Entry.focus_set()
        else:
            self.Update_Student_Address_Entry.focus_set()

    def onEnterUpdateStudentAddress(self, event):
        if self.Update_Student_Address_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Address")
            self.Update_Student_Address_Entry.focus_set()
        else:
            self.Update_Student_City_Entry.focus_set()

    def onEnterUpdateStudentCity(self, event):
        if self.Update_Student_City_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student City")
            self.Update_Student_City_Entry.focus_set()
        else:
            self.Update_Student_State_Entry.focus_set()

    def onEnterUpdateStudentState(self, event):
        if self.Update_Student_State_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student State")
            self.Update_Student_State_Entry.focus_set()
        else:
            self.Update_Add_Std_Move_Btn.focus_set()

    def onEnterUpdateStudentBtn(self, event):
        self.updateStudentData()

    def resetUpdateStudentForm(self):
        self.Update_Student_F_Name_Entry.delete(0,tkinter.END)
        self.Update_Student_L_Name_Entry.delete(0,tkinter.END)
        self.Update_Student_Gender_Entry.delete(0,tkinter.END)
        self.Update_Class_Entry.current(0)
        self.Update_Guardian_Phone_No_Entry.delete(0,tkinter.END)
        self.Update_Student_Address_Entry.delete(0,tkinter.END)
        self.Update_Student_City_Entry.delete(0,tkinter.END)
        self.Update_Student_State_Entry.delete(0,tkinter.END)
        self.Update_Student_Roll_No_Entry.focus_set()

    def updateStudentData(self):
        u1 = self.Update_Student_Roll_No_Entry.get().strip()
        u2 = self.Update_Class_Entry.get().strip()
        u3 = self.Update_Student_F_Name_Entry.get().strip()
        u4 = self.Update_Student_L_Name_Entry.get().strip()
        u5 = self.Update_Student_Gender_Entry.get().strip()
        u6 = self.Update_Guardian_Phone_No_Entry.get().strip()
        u7 = self.Update_Student_Address_Entry.get().strip()
        u8 = self.Update_Student_City_Entry.get().strip()
        u9 = self.Update_Student_State_Entry.get().strip()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = (f"update student set adm_in_class = '{u2}',f_name = '{u3}', l_name = '{u4}',gender = '{u5}',gardian_Phone_no = '{u6}',"
                f"address = '{u7}',city = '{u8}',state = '{u9}' where roll_no = '{u1}';")
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.update_Student_Window.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

# ----------------update Employee Data saved in Database ----------------------------------------------START ------#

# --------------------------------------Update Student record -----------------------------END -------------------#
    def deleteStudent(self):
        self.Find_Student_Window = tkinter.Toplevel(self.master)
        self.Find_Student_Window.title("Find Student")
        self.Find_Student_Window.geometry("600x260+420+85")
        self.Find_Student_Window.resizable(False, False)

        self.Title_Find_Student_Label = tkinter.Label(self.Find_Student_Window, text="_____Find Details____",font=("bookman old style", 20, "bold"))
        self.Title_Find_Student_Label.place(x=130, y=20)

        self.Student_Find_Frame = tkinter.LabelFrame(self.Find_Student_Window, bg="#EDF5F4")
        self.Student_Find_Frame.place(x=20, y=70, height=160, width=550)

        self.Student_Roll_No_Label = tkinter.Label(self.Student_Find_Frame, text="Student Roll: ",font=("bookman old style", 15))
        self.Student_Roll_No_Label.place(x=20, y=20)

        self.Student_Roll_No_Entry = tkinter.Entry(self.Student_Find_Frame, width=26, font=("bookman old style", 15))
        self.Student_Roll_No_Entry.place(x=180, y=20)
        self.Student_Roll_No_Entry.focus_set()
        self.Student_Roll_No_Entry.bind("<Return>", self.onEnterStudentRollNoEntry)

        self.Student_Find_Cancel_Img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Student_Find_Cancel_PhotoImage = ImageTk.PhotoImage(self.Student_Find_Cancel_Img)

        self.Student_Find_Cancel_Btn = tkinter.Button(self.Student_Find_Frame, text="Cancel", width=148, height=30,
                        font=("bookman old style", 15), command=self.resetStudnetFindBtn, image=self.Student_Find_Cancel_PhotoImage,compound=tkinter.LEFT)
        self.Student_Find_Cancel_Btn.place(x=180, y=60)

        self.Student_Find_Img = Image.open("icon/find2.jpg").resize((26, 26), Image.BOX)
        self.Student_Find_PhotoImage = ImageTk.PhotoImage(self.Student_Find_Img)

        self.Student_Find_Btn = tkinter.Button(self.Student_Find_Frame, text="Find", width=148, height=30,font=("bookman old style", 15), command=self.stdFind,
                                            image=self.Student_Find_PhotoImage, compound=tkinter.LEFT)
        self.Student_Find_Btn.place(x=335, y=60)
        self.Student_Find_Btn.bind("<Return>", self.onEnterStudentFindBTN)

        self.Student_Delete_Img = Image.open("icon/delete.jpg").resize((30, 30), Image.BOX)
        self.Student_Delete_PhotoImage = ImageTk.PhotoImage(self.Student_Delete_Img)

        self.Student_Delete_Btn = tkinter.Button(self.Student_Find_Frame, text="Delete", width=301, height=30, font=("bookman old style", 15), command=self.stdDelete,
                                        image=self.Student_Delete_PhotoImage, compound=tkinter.LEFT)
        self.Student_Delete_Btn.place(x=180, y=100)
        self.Student_Delete_Btn.bind("<Return>", self.onEnterStudentDeleteBtn)

        # ------------------------Find Form Function ----------------------------------END-------------------------------#

        # ----------- all functions ------------------------

    def onEnterStudentRollNoEntry(self, event):
        if self.Student_Roll_No_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Roll No")
            self.Student_Roll_No_Entry.focus_set()
        else:
            self.Student_Find_Btn.focus_set()

    def resetStudnetFindBtn(self):
        self.Student_Roll_No_Entry.delete(0, tkinter.END)
        self.Student_Roll_No_Entry.focus_set()

    def onEnterStudentFindBTN(self, event):
        self.stdFind()

    def onEnterStudentDeleteBtn(self, event):
        self.stdDelete()

    def stdFind(self):
        rollNo = self.Student_Roll_No_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM student where roll_no = '{rollNo}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
                self.Student_Roll_No_Entry.focus_set()
            elif len(row) == 0:
                tkinter.messagebox.showerror("Error", "Record Not Found")
                self.Student_Roll_No_Entry.focus_set()
            else:
                tkinter.messagebox.showinfo("Success", "Record Found")
                self.Student_Delete_Btn.focus_set()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()
    def stdDelete(self):
        rollNo = self.Student_Roll_No_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = (f"update student set adm_in_class = NULL, f_name = NULL, l_name = NULL,gender = NULL, gardian_Phone_no = NULL,"
                f"date_of_admission = NULL, address = NULL,city = NULL,state = NULL where roll_no = '{rollNo}';")
            self.mycursor.execute(q)
            self.myconnect.commit()
            q = f"update fee set admission_fee = NULL, Tution_fee = NULL,dev_fee = NULL,cantine_fee = NULL,bus_fee = NULL,sports_fee = NULL, total_fee = NULL where roll_no = '{rollNo}';"
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Delete successfully")
            self.Find_Student_Window.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def listStudent(self):

# ---------------List of all Student in the School -----------------------------------START-------------------#

        self.Student_All_List_Window = tkinter.Toplevel(self.master)
        self.Student_All_List_Window.title("Student List . . .")
        self.Student_All_List_Window.geometry("1200x800+120+85")
        self.Student_All_List_Window.resizable(False, False)

        self.Title_Student_All_List_Label = tkinter.Label(self.Student_All_List_Window,  text="List of all Student:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Student_All_List_Label.place(x=250, y=20)

        self.Student_All_List_TextArea = tkinter.Text(self.Student_All_List_Window, width=95, height=30,   font=("bookman old style", 15))
        self.Student_All_List_TextArea.place(x=25, y=70)

        try:
            self.itemlist.clear()
            self.Student_All_List_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 5
            s3 = " " * 10
            s4 = " " * 10
            s5 = " " * 11
            s6 = " " * 13
            s7 = " " * 8
            s8 = " " * 7
            s9 = " " * 8
            ItemHead = f"Sno.{s2}Roll No{s4}Class{s3}Name\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = "SELECT * FROM student;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    if name[3] == None:
                        data = (f"{s1}\nTotal Student Registered -> {count}\n{s1}")
                        self.itemlist.append(data)
                        break
                    else:
                        data = (f"{name[0]}.{s7}{name[1]}{s8}{name[5]}{s9}{name[2]} {name[3]}\n")
                        self.itemlist.append(data)
                for item in self.itemlist:
                    self.Student_All_List_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

# -----------------List of all Student in the School--------------------------------END-------------------#

# ----------------------------------------------- Area for Student -----------------------END----------------------#

# ----------------------------- Area for Fee Structure for Student ----------------------START----------------------#
    def addNewFee(self):
        self.Add_New_Fee = tkinter.Toplevel(self.master)
        self.Add_New_Fee.title("Register Fee")
        self.Add_New_Fee.geometry("800x500+420+85")
        self.Add_New_Fee.resizable(False, False)

        self.Title_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Fee Form:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Fee_Label.place(x=300, y=20)

# ---------Get New Student Roll No -----------------------------------------------------------START-------------#

        self.Std_Roll_No_Label = tkinter.Label(self.Add_New_Fee, text="Student Roll No: ",    font=("bookman old style", 15))
        self.Std_Roll_No_Label.place(x=110, y=90)

        self.Std_Roll_No_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Std_Roll_No_Entry.place(x=390, y=90)
        self.Std_Roll_No_Entry.insert(0, getIdNumber.getRollNoinFeeTable())
        self.Std_Roll_No_Entry.config(state=tkinter.DISABLED)

# --------Get New Student Roll No -----------------------------------------------------------END-------------#

        self.Admission_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Admission Fee: ", font=("bookman old style", 15))
        self.Admission_Fee_Label.place(x=110, y=130)

        self.Admission_Fee_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Admission_Fee_Entry.place(x=390, y=130)
        self.Admission_Fee_Entry.focus_set()
        self.Admission_Fee_Entry.bind("<Return>", self.onEnterAdmissionFee)

        self.Tuition_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Tuition Fee: ",font=("bookman old style", 15))
        self.Tuition_Fee_Label.place(x=110, y=170)

        self.Tuition_Fee_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Tuition_Fee_Entry.place(x=390, y=170)
        self.Tuition_Fee_Entry.bind("<Return>", self.onEnterTuitionFee)

        self.Dev_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Development Fee: ", font=("bookman old style", 15))
        self.Dev_Fee_Label.place(x=110, y=210)

        self.Dev_Fee_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Dev_Fee_Entry.place(x=390, y=210)
        self.Dev_Fee_Entry.bind("<Return>", self.onEnterDevFee)

        self.Cantine_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Cantine Fee: ", font=("bookman old style", 15))
        self.Cantine_Fee_Label.place(x=110, y=250)

        self.Cantine_Fee_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Cantine_Fee_Entry.place(x=390, y=250)
        self.Cantine_Fee_Entry.bind("<Return>", self.onEnterCantineFee)

        self.Bus_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Bus Fee: ", font=("bookman old style", 15))
        self.Bus_Fee_Label.place(x=110, y=290)

        self.Bus_Fee_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Bus_Fee_Entry.place(x=390, y=290)
        self.Bus_Fee_Entry.bind("<Return>", self.onEnterBusFee)

        self.Sports_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Sports Fee: ",   font=("bookman old style", 15))
        self.Sports_Fee_Label.place(x=110, y=330)

        self.Sports_Fee_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Sports_Fee_Entry.place(x=390, y=330)
        self.Sports_Fee_Entry.bind("<Return>", self.onEnterSportsFee)

        self.Total_Fee_Label = tkinter.Label(self.Add_New_Fee, text="Total Fee: ",font=("bookman old style", 15))
        self.Total_Fee_Label.place(x=110, y=370)

        self.Total_Fee_Entry = tkinter.Entry(self.Add_New_Fee, width=27, font=("bookman old style", 15))
        self.Total_Fee_Entry.place(x=390, y=370)
        self.Total_Fee_Entry.bind("<Return>", self.onEnterTotalFee)

        self.Std_Fee_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Std_Fee_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Std_Fee_Cancel_img)

        self.Fee_Cancel_Btn = tkinter.Button(self.Add_New_Fee, text="Cancel", width=152, height=30,font=("bookman old style", 15), command=self.resetNewFeeForm,bg="#FF7575", fg="white",
                            image=self.Std_Fee_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Fee_Cancel_Btn.place(x=390, y=410)

        self.Std_Fee_Pay_img = Image.open("icon/save1.png").resize((26, 26), Image.BOX)
        self.Std_Fee_Pay_img_PhotoImage = ImageTk.PhotoImage(self.Std_Fee_Pay_img)

        self.Fee_Pay_Btn = tkinter.Button(self.Add_New_Fee, text="Pay", width=152, height=30, bg="#ceffcf", font=("bookman old style", 15), command=self.submitStudentAllData,
                                            image=self.Std_Fee_Pay_img_PhotoImage, compound=tkinter.RIGHT)
        self.Fee_Pay_Btn.place(x=550, y=410)
        self.Fee_Pay_Btn.bind("<Return>",self.onEnterSubmitFee)

# ----------------Add Fee for New Student Data saved in Database ----------------------------------------------START ------#

    def onEnterAdmissionFee(self, event):

        try:
            if self.Admission_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Admission Fee")
                self.Admission_Fee_Entry.focus_set()
            elif int(self.Admission_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Admission_Fee_Entry.focus_set()
            else:
                self.Tuition_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterTuitionFee(self, event):

        try:
            if self.Tuition_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Tuition Fee")
                self.Tuition_Fee_Entry.focus_set()
            elif int(self.Tuition_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Tuition_Fee_Entry.focus_set()
            else:
                self.Dev_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterDevFee(self, event):
        try:
            if self.Dev_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Development Fee")
                self.Dev_Fee_Entry.focus_set()
            elif int(self.Dev_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Dev_Fee_Entry.focus_set()
            else:
                self.Cantine_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterCantineFee(self, event):
        try:
            if self.Cantine_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Cantine Fee")
                self.Cantine_Fee_Entry.focus_set()
            elif int(self.Cantine_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Cantine_Fee_Entry.focus_set()
            else:
                self.Bus_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterBusFee(self, event):
        try:
            if self.Bus_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Bus Fee")
                self.Bus_Fee_Entry.focus_set()
            elif int(self.Bus_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Bus_Fee_Entry.focus_set()
            else:
                self.Sports_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterSportsFee(self, event):
        try:
            if self.Sports_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Sports Fee")
                self.Sports_Fee_Entry.focus_set()
            elif int(self.Sports_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Sports_Fee_Entry.focus_set()
            else:
                u2 = int(self.Admission_Fee_Entry.get())
                u3 = int(self.Tuition_Fee_Entry.get())
                u4 = int(self.Dev_Fee_Entry.get())
                u5 = int(self.Cantine_Fee_Entry.get())
                u6 = int(self.Bus_Fee_Entry.get())
                u7 = int(self.Sports_Fee_Entry.get())
                sum = u2 + u3 + u4 + u5 + u6 + u7
                self.Total_Fee_Entry.insert(0, str(sum))
                self.Total_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterTotalFee(self, event):
        try:
            if self.Total_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Total Fee")
                self.Total_Fee_Entry.focus_set()
            elif int(self.Total_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Total_Fee_Entry.focus_set()
            else:
                self.Fee_Pay_Btn.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def resetNewFeeForm(self):
        self.Admission_Fee_Entry.delete(0, tkinter.END)
        self.Tuition_Fee_Entry.delete(0, tkinter.END)
        self.Dev_Fee_Entry.delete(0, tkinter.END)
        self.Cantine_Fee_Entry.delete(0, tkinter.END)
        self.Bus_Fee_Entry.delete(0, tkinter.END)
        self.Sports_Fee_Entry.delete(0, tkinter.END)
        self.Total_Fee_Entry.delete(0, tkinter.END)
        self.Admission_Fee_Entry.focus_set()

    def onEnterSubmitFee(self,event):
        self.submitStudentAllData()

    def submitStudentAllData(self):
            u1 = int(self.Std_Roll_No_Entry.get())
            u2 = int(self.Admission_Fee_Entry.get())
            u3 = int(self.Tuition_Fee_Entry.get())
            u4 = int(self.Dev_Fee_Entry.get())
            u5 = int(self.Cantine_Fee_Entry.get())
            u6 = int(self.Bus_Fee_Entry.get())
            u7 = int(self.Sports_Fee_Entry.get())
            u8 = int(self.Total_Fee_Entry.get())
            try:
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"update fee set admission_fee = '{u2}', Tution_fee = '{u3}',dev_fee = '{u4}',cantine_fee = '{u5}',bus_fee = '{u6}',sports_fee = '{u7}', total_fee = '{u8}' where roll_no = '{u1}';"
                self.mycursor.execute(q)
                self.myconnect.commit()
                tkinter.messagebox.showinfo("Success", "Save Data successfully")
                self.Add_New_Fee.destroy()
            except MySQLdb.Error as e:
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            finally:
                self.mycursor.close()
                self.myconnect.close()

# -------------------saved data  ------------------------------------------------END ----------------------#

    def updateFee(self):
        self.update_Fee = tkinter.Toplevel(self.master)
        self.update_Fee.title("Register Fee")
        self.update_Fee.geometry("800x500+420+85")
        self.update_Fee.resizable(False, False)

        self.Title_Update_Fee_Label = tkinter.Label(self.update_Fee, text="Update Fee Form:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Update_Fee_Label.place(x=300, y=20)

        self.Update_Std_Roll_No_Label = tkinter.Label(self.update_Fee, text="Student Roll No: ",  font=("bookman old style", 15))
        self.Update_Std_Roll_No_Label.place(x=110, y=90)

        self.Update_Std_Roll_No_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Std_Roll_No_Entry.place(x=390, y=90)
        self.Update_Std_Roll_No_Entry.focus_set()
        self.Update_Std_Roll_No_Entry.bind("<Return>", self.onEnterSearchUpdateStudentRollNo)

        self.Update_Admission_Fee_Label = tkinter.Label(self.update_Fee, text="Admission Fee: ",   font=("bookman old style", 15))
        self.Update_Admission_Fee_Label.place(x=110, y=130)

        self.Update_Admission_Fee_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Admission_Fee_Entry.place(x=390, y=130)
        self.Update_Admission_Fee_Entry.focus_set()
        self.Update_Admission_Fee_Entry.bind("<Return>", self.onEnterUpdateAdmissionFee)

        self.Update_Tuition_Fee_Label = tkinter.Label(self.update_Fee, text="Tuition Fee: ",font=("bookman old style", 15))
        self.Update_Tuition_Fee_Label.place(x=110, y=170)

        self.Update_Tuition_Fee_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Tuition_Fee_Entry.place(x=390, y=170)
        self.Update_Tuition_Fee_Entry.bind("<Return>", self.onEnterUpdateTuitionFee)

        self.Update_Dev_Fee_Label = tkinter.Label(self.update_Fee, text="Development Fee: ",  font=("bookman old style", 15))
        self.Update_Dev_Fee_Label.place(x=110, y=210)

        self.Update_Dev_Fee_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Dev_Fee_Entry.place(x=390, y=210)
        self.Update_Dev_Fee_Entry.bind("<Return>", self.onEnterUpdateDevFee)

        self.Update_Cantine_Fee_Label = tkinter.Label(self.update_Fee, text="Cantine Fee: ",   font=("bookman old style", 15))
        self.Update_Cantine_Fee_Label.place(x=110, y=250)

        self.Update_Cantine_Fee_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Cantine_Fee_Entry.place(x=390, y=250)
        self.Update_Cantine_Fee_Entry.bind("<Return>", self.onEnterUpdateCantineFee)

        self.Update_Bus_Fee_Label = tkinter.Label(self.update_Fee, text="Bus Fee: ",font=("bookman old style", 15))
        self.Update_Bus_Fee_Label.place(x=110, y=290)

        self.Update_Bus_Fee_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Bus_Fee_Entry.place(x=390, y=290)
        self.Update_Bus_Fee_Entry.bind("<Return>", self.onEnterUpdateBusFee)

        self.Update_Sports_Fee_Label = tkinter.Label(self.update_Fee, text="Sports Fee: ", font=("bookman old style", 15))
        self.Update_Sports_Fee_Label.place(x=110, y=330)

        self.Update_Sports_Fee_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Sports_Fee_Entry.place(x=390, y=330)
        self.Update_Sports_Fee_Entry.bind("<Return>", self.onEnterUpdateSportsFee)

        self.Update_Total_Fee_Label = tkinter.Label(self.update_Fee, text="Total Fee: ", font=("bookman old style", 15))
        self.Update_Total_Fee_Label.place(x=110, y=370)

        self.Update_Total_Fee_Entry = tkinter.Entry(self.update_Fee, width=27, font=("bookman old style", 15))
        self.Update_Total_Fee_Entry.place(x=390, y=370)
        self.Update_Total_Fee_Entry.bind("<Return>", self.onEnterUpdateTotalFee)

        self.Update_Std_Fee_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Update_Std_Fee_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Update_Std_Fee_Cancel_img)

        self.Update_Fee_Cancel_Btn = tkinter.Button(self.update_Fee, text="Cancel", width=152, height=30, font=("bookman old style", 15), command=self.resetUpdateStudentFee, bg="#FF7575",fg="white",
                image=self.Update_Std_Fee_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Update_Fee_Cancel_Btn.place(x=390, y=410)

        self.Update_Std_Fee_Pay_img = Image.open("icon/save1.png").resize((26, 26), Image.BOX)
        self.Update_Std_Fee_Pay_img_PhotoImage = ImageTk.PhotoImage(self.Update_Std_Fee_Pay_img)

        self.Update_Fee_Pay_Btn = tkinter.Button(self.update_Fee, text="Pay", width=152, height=30, bg="#ceffcf", font=("bookman old style", 15), command=self.updatesubmitStudentAllData,
                    image=self.Update_Std_Fee_Pay_img_PhotoImage, compound=tkinter.RIGHT)
        self.Update_Fee_Pay_Btn.place(x=550, y=410)
        self.Update_Fee_Pay_Btn.bind("<Return>", self.onEnterUpdateSubmitFee)

        # ----------------Add Fee for New Student Data saved in Database ----------------------------------------------START ------#

    def onEnterSearchUpdateStudentRollNo(self, event):
        self.resetUpdateStudentFee()
        roll_no = self.Update_Std_Roll_No_Entry.get()
        if roll_no == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Roll no")
            self.Update_Std_Roll_No_Entry.focus_set()
        else:
            try:
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"SELECT * FROM fee where roll_no = '{roll_no}';"
                self.mycursor.execute(q)
                row = self.mycursor.fetchall()
                if row == None:
                    tkinter.messagebox.showerror("Error", "Invalid details")
                    self.Update_Std_Roll_No_Entry.focus_set()
                elif len(row) == 0:
                    tkinter.messagebox.showerror("Error", "No Record Found")
                    self.Update_Std_Roll_No_Entry.focus_set()
                else:
                    for count in range(1):
                        name = row[count]
                        self.Update_Admission_Fee_Entry.insert(0, name[2])
                        self.Update_Tuition_Fee_Entry.insert(0, name[3])
                        self.Update_Dev_Fee_Entry.insert(0, name[4])
                        self.Update_Cantine_Fee_Entry.insert(0, name[5])
                        self.Update_Bus_Fee_Entry.insert(0, name[6])
                        self.Update_Sports_Fee_Entry.insert(0, name[7])
            except Exception as ee:
                print(str(ee))
            finally:
                self.mycursor.close()
                self.myconnect.close()
            self.Update_Admission_Fee_Entry.focus_set()

    def onEnterUpdateAdmissionFee(self, event):

        try:
            if self.Update_Admission_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Admission Fee")
                self.Update_Admission_Fee_Entry.focus_set()
            elif int(self.Update_Admission_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Admission_Fee_Entry.focus_set()
            else:
                self.Update_Tuition_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateTuitionFee(self, event):

        try:
            if self.Update_Tuition_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Tuition Fee")
                self.Update_Tuition_Fee_Entry.focus_set()
            elif int(self.Update_Tuition_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Tuition_Fee_Entry.focus_set()
            else:
                self.Update_Dev_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateDevFee(self, event):
        try:
            if self.Update_Dev_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Development Fee")
                self.Update_Dev_Fee_Entry.focus_set()
            elif int(self.Update_Dev_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Dev_Fee_Entry.focus_set()
            else:
                self.Update_Cantine_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateCantineFee(self, event):
        try:
            if self.Update_Cantine_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Cantine Fee")
                self.Update_Cantine_Fee_Entry.focus_set()
            elif int(self.Update_Cantine_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Cantine_Fee_Entry.focus_set()
            else:
                self.Update_Bus_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateBusFee(self, event):
        try:
            if self.Update_Bus_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Bus Fee")
                self.Update_Bus_Fee_Entry.focus_set()
            elif int(self.Update_Bus_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Bus_Fee_Entry.focus_set()
            else:
                self.Update_Sports_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateSportsFee(self, event):
        try:
            if self.Update_Sports_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Sports Fee")
                self.Update_Sports_Fee_Entry.focus_set()
            elif int(self.Update_Sports_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Sports_Fee_Entry.focus_set()
            else:
                u2 = int(self.Update_Admission_Fee_Entry.get())
                u3 = int(self.Update_Tuition_Fee_Entry.get())
                u4 = int(self.Update_Dev_Fee_Entry.get())
                u5 = int(self.Update_Cantine_Fee_Entry.get())
                u6 = int(self.Update_Bus_Fee_Entry.get())
                u7 = int(self.Update_Sports_Fee_Entry.get())
                sum = u2 + u3 + u4 + u5 + u6 + u7
                self.Update_Total_Fee_Entry.insert(0, str(sum))
                self.Update_Total_Fee_Entry.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def onEnterUpdateTotalFee(self, event):
        try:
            if self.Update_Total_Fee_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Total Fee")
                self.Update_Total_Fee_Entry.focus_set()
            elif int(self.Update_Total_Fee_Entry.get()) == 0:
                tkinter.messagebox.showerror("Blank Field", "Please Enter Integer Value")
                self.Update_Total_Fee_Entry.focus_set()
            else:
                self.Update_Fee_Pay_Btn.focus_set()
        except ValueError as ve:
            tkinter.messagebox.showerror("Value Error", "Please Enter Integer Value")
        except Exception as e:
            tkinter.messagebox.showerror("Value Error", str(e))

    def resetUpdateStudentFee(self):
        self.Update_Admission_Fee_Entry.delete(0, tkinter.END)
        self.Update_Tuition_Fee_Entry.delete(0, tkinter.END)
        self.Update_Dev_Fee_Entry.delete(0, tkinter.END)
        self.Update_Cantine_Fee_Entry.delete(0, tkinter.END)
        self.Update_Bus_Fee_Entry.delete(0, tkinter.END)
        self.Update_Sports_Fee_Entry.delete(0, tkinter.END)
        self.Update_Total_Fee_Entry.delete(0, tkinter.END)
        self.Update_Admission_Fee_Entry.focus_set()

    def onEnterUpdateSubmitFee(self, event):
        self.updatesubmitStudentAllData()

    def updatesubmitStudentAllData(self):
        u1 = int(self.Update_Std_Roll_No_Entry.get())
        u2 = int(self.Update_Admission_Fee_Entry.get())
        u3 = int(self.Update_Tuition_Fee_Entry.get())
        u4 = int(self.Update_Dev_Fee_Entry.get())
        u5 = int(self.Update_Cantine_Fee_Entry.get())
        u6 = int(self.Update_Bus_Fee_Entry.get())
        u7 = int(self.Update_Sports_Fee_Entry.get())
        u8 = int(self.Update_Total_Fee_Entry.get())
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"update fee set admission_fee = '{u2}', Tution_fee = '{u3}',dev_fee = '{u4}',cantine_fee = '{u5}',bus_fee = '{u6}',sports_fee = '{u7}', total_fee = '{u8}' where roll_no = '{u1}';"
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.update_Fee.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def deleteFee(self):
        self.Find_Delete_Fee_Window = tkinter.Toplevel(self.master)
        self.Find_Delete_Fee_Window.title("Find Employee")
        self.Find_Delete_Fee_Window.geometry("600x260+420+85")
        self.Find_Delete_Fee_Window.resizable(False, False)

        self.Title_Find_Fee_Label = tkinter.Label(self.Find_Delete_Fee_Window, text="_____Find Details____",  font=("bookman old style", 20, "bold"))
        self.Title_Find_Fee_Label.place(x=130, y=20)

        self.Delete_Student_Fee_Find_Frame = tkinter.LabelFrame(self.Find_Delete_Fee_Window, bg="#EDF5F4")
        self.Delete_Student_Fee_Find_Frame.place(x=20, y=70, height=160, width=550)

        self.Delete_Fee_Student_Roll_No_Label = tkinter.Label(self.Delete_Student_Fee_Find_Frame, text="Roll No: ",  font=("bookman old style", 15))
        self.Delete_Fee_Student_Roll_No_Label.place(x=20, y=20)

        self.Delete_Fee_Student_Roll_No_Entry = tkinter.Entry(self.Delete_Student_Fee_Find_Frame, width=26,font=("bookman old style", 15))
        self.Delete_Fee_Student_Roll_No_Entry.place(x=180, y=20)
        self.Delete_Fee_Student_Roll_No_Entry.focus_set()
        self.Delete_Fee_Student_Roll_No_Entry.bind("<Return>", self.onEnterDeleteFeeStudentRollNoEntry)

        self.Delete_Fee_Student_Find_Cancel_Img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Delete_Fee_Student_Find_Cancel_PhotoImage = ImageTk.PhotoImage(self.Delete_Fee_Student_Find_Cancel_Img)

        self.Delete_Fee_Student_Find_Cancel_Btn = tkinter.Button(self.Delete_Student_Fee_Find_Frame, text="Cancel", width=148, height=30,font=("bookman old style", 15),command=self.restDeleteFeeStudentBTN,
                        image=self.Delete_Fee_Student_Find_Cancel_PhotoImage,compound=tkinter.LEFT)
        self.Delete_Fee_Student_Find_Cancel_Btn.place(x=180, y=60)

        self.Delete_Fee_Student_Find_Img = Image.open("icon/find2.jpg").resize((26, 26), Image.BOX)
        self.Delete_Fee_Student_Find_PhotoImage = ImageTk.PhotoImage(self.Delete_Fee_Student_Find_Img)

        self.Delete_Fee_Student_Find_Btn = tkinter.Button(self.Delete_Student_Fee_Find_Frame, text="Find", width=148, height=30,font=("bookman old style", 15), command=self.empFeeFind,
                                image=self.Delete_Fee_Student_Find_PhotoImage,compound=tkinter.LEFT)
        self.Delete_Fee_Student_Find_Btn.place(x=335, y=60)
        self.Delete_Fee_Student_Find_Btn.bind("<Return>", self.onEnterDeleteFeeStudentRollNoFindBTN)

        self.Delete_Fee_Student_Delete_Img = Image.open("icon/delete.jpg").resize((30, 30), Image.BOX)
        self.Delete_Fee_Student_Delete_PhotoImage = ImageTk.PhotoImage(self.Delete_Fee_Student_Delete_Img)

        self.Delete_Fee_Student_Delete_Btn = tkinter.Button(self.Delete_Student_Fee_Find_Frame, text="Delete", width=301,height=30,font=("bookman old style", 15),command=self.empFeeDelete,
                            image=self.Delete_Fee_Student_Delete_PhotoImage,compound=tkinter.LEFT)
        self.Delete_Fee_Student_Delete_Btn.place(x=180, y=100)
        self.Delete_Fee_Student_Delete_Btn.bind("<Return>", self.onEnterFeeStudentDeleteBtn)

        # ------------------------Find Form Function ----------------------------------END-------------------------------#

        # ----------- all functions ------------------------

    def onEnterDeleteFeeStudentRollNoEntry(self, event):
        if self.Delete_Fee_Student_Roll_No_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Student Roll No")
            self.Delete_Fee_Student_Roll_No_Entry.focus_set()
        else:
            self.Delete_Fee_Student_Find_Btn.focus_set()

    def restDeleteFeeStudentBTN(self):
        self.Delete_Fee_Student_Roll_No_Entry.delete(0, tkinter.END)
        self.Delete_Fee_Student_Roll_No_Entry.focus_set()

    def onEnterDeleteFeeStudentRollNoFindBTN(self, event):
        self.empFeeFind()

    def onEnterFeeStudentDeleteBtn(self, event):
        self.empFeeDelete()

    def empFeeFind(self):
        roll_no = self.Delete_Fee_Student_Roll_No_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM fee where roll_no = '{roll_no}';"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
                self.Delete_Fee_Student_Roll_No_Entry.focus_set()
            elif len(row) == 0:
                tkinter.messagebox.showerror("Error", "Record Not Found")
                self.Delete_Fee_Student_Roll_No_Entry.focus_set()
            else:
                tkinter.messagebox.showinfo("Success", "Record Found")
                self.Delete_Fee_Student_Delete_Btn.focus_set()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def empFeeDelete(self):
        roll_no = self.Delete_Fee_Student_Roll_No_Entry.get()
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"update fee set admission_fee = NULL, Tution_fee = NULL,dev_fee = NULL,cantine_fee = NULL,bus_fee = NULL,sports_fee = NULL, total_fee = NULL where roll_no = '{roll_no}';"
            self.mycursor.execute(q)
            self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Delete successfully")
            self.Find_Delete_Fee_Window.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
            print(e)
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def totalFee(self):
        self.totalFeeCollected = 0

# ---------------List of total Fee collected from the School -----------------------------------START-------------------#

        self.StudentFee_All_List_Window = tkinter.Toplevel(self.master)
        self.StudentFee_All_List_Window.title("List of Total Fee Collected From Student . . .")
        self.StudentFee_All_List_Window.geometry("1200x800+120+85")
        self.StudentFee_All_List_Window.resizable(False, False)

        self.Title_StudentFee_All_List_Label = tkinter.Label(self.StudentFee_All_List_Window, text="List of Total Fee Collected From Student:",
                                                          font=("bookman old style", 20, "underline", "bold"))
        self.Title_StudentFee_All_List_Label.place(x=250, y=20)

        self.StudentFee_All_List_TextArea = tkinter.Text(self.StudentFee_All_List_Window, width=95, height=30,   font=("bookman old style", 15))
        self.StudentFee_All_List_TextArea.place(x=25, y=70)
        try:
            self.itemlist.clear()
            self.StudentFee_All_List_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 5
            s3 = " " * 10
            s4 = " " * 10
            s5 = " " * 11
            s6 = " " * 13
            s7 = " " * 8
            s8 = " " * 8
            s9 = " " * 8
            ItemHead = f"Sno.{s2}Roll No{s4}Total Amount\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = "SELECT * FROM fee;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    if name[3] == None:
                        break
                    else:
                        self.totalFeeCollected += int(name[8])
                        data = (f"{name[0]}.{s7}{name[1]}{s8}Rs.{name[8]}\n")
                        self.itemlist.append(data)
                data = (f"{s1}\nTotal Fee Collected -> Rs.{self.totalFeeCollected}\n{s1}")
                self.itemlist.append(data)
                for item in self.itemlist:
                    self.StudentFee_All_List_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

    # --------------List of total Fee collected from the School---------------------------------END-------------------#

    # ------------------------------------ Area for Fee Structure for Student -----------END----------------------#

# --------------Area for WhatsappMessage -----------------------------------------START --------------------------#
    def whatsappMessage(self):
        self.Add_WA_Message = tkinter.Toplevel(self.master)
        self.Add_WA_Message.title("Messaging . . .")
        self.Add_WA_Message.geometry("800x500+420+85")
        self.Add_WA_Message.resizable(False, False)

        self.Title_WA_Message_Label = tkinter.Label(self.Add_WA_Message, text="Whatsapp Message:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_WA_Message_Label.place(x=250, y=20)

        self.WA_PhoneNo_Label = tkinter.Label(self.Add_WA_Message, text="Phone No: ",font=("bookman old style", 15))
        self.WA_PhoneNo_Label.place(x=110, y=90)

        self.WA_PhoneNo_Entry = tkinter.Entry(self.Add_WA_Message, width=36, font=("bookman old style", 15))
        self.WA_PhoneNo_Entry.place(x=250, y=90)
        self.WA_PhoneNo_Entry.focus_set()
        self.WA_PhoneNo_Entry.bind("<Return>",self.onEnterWAPhoneNo)

        self.WA_Message_Label = tkinter.Label(self.Add_WA_Message, text="Message: ",  font=("bookman old style", 15))
        self.WA_Message_Label.place(x=110, y=130)
        self.WA_Message_TextArea = tkinter.Text(self.Add_WA_Message, width=36,height=10, font=("bookman old style", 15))
        self.WA_Message_TextArea.place(x=250, y=130)

        self.WA_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.WA_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.WA_Cancel_img)

        self.WA_Cancel_Btn = tkinter.Button(self.Add_WA_Message, text="Cancel", width=210, height=30,font=("bookman old style", 15), command=self.resetWAWindow,
                              bg="#FF7575", fg="white",image=self.WA_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.WA_Cancel_Btn.place(x=250, y=373)

        self.WA_Send_img = Image.open("icon/send.png").resize((50, 50), Image.BOX)
        self.WA_Send_PhotoImage = ImageTk.PhotoImage(self.WA_Send_img)

        self.WA_Send_Btn = tkinter.Button(self.Add_WA_Message, text="Send", width=210, height=30, bg="#ceffcf", font=("bookman old style", 15), command=self.sendWAMessage,
                                          image=self.WA_Send_PhotoImage, compound=tkinter.RIGHT)
        self.WA_Send_Btn.place(x=470, y=373)

    def onEnterWAPhoneNo(self,event):
        self.WA_Message_TextArea.focus_set()

    def resetWAWindow(self):
        self.WA_PhoneNo_Entry.delete(0, tkinter.END)
        self.WA_Message_TextArea.delete(1.0,tkinter.END)
        self.WA_PhoneNo_Entry.focus_set()

    def sendWAMessage(self):

        if self.WA_PhoneNo_Entry.get() == "":
            tkinter.messagebox.showerror("Error", "Please Enter Phone Number")
        elif self.WA_Message_TextArea.get(1.0, tkinter.END) == "":
            tkinter.messagebox.showerror("Error", "Please Write Message")
        else:
            u1,u2,u3,u4 = 1,"","","pending"
            try:
                u2 = self.WA_PhoneNo_Entry.get()
                u3 = self.WA_Message_TextArea.get(1.0, tkinter.END)
                phone_no = "+91" + u2
                print("Phone No "+phone_no)
                dt = datetime.datetime.now()
                time = dt.time()
                tt = str(time)
                hh = int(tt[0:2])
                mm = int(tt[3:5])
                mm += 1
                kit.sendwhatmsg(phone_no,u3,hh,mm,15,True, 15)
            except ValueError as e:
                print(str(e))
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            try:
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"insert into wa_message (phone_no, msg, msg_status) values ('{u2}','{u3}', '{u4}');"
                self.mycursor.execute(q)
                self.myconnect.commit()
                tkinter.messagebox.showinfo("Success", "Message Send successfully")
                self.resetWAWindow()
                self.Add_WA_Message.destroy()
            except MySQLdb.Error as e:
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Error {e} ")
            finally:
                self.mycursor.close()
                self.myconnect.close()

# --------------Area for WhatsappMessage -----------------------------------------END --------------------------#
    def smsMessage(self):
        self.Add_SMS_Message = tkinter.Toplevel(self.master)
        self.Add_SMS_Message.title("Messaging . . .")
        self.Add_SMS_Message.geometry("800x500+420+85")
        self.Add_SMS_Message.resizable(False, False)

        self.Title_SMS_Message_Label = tkinter.Label(self.Add_SMS_Message, text="Send Message on Cell Phone:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_SMS_Message_Label.place(x=250, y=20)

        self.SMS_PhoneNo_Label = tkinter.Label(self.Add_SMS_Message, text="Phone No: ",font=("bookman old style", 15))
        self.SMS_PhoneNo_Label.place(x=110, y=90)

        self.SMS_PhoneNo_Entry = tkinter.Entry(self.Add_SMS_Message, width=36, font=("bookman old style", 15))
        self.SMS_PhoneNo_Entry.place(x=250, y=90)
        self.SMS_PhoneNo_Entry.focus_set()

        self.SMS_Message_Label = tkinter.Label(self.Add_SMS_Message, text="Message: ", font=("bookman old style", 15))
        self.SMS_Message_Label.place(x=110, y=130)
        self.SMS_Message_TextArea = tkinter.Text(self.Add_SMS_Message, width=36,height=10, font=("bookman old style", 15))
        self.SMS_Message_TextArea.place(x=250, y=130)

        self.SMS_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.SMS_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.SMS_Cancel_img)

        self.SMS_Cancel_Btn = tkinter.Button(self.Add_SMS_Message, text="Cancel", width=210, height=30, font=("bookman old style", 15), command=self.resetAddNewCustomerForm,
                              bg="#FF7575", fg="white",image=self.SMS_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.SMS_Cancel_Btn.place(x=250, y=373)

        self.SMS_Send_img = Image.open("icon/send.png").resize((50, 50), Image.BOX)
        self.SMS_Send_PhotoImage = ImageTk.PhotoImage(self.SMS_Send_img)

        self.SMS_Send_Btn = tkinter.Button(self.Add_SMS_Message, text="Send", width=210, height=30, bg="#ceffcf", font=("bookman old style", 15), command=self.movetowardsubmit,
                                          image=self.SMS_Send_PhotoImage, compound=tkinter.RIGHT)
        self.SMS_Send_Btn.place(x=470, y=373)

    def sendMail(self):
        self.Send_Email_Window = tkinter.Toplevel(self.master)
        self.Send_Email_Window.title("Mailing . . .")
        self.Send_Email_Window.geometry("800x600+420+85")
        self.Send_Email_Window.resizable(False, False)

        self.Title_Send_Email_Label = tkinter.Label(self.Send_Email_Window, text="Send Message through Email:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Send_Email_Label.place(x=250, y=20)

        self.Email_From_Label = tkinter.Label(self.Send_Email_Window, text="From: ", font=("bookman old style", 15))
        self.Email_From_Label.place(x=80, y=90)

        self.Email_From_Entry = tkinter.Entry(self.Send_Email_Window, width=36, font=("bookman old style", 15))
        self.Email_From_Entry.place(x=250, y=90)
        self.Email_From_Entry.focus_set()

        self.Email_To_Label = tkinter.Label(self.Send_Email_Window, text="To: ", font=("bookman old style", 15))
        self.Email_To_Label.place(x=80, y=130)

        self.Email_To_Entry = tkinter.Entry(self.Send_Email_Window, width=36, font=("bookman old style", 15))
        self.Email_To_Entry.place(x=250, y=130)
        self.Email_To_Entry.focus_set()

        self.Email_Subject_Label = tkinter.Label(self.Send_Email_Window, text="Subject: ",  font=("bookman old style", 15))
        self.Email_Subject_Label.place(x=80, y=170)

        self.Email_Subject_Entry = tkinter.Entry(self.Send_Email_Window, width=36, font=("bookman old style", 15))
        self.Email_Subject_Entry.place(x=250, y=170)
        self.Email_Subject_Entry.focus_set()

        self.Email_Compose_Label = tkinter.Label(self.Send_Email_Window, text="Compose Email: ",   font=("bookman old style", 15))
        self.Email_Compose_Label.place(x=80, y=210)

        self.Email_Compose_TextArea = tkinter.Text(self.Send_Email_Window, width=36, height=10,  font=("bookman old style", 15))
        self.Email_Compose_TextArea.place(x=250, y=210)

        self.Email_Cancel_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Email_Cancel_img_PhotoImage = ImageTk.PhotoImage(self.Email_Cancel_img)

        self.Email_Cancel_Btn = tkinter.Button(self.Send_Email_Window, text="Cancel", width=210, height=30, font=("bookman old style", 15), command=self.resetAddNewCustomerForm,
                          bg="#FF7575", fg="white", image=self.Email_Cancel_img_PhotoImage, compound=tkinter.RIGHT)
        self.Email_Cancel_Btn.place(x=250, y=455)

        self.Email_Send_img = Image.open("icon/emil2.jpg").resize((30, 30), Image.BOX)
        self.Email_Send_PhotoImage = ImageTk.PhotoImage(self.Email_Send_img)

        self.Email_Send_Btn = tkinter.Button(self.Send_Email_Window, text="Send", width=210, height=30, bg="#ceffcf", font=("bookman old style", 15), command=self.movetowardsubmit,
                                           image=self.Email_Send_PhotoImage, compound=tkinter.RIGHT)
        self.Email_Send_Btn.place(x=470, y=455)

# ----------------Show all Messages ------------------------------------------START ------------------------------#

    def showAllMessages(self):

# ----------------Whatsapp Messages List ----------------------------------------------
        self.WA_All_List_Window = tkinter.Toplevel(self.master)
        self.WA_All_List_Window.title("WhatsApp List . . .")
        self.WA_All_List_Window.geometry("1200x800+120+85")
        self.WA_All_List_Window.resizable(False, False)

        self.Title_WA_All_List_Label = tkinter.Label(self.WA_All_List_Window, text="Whatsapp Message List:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_WA_All_List_Label.place(x=250, y=20)

        self.WA_All_List_SearchBox_TextArea = tkinter.Text(self.WA_All_List_Window, width=95,height=30, font=("bookman old style", 15))
        self.WA_All_List_SearchBox_TextArea.place(x=25, y=70)
        try:
            self.itemlist.clear()
            self.WA_All_List_SearchBox_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 3
            s3 = " " * 5
            s4 = " " * 5
            s5 = " " * 3
            s6 = " " * 3
            ItemHead = f"ID.{s2}Phone No{s3}Status{s4}Message\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM wa_message;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    data = (f"{name[0]}.{s2}{name[1]}{s5}{name[3]}{s6}{name[2]}")
                    self.itemlist.append(data)
                for item in self.itemlist:
                    self.WA_All_List_SearchBox_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

# ----------------SMS List ----------------------------------------------
        self.SMS_All_List_Window = tkinter.Toplevel(self.master)
        self.SMS_All_List_Window.title("SMS List . . .")
        self.SMS_All_List_Window.geometry("1200x800+220+185")
        self.SMS_All_List_Window.resizable(False, False)

        self.Title_SMS_All_List_Label = tkinter.Label(self.SMS_All_List_Window, text="SMS List:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_SMS_All_List_Label.place(x=250, y=20)

        self.SMS_All_List_SearchBox_TextArea = tkinter.Text(self.SMS_All_List_Window, width=95,height=30, font=("bookman old style", 15))
        self.SMS_All_List_SearchBox_TextArea.place(x=25, y=70)
        try:
            self.itemlist.clear()
            self.SMS_All_List_SearchBox_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 3
            s3 = " " * 5
            s4 = " " * 5
            s5 = " " * 3
            s6 = " " * 3
            ItemHead = f"ID.{s2}Phone No{s3}Status{s4}Message\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM sms_message;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    data = (f"{name[0]}.{s2}{name[1]}{s5}{name[3]}{s6}{name[2]}")
                    self.itemlist.append(data)
                for item in self.itemlist:
                    self.SMS_All_List_SearchBox_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

# ----------------Emai List ----------------------------------------------
        self.Email_All_List_Window = tkinter.Toplevel(self.master)
        self.Email_All_List_Window.title("Email List . . .")
        self.Email_All_List_Window.geometry("1200x800+420+285")
        self.Email_All_List_Window.resizable(False, False)

        self.Title_Email_All_List_Label = tkinter.Label(self.Email_All_List_Window, text="Email List:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_Email_All_List_Label.place(x=250, y=20)

        self.Email_All_List_SearchBox_TextArea = tkinter.Text(self.Email_All_List_Window, width=95,height=30, font=("bookman old style", 15))
        self.Email_All_List_SearchBox_TextArea.place(x=25, y=70)

        try:
            self.itemlist.clear()
            self.Email_All_List_SearchBox_TextArea.delete("1.0", tkinter.END)
            s1 = "-" * 100
            s2 = " " * 3
            s3 = " " * 3
            s4 = " " * 3
            s5 = " " * 3
            s6 = " " * 3
            s7 = " " * 25
            s8 = " " * 25
            ItemHead = f"ID.{s2}Status{s3}From{s7}To{s8}Message\n{s1}\n"
            self.itemlist.append(ItemHead)
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"SELECT * FROM email;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for count in range(len(row)):
                    name = row[count]
                    data = (f"{name[0]}.{s2}{name[5]}{s3}{name[1]}{s4}{name[2]}{s5}{name[4]}")
                    self.itemlist.append(data)
                for item in self.itemlist:
                    self.Email_All_List_SearchBox_TextArea.insert(tkinter.END, str(item))
        except Exception as ee:
            print(str(ee))
        finally:
            self.mycursor.close()
            self.myconnect.close()

# ----------------Show all Messages ------------------------------------------END --------------------------------#

# -----------------Area of Setting for Student in the School--------------------------------START-------------------#

    def addNewUser(self):
        self.Add_New_User = tkinter.Toplevel(self.master)
        self.Add_New_User.title("Add User Form")
        self.Add_New_User.geometry("800x500+420+85")
        self.Add_New_User.resizable(False, False)

        self.Title_Add_New_UserLabel = tkinter.Label(self.Add_New_User, text="Add User Form:", font=("bookman old style", 20, "underline", "bold"))
        self.Title_Add_New_UserLabel.place(x=300, y=20)

        self.Add_New_User_Label = tkinter.Label(self.Add_New_User, text="New Employee Type: ", font=("bookman old style", 15))
        self.Add_New_User_Label.place(x=80, y=60)

        self.Add_New_User_Entry = tkinter.Entry(self.Add_New_User, width=38, font=("bookman old style", 15))
        self.Add_New_User_Entry.place(x=300, y=60)
        self.Add_New_User_Entry.focus_set()
        self.Add_New_User_Entry.bind("<Return>",self.onEnterAddNewUser)

        self.UserList_Label = tkinter.Label(self.Add_New_User, text="List of Employees: ",  font=("bookman old style", 15))
        self.UserList_Label.place(x=80, y=100)

        self.AddNew_UserList = tkinter.Listbox(self.Add_New_User,selectmode=tkinter.MULTIPLE, width=38, height=13, font=("bookman old style", 15))
        self.AddNew_UserList.place(x=300, y=100)

        self.AddNewUser_Delete_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.AddNewUser_Delete_PhotoImage = ImageTk.PhotoImage(self.AddNewUser_Delete_img)


        self.AddNew_Delete_Btn = tkinter.Button(self.Add_New_User, text="Delete", width=220, height=30, font=("bookman old style", 15), command=self.deleteNewUser, bg="#FF7575",
                                fg="white",image=self.AddNewUser_Delete_PhotoImage, compound=tkinter.RIGHT)
        self.AddNew_Delete_Btn.place(x=300, y=425)

        self.AddNewUser_Add_img = Image.open("icon/add.jpg").resize((26, 26), Image.BOX)
        self.AddNewUser_Add_PhotoImage = ImageTk.PhotoImage(self.AddNewUser_Add_img)

        self.AddNewUser_Add_Btn = tkinter.Button(self.Add_New_User, text="Add", width=220, height=30, bg="#ceffcf", font=("bookman old style", 15), command=self.SaveAddNewEmployee,
                                          image=self.AddNewUser_Add_PhotoImage, compound=tkinter.RIGHT)
        self.AddNewUser_Add_Btn.place(x=530, y=425)

    # ----------------Add Fee for New Student Data saved in Database ----------------------------------------------START ------#

    def onEnterAddNewUser(self, event):

            if self.Add_New_User_Entry.get() == "":
                tkinter.messagebox.showerror("Blank Field", "Please Enter Add New Employee Type")
                self.Add_New_User_Entry.focus_set()
            else:
                a = self.Add_New_User_Entry.get()
                self.AddNew_UserList.insert(tkinter.END,a)
                self.Add_New_User_Entry.delete(0, tkinter.END)
                self.Add_New_User_Entry.focus_set()

    def deleteNewUser(self):
        selected_items = self.AddNew_UserList.curselection()
        if not selected_items:
            tkinter.messagebox.showwarning("Selection Error", "Please select an item in the list to remove.")
        for index in selected_items[::-1]:
            self.AddNew_UserList.delete(index)
            tkinter.messagebox.showinfo("Success", "Delete Successfully")
        self.Add_New_User_Entry.focus_set()

    def SaveAddNewEmployee(self):
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            l = self.AddNew_UserList.size()
            for i in range(0,l):
                item = self.AddNew_UserList.get(i)
                q = f"insert into stafflist(stafftype) values('{item}');"
                self.mycursor.execute(q)
                self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.Add_New_User.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        finally:
            self.mycursor.close()
            self.myconnect.close()

    def updateUser(self):
        self.Update_User = tkinter.Toplevel(self.master)
        self.Update_User.title("Update User Form")
        self.Update_User.geometry("800x500+420+85")
        self.Update_User.resizable(False, False)

        self.Title_Update_UserLabel = tkinter.Label(self.Update_User, text="Update User Form:",font=("bookman old style", 20, "underline", "bold"))
        self.Title_Update_UserLabel.place(x=300, y=20)

        self.Update_User_Label = tkinter.Label(self.Update_User, text="Employee Type: ",font=("bookman old style", 15))
        self.Update_User_Label.place(x=80, y=60)

        self.Update_User_Entry = tkinter.Entry(self.Update_User, width=38, font=("bookman old style", 15))
        self.Update_User_Entry.place(x=300, y=60)
        self.Update_User_Entry.focus_set()
        self.Update_User_Entry.bind("<Return>", self.onEnterUpdateUserEntry)

        self.Update_UserList_Label = tkinter.Label(self.Update_User, text="List of Employees: ",font=("bookman old style", 15))
        self.Update_UserList_Label.place(x=80, y=100)

        self.Update_UserList = tkinter.Listbox(self.Update_User, selectmode=tkinter.MULTIPLE, width=38, height=13,font=("bookman old style", 15))
        self.Update_UserList.place(x=300, y=100)

# -----------------Area to get Details-------------------------------------------------START -------------------
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"select * from  stafflist;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Invalid details")
            else:
                for i in range(len(row)):
                    name = row[i]
                    self.Update_UserList.insert(i, name[1])
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        finally:
            self.mycursor.close()
            self.myconnect.close()

        # ----------------Area to get Details------------------------------END----------------------#

        self.Update_User_Delete_img = Image.open("icon/cancel13.png").resize((26, 26), Image.BOX)
        self.Update_User_Delete_PhotoImage = ImageTk.PhotoImage(self.Update_User_Delete_img)

        self.Update_Delete_Btn = tkinter.Button(self.Update_User, text="Delete", width=220, height=30,font=("bookman old style", 15), command=self.deleteUpdateUser,
                                                    bg="#FF7575",fg="white",image=self.Update_User_Delete_PhotoImage, compound=tkinter.RIGHT)
        self.Update_Delete_Btn.place(x=300, y=425)

        self.Update_User_Add_img = Image.open("icon/add.jpg").resize((26, 26), Image.BOX)
        self.Update_User_Add_PhotoImage = ImageTk.PhotoImage(self.Update_User_Add_img)

        self.Update_User_Add_Btn = tkinter.Button(self.Update_User, text="Update", width=220, height=30, bg="#ceffcf",font=("bookman old style", 15), command=self.SaveUpdateUser,
                                                     image=self.Update_User_Add_PhotoImage, compound=tkinter.RIGHT)
        self.Update_User_Add_Btn.place(x=530, y=425)

    # ----------------Add Fee for New Student Data saved in Database ----------------------------------------------START ------#

    def onEnterUpdateUserEntry(self, event):

        if self.Update_User_Entry.get() == "":
            tkinter.messagebox.showerror("Blank Field", "Please Enter Employee Type")
            self.Update_User_Entry.focus_set()
        else:
            a = self.Update_User_Entry.get()
            self.Update_UserList.insert(tkinter.END, a)
            self.Update_User_Entry.delete(0, tkinter.END)
            self.Update_User_Entry.focus_set()

    def deleteUpdateUser(self):
        selected_items = self.Update_UserList.curselection()
        if not selected_items:
            tkinter.messagebox.showwarning("Selection Error", "Please select an item in the list to remove.")
        for index in selected_items[::-1]:
            self.Update_UserList.delete(index)
            tkinter.messagebox.showinfo("Success", "Delete Successfully")
        self.Update_User_Entry.focus_set()

    def SaveUpdateUser(self):
        try:
            self.myconnect = Conn.Conn.makeConnection(Conn)
            self.mycursor = self.myconnect.cursor()
            q = f"select * from  stafflist;"
            self.mycursor.execute(q)
            row = self.mycursor.fetchall()
            if row == None:
                tkinter.messagebox.showerror("Error", "Rows Empty")
            else:
                for i in range(len(row)):
                    q = f"update stafflist set stafftype = NULL WHERE id = '{i + 1}';"
                    self.mycursor.execute(q)
                    self.myconnect.commit()
            l = self.Update_UserList.size()
            for i in range(0, l):
                item = self.Update_UserList.get(i)
                q = f"update stafflist set stafftype = '{item}' WHERE id = '{i+1}';"
                self.mycursor.execute(q)
                self.myconnect.commit()
            tkinter.messagebox.showinfo("Success", "Save Data successfully")
            self.Update_User.destroy()
        except MySQLdb.Error as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error {e} ")
        finally:
            self.mycursor.close()
            self.myconnect.close()

        # -----------------Area of Setting for Student in the School-------------------------------END----------------------#

if __name__=="__main__":
    main()