import tkinter
import tkinter.messagebox

class emailValidation:
    def __init__(self):
        pass


    def email_textfield_validation(self,email):

        '''
        Conditions  1# Email minimum length 6 character
                    2# Email contains first letter is only character
                    3# Email contains only one @ symbol
                    4# Email designed for only .in or .com domain only
                    5# Email doesn't contain space or special symbol or upper case letter

        '''
           
        self.email = email
        #self.email = input("Enter your Email: ")  # minimum email format -> #g@g.in or 6 character

        k,j,d = 0,0,0

        if len(email) >= 6:
            if email[0].isalpha():
                if ("@" in email) and (email.count("@") == 1):
                    if (email[-4] == ".") ^ (email[-3] == "."):
                        for i in email:
                            if i == i.isspace():
                                k = 1

                            elif i.isalpha():
                                if i == i.upper(): # change small case character into upper case character
                                    j = 1

                            elif i.isdigit():
                                continue

                            elif i == "_" or i == "." or i == "@":
                                continue

                            else:
                                d = 1
                        if k == 1 or j == 1 or d == 1:
                            tkinter.messagebox.showerror("Email format Error", " Email doesn't contain space or other symbol ")
                            #print(" Wrong Email 5") # email doesn't contain space or other symbol or not upper case character

                        else:
                            tkinter.messagebox.showinfo("Email format Correct", " Email validation successful ")
                           # print("Right Email") # email follows all conditions


                    else:
                        tkinter.messagebox.showerror("Email format Error", " Email designed for '.in' and '.com' ")
                        #print(" Wrong Email 4") # email contains "." for .in [-3] for .com in [-4]

                else:
                    tkinter.messagebox.showerror("Email format Error", " Email contains only one @ symbol")
                    #print(" Wrong Email 3") # email contains only one @

            else:
                tkinter.messagebox.showerror("Email format Error", " Email contains first character is alphabet")
               # print(" Wrong Email 2") # email contains first character is alphabet

        else:
            tkinter.messagebox.showerror("Email format Error"," Email contains minimum 6 character")
            #print("wrong email 1") # email contains minimum 6 character