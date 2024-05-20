import MySQLdb
import Conn

myconnect = Conn.Conn.makeConnection(Conn)
mycursor = myconnect.cursor()

empno = ""
def getEmpNoinEmployeeTable():
    for count in range(1, 100, 1):

        try:

            #q = f"select emp_no from employee where id='{count}' and f_name='';"
            q = f"select emp_no from employee where id='{count}' and f_name is NULL;"

            mycursor.execute(q)
            row = mycursor.fetchone()

            if row == None:

                continue
            else:
                print(row[0])
                empno = row[0]
                break

        except MySQLdb.Error as e:
            print("Error", f"Error {e} ")

        except Exception as e:
            print("Error", f"Error {e} ")

    return empno

def getEmpNoinSalaryTable():
    for count in range(1, 100, 1):

        try:

            #q = f"select emp_no from employee where id='{count}' and f_name='';"
            q = f"select emp_no from salary where id='{count}' and total_sal is NULL;"

            mycursor.execute(q)
            row = mycursor.fetchone()

            if row == None:

                continue
            else:
                print(row[0])
                empno = row[0]
                break

        except MySQLdb.Error as e:
            print("Error", f"Error {e} ")

        except Exception as e:
            print("Error", f"Error {e} ")

    return empno

def getRollNoinStudentTable():
    for count in range(1, 100, 1):

        try:

            q = f"select roll_no from student where id='{count}' and f_name is NULL;"

            mycursor.execute(q)
            row = mycursor.fetchone()

            if row == None:
                continue
            else:
                print(row[0])
                empno = row[0]
                break

        except MySQLdb.Error as e:
            print("Error", f"Error {e} ")

        except Exception as e:
            print("Error", f"Error {e} ")

    return empno


def getRollNoinFeeTable():
    for count in range(1, 100, 1):

        try:

            q = f"select roll_no from fee where id='{count}' and total_fee is NULL;"

            mycursor.execute(q)
            row = mycursor.fetchone()

            if row == None:
                continue
            else:
                print(row[0])
                empno = row[0]
                break

        except MySQLdb.Error as e:
            print("Error", f"Error {e} ")

        except Exception as e:
            print("Error", f"Error {e} ")

    return empno
