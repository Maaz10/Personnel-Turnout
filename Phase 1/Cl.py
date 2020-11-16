"""
-------------------------------Pre-Requisits ---------------------------
Pre Processing.py File must be run Before running this file to Initialize a Test Case
Run the Below Comands:
->create database miniproject
->create table details (ssn int primary key, name varchar(20) , punchIn varchar(30) , bufferTime int , NoOfCl int);
Install mysql library pip install mysql-connector-python
"""

# import Mysql library
import mysql.connector
from datetime import datetime
from datetime import time
from datetime import timedelta
from Buffer import Buffer
from os import system, name 
from time import sleep
#Connection To Database Server
mydb = mysql.connector.connect(
    host="localhost", user="root", password="12345", database="miniproject")
mycursor = mydb.cursor()

#Get current ime in Y-M-D H:M:S.F format
ytime = datetime.now()
xy = str(ytime)
current_time = ytime.strptime(xy, "%Y-%m-%d  %H:%M:%S.%f")
hor = current_time.hour
mins = current_time.minute
secs = current_time.second
#Changed From Ytime to Ctime as datetime and time delta values structures
ctime = default_College_Time = timedelta(
    hours=hor, minutes=mins, seconds=secs)  # time object

cl_time = timedelta(hours=10, minutes=45, seconds=00)

def CL(employeeID,mycursor):
    
        

        for x in mycursor:
            cl = x[-2]
            if cl > 0:

                # Decrease CL
                cl -= 1
                print("           Cl is deducted")
                sql = ("Update details set Noofcl =%s where ssn=%s")
                mycursor.execute(sql, (cl, employeeID,))
                print("           remaining CL is :", cl)

            else:

                # Deduct Salary after Cl becomes 0 and Refresh Cl
                print(
                    "           No cl left in the account\n           Salary deducted\n\n")
                sal = x[-1]
                sal -= 1
                sql = ("Update details set salary_decrease =%s where ssn=%s")
                mycursor.execute(sql, (sal, employeeID,))
                cl = 15
                sql = ("Update details set Noofcl =%s where ssn=%s")
                mycursor.execute(sql, (cl, employeeID,))
        for i in mycursor:
            print(i)
        
