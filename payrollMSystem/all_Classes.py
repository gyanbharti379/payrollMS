class login:
    def __init__(self):
        self.utype = ""
        self.username = ""
        self.userpass = ""
        self.owenerName = ""
        self.companyName = ""
        self.maxEmployee = 0
        self.maxStudent = 0

    def LoginForm(self):
        pass

class Staff:
    def __init__(self):
        self.emp_no = ""
        self.emp_type = ""
        self.Appoint_in_Class =""
        self.Appoint_in_Department =""
        self.First_Name = ""
        self.Last_Name = ""
        self.gender = ""
        self.email_id = ""
        self.phone_no = ""
        self.date_of_joining = ""
        self.date_of_leave = ""
        self.address = ""
        self.city = ""
        self.state = ""

class Student:
    def __init__(self):
        self.roll_no = ""
        self.First_Name = ""
        self.Last_Name = ""
        self.gender = ""
        self.Admission_in_class = ""
        self.date_of_Admission = ""
        self.gardian_Phone_no = ""
        self.address = ""
        self.city = ""
        self.state = ""


class Fee:
    def __init__(self):
        self.roll_no = ""
        self.Admission_Fee = 0
        self.Tuition_Fee = 0
        self.Dev_Fee = 0
        self.Cantine_Fee = 0
        self.Bus_Fee = 0
        self.Sports_fee = 0
        self.Total_Fee = 0

class Salary:
    def __init__(self):
        self.Emp_No = ""
        self.Ta = 0
        self.Da = 0
        self.Hra = 0
        self.Med = 0
        self.Pf = 0
        self.Basic_Salary = 0
        self.Total_Salary = 0

#-------------Teacher Section ------START----#

class Teacher(Staff,Salary):

    def takeAttendance(self):
        self.Roll_No = ""
        self.Today_Date = ""
        self.First_Half = ""
        self.Second_Half = ""

    def createReminders(self):
        self.Date_of_Reminder = ""
        self.Appoint_in_Class = ""
        self.Reminder_Message = ""
        self.Reminder_Status = ""


    def teacherSchedule(self):
        self.Appoint_in_Class = ""
        self.Teacher_Name = ""
        self.Day = ""
        self.Time = ""
        self.Subject = ""


    def showListofStudent(self):
        self.First_Name = ""
        self.Last_Name = ""
        self.gender = ""
        self.Admission_in_class = ""
        self.gardian_Phone_no = ""
        self.address = ""
        self.city = ""
        self.state = ""
#-------------Teacher Section ------END----#

class OtherStaff(Staff,Salary):
        pass

#-------------Clerk Section ------START----#

class Clerk(Staff):

# -----------Employee --------------START------#
    def AddEmployee(self):
        pass

    def UpdateEmployee(self):
        pass


    def AddSalary(self):
        pass

    def UpdateSalary(self):
        pass

    def employeeFine(self):
        pass
# ---------Employee ------------END -----------#

#----------Student ------------START ----------#
    def addStudence(self):
        pass

    def updateStudent(self):
        pass

    def addFee(self):
        pass

    def updateFee(self):
        pass


    def studentFine(self):
        self.Fine_Name = ""
        self.Fine_Amount = 0
        self.Fine_Status = "Active/Deactive"

# -----------Student ----------END ------------#

#-------------Clerk Section ------END----#

class Admin(Staff):

# ----------CreateUser --------START-------#
    def createUser(self):
        self.Staff_Type = ""

    def updateUser(self):
        self.Staff_Type = ""

    def deleteUser(self):
        self.Staff_Type = ""

    def showUser(self):
        self.Staff_Type = ""

# ----------CreateUser --------END-------#

#----------Notification --------START-------#
    def createNotification(self):
        self.utype = ""
        self.notif_message = ""
        self.notif_status = ""

    def showNotification(self):
        self.utype = ""
        self.notif_message = ""
        self.notif_status = ""

#----------Notification --------END-------#

# ----------Message --------START-------#
    def createMessage(self):
        self.Phone_no =""
        self.Message = ""
        self.Message_Status = ""

    def showMessage(self):
        self.Phone_no = ""
        self.Message = ""
        self.Message_Status = ""

# ----------Message --------END-------#

# ----------WhatsAppMessage --------START-------#
    def createWAMessage(self):
        self.Phone_no = ""
        self.Message = ""
        self.Message_Status = ""

    def showWAMessage(self):
        self.Phone_no = ""
        self.Message = ""
        self.Message_Status = ""
# ----------WhatsAppMessage --------END-------#

# ----------Email --------START-------#
    def createEmails(self):
        self.Email_From = ""
        self.Email_To = ""
        self.Email_Subject = ""
        self.Email_Message = ""
        self.Email_Status = ""

    def showEmails(self):
        self.Email_From = ""
        self.Email_To = ""
        self.Email_Subject = ""
        self.Email_Message = ""
        self.Email_Status = ""

# ----------Email --------END-------#

# --------Show Salary Details ---------#
    def ShowAllSalaryDetails(self):
        pass

# --------Show Fee Details -----------#
    def showAllFeedetails(self):
        pass


# --------Show Salary Details ---------#
    def ShowAllEmployeeFineDetails(self):
        pass

# --------Show Fee Details -----------#
    def ShowAllStudentFineDetails(self):
        pass

# ----------Delete Employee -----------#
    def DeleteEmployee(self):
        self.Employee_Status = "Active/Deactive"

# ---------Delete Student ------------#
    def deleteStudent(self):
        self.Student_Status = "Active/Deactive"

#-----------Student Atendence details ------------#
    def showAttendanceList(self):
        pass

    def showListofStudentallClasses(self):
        self.First_Name = ""
        self.Last_Name = ""
        self.gender = ""
        self.Admission_in_class = ""
        self.date_of_Admission = ""
        self.gardian_Phone_no = ""
        self.address = ""
        self.city = ""
        self.state = ""

    def ShowAllEmployeeDetails(self):
        pass



