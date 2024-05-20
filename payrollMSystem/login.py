import sys
import tkinter
import tkinter.ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import hashlib

def main():
    Login()

class Login:

    def __init__(self):

# ------------------Area for creating window -------------------------------START --------------------------

        self.master = tkinter.Tk()
        self.master.title("Payroll Management System")
        self.master.geometry("800x500+350+110")
        self.master.config(bg="#FEFDFE")
        img = Image.open("icon/iconwin.png")
        ImageLabel = ImageTk.PhotoImage(img)
        self.master.iconphoto(True,ImageLabel)
        self.master.resizable(False,False)
        self.master.bind("<Destroy>", self.on_close)

# ------------------Area for creating window --------------------------------END---------------------------

# ------------------Add widget to window -----------------------------------START--------------------------

        img_bg = Image.open("images/logi.jpg").resize((800,500),Image.BOX)
        Photo_Image_bg = ImageTk.PhotoImage(img_bg)

        self.Background_Label = tkinter.Label(self.master, image=Photo_Image_bg)
        self.Background_Label.place(x=0,y=0)

        self.user_Name_Entry = tkinter.Entry(self.master, width=21,font=("bookman old style", 15))
        self.user_Name_Entry.place(x=475, y=250)
        self.user_Name_Entry.focus_set()
        self.user_Name_Entry.bind("<Return>",self.onEnterUserName)

        self.password_Entry = tkinter.Entry(self.master, width=21, show="*", font=("bookman old style", 15))
        self.password_Entry.place(x=475, y=302)
        self.password_Entry.bind("<Return>",self.onEnterPasword)

        self.register_btn_img = Image.open("icon/registerimage.png").resize((30,30),Image.BOX)
        self.register_Photo_Login_Img = ImageTk.PhotoImage(self.register_btn_img)
        self.Register_BTN = tkinter.Button(self.master, text="Register",  width=122, font=("bookman old style", 15), command=self.register, image=self.register_Photo_Login_Img, compound=tkinter.LEFT,   bg="#ffe28a", fg="red")
        self.Register_BTN.place(x=475, y=350)

        self.Login_btn_img = Image.open("icon/login.png").resize((30,30),Image.BOX)
        self.Photo_Login_Img = ImageTk.PhotoImage(self.Login_btn_img)
        self.Login_btn = tkinter.Button(self.master, text="Login",  width=120, font=("bookman old style", 15),  command=self.checkEntryValidation, image=self.Photo_Login_Img, compound=tkinter.LEFT,   bg="#ffe28a", fg="red")
        self.Login_btn.place(x=605, y=350)
        self.Login_btn.bind("<Return>", self.onEnterLogInBtn)

        self.Forget_Password = tkinter.Label(self.master,text="Forget Password?",font=("bookman old style", 8),  fg="red")
        self.Forget_Password.place(x=475, y=395)

        self.Forget_Password_Click_Here = tkinter.Label(self.master,text="Click Here!",font=("bookman old style", 8))
        self.Forget_Password_Click_Here.place(x=590, y=395)

# ------------------Add widget to window --------------------------------------END ----------------------------

        self.master.mainloop()

# -------------Other Functions -----------------------------------------------START --------------------------

    def on_close(self, event):
        self.master.quit()

    def onEnterUserName(self, event):
        self.password_Entry.focus_set()

    def onEnterPasword(self, event):
        self.Login_btn.focus_set()


    def onEnterLogInBtn(self, event):
        self.checkEntryValidation()


    def checkEntryValidation(self):
        if  self.user_Name_Entry.get() == "":
                tkinter.messagebox.showerror("Error", "Please fill User Id")
                self.user_Name_Entry.focus_set()
        elif self.password_Entry.get() == "":
                tkinter.messagebox.showerror("Error", "Please fill Password")
                self.password_Entry.focus_set()
        else:
                self.check_User_Authentication()

    def check_User_Authentication(self):

        us = self.user_Name_Entry.get().lower()
        pp = self.password_Entry.get()
        try:
                import Conn
                self.myconnect = Conn.Conn.makeConnection(Conn)
                self.mycursor = self.myconnect.cursor()
                q = f"SELECT * FROM login where username= '{us}';"
                self.mycursor.execute(q)
                row = self.mycursor.fetchone()
                if row == None:
                    tkinter.messagebox.showerror("Error", "Invalid details")
                    self.resetallfields()
                elif row[3] == hashlib.sha256(pp.encode()).hexdigest():
                    self.master.destroy()
                    import UserDashboard
                    UserDashboard.UserDashboard.userName = row[1]
                    UserDashboard.UserDashboard.usertype = row[2]
                    UserDashboard.main()
                    self.resetallfields()
                else:
                    tkinter.messagebox.showerror("Login . . .","Login Failed")
        except Exception as ee:
                print(str(ee))
        finally:
                self.mycursor.close()
                self.myconnect.close()

    def register(self):
                try:
                    self.master.destroy()
                    import SignUP
                    a = SignUP
                    a.RegistrationEntryForm()

                except Exception as e:
                    print(str(e))

    def forgetidandpassword(self, event):
                try:
                        self.master.destroy()
                        import ForgetPassword
                        ForgetPassword.main()
                except Exception as e:
                        print(str(e))

    def resetallfields(self):
                self.user_Name_Entry.delete(0, tkinter.END)
                self.password_Entry.delete(0, tkinter.END)
                self.user_Name_Entry.focus_set()

if __name__ =="__main__":
    main()
