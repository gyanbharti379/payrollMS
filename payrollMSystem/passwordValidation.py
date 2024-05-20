import tkinter
import tkinter.messagebox
import re

class passValidation:
    def __init__(self):
        pass


    def password_passfield_validation(self,password):

        '''
        Conditions  1# Password contain minimum length 8 character and maximum 20 character
                    2# Password contains At least 1 letter between [A-Z] and 1 letter between [a-z]
                    3# Password contains At least 1 number
                    4# Password contains At least 1 symbol from [$#@!]

        '''

        self.pwd = password
        pwd_len = len(self.pwd)
        print(pwd_len)
        is_valid = False

        while True: #infinite loop for checking the password stirng
            if pwd_len < 8 or pwd_len > 20:
                tkinter.messagebox.showerror("Password Validation . . .", "Password contains min: 7 amd max:20 character")
                break

            elif not re.search('[A-Z]',self.pwd):
                tkinter.messagebox.showerror("Password Validation . . .", "Password contains At least one character between [A-Z]")
                break

            elif not re.search('[a-z]', self.pwd):
                tkinter.messagebox.showerror("Password Validation . . .", "Password contains At least one character between [a-z]")
                break

            elif not re.search('[0-9]',self.pwd):
                tkinter.messagebox.showerror("Password Validation . . .", "Password contains At least one number between [0-9]")
                break

            elif not re.search('[$#@!]', self.pwd):
                tkinter.messagebox.showerror("Password Validation . . .","Password contains At least one symbol between [$#@!]")
                break
            elif re.search('\s',self.pwd):
                tkinter.messagebox.showerror("Password Validation . . .","Password contains wide space character")
                break
            else:
                is_valid = True
                break
        if is_valid:
            tkinter.messagebox.showinfo("Password Validation . . .", "Entered password is Valid")
            #print("Password is valid")


