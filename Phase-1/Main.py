import mysql.connector
from datetime import datetime
from datetime import time
from datetime import timedelta
from Buffer import Buffer
from Cl import CL
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



# while loop for unlimited re-attempts
testValue = 1
while testValue == 1:
    def clear(): 
	    if name == 'nt':
		    _ = system('cls') 
	    else: 
		    _ = system('clear') 

    for x in range(100):
        print('_', end=' ')
    print("""\n
        Welcome To DSU Attendance System !!! ---  Current Time is """,ctime,"\n")
    employeeID = int(input("          Enter your employee ID: "))
    my_select_query = "Select * from details where ssn=%s"
    mycursor.execute(my_select_query, (employeeID,))
    if (ctime > cl_time):
        CL(employeeID,mycursor)
    else:
        Buffer(employeeID,mycursor)
    sleep(5) 
    clear() 