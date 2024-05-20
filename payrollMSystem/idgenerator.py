import MySQLdb
import Conn

myconnect = Conn.Conn.makeConnection(Conn)
mycursor = myconnect.cursor()

# ------------------Employee No generator ----------------------------START ----------#
def empNoGenerator(max_Emp_Size):
        max_Emp_Size = int(max_Emp_Size)

        for count in range(1,max_Emp_Size,1):
            emp_No = f"emp000{count}"
            try:
                q = f"insert into employee (emp_no) values ('{emp_No}');"
                mycursor.execute(q)
                myconnect.commit()

                q = f"insert into salary (emp_no) values ('{emp_No}');"
                mycursor.execute(q)
                myconnect.commit()

            except MySQLdb.Error as e:
                print("Error", f"Error {e} ")

            except Exception as e:
                print("Error", f"Error {e} ")

def stdRollNoGenerator(max_Std_size):
        max_Std_size = int(max_Std_size)

        for count in range(1, max_Std_size, 1):

            roll_No = f"202400{count}"
            try:
                q = f"insert into student (roll_no) values ('{roll_No}');"
                mycursor.execute(q)
                myconnect.commit()

                q = f"insert into attendence (roll_no) values ('{roll_No}');"
                mycursor.execute(q)
                myconnect.commit()

                q = f"insert into fee (roll_no) values ('{roll_No}');"

                mycursor.execute(q)
                myconnect.commit()

            except MySQLdb.Error as e:
                print("Error", f"Error {e} ")

            except Exception as e:
                print("Error", f"Error {e} ")

# -------------------Insert data into the Database -------------------END -------------#
