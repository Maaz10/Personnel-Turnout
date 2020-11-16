"""
-------------------------------Pre-Requisits ---------------------------
Pre Processing.py File must be run Before running this file to Initialize a Test Case
Run the Below Comands:
->create database miniproject
->create table details (ssn int primary key, name varchar(20) , punchIn varchar(30) , bufferTime int , NoOfCl int);
Install mysql library pip install mysql-connector-python
"""

#Import sql library
import mysql.connector

class personal_info:
    emp_id= int(input("Enter Employee ID: "))
    name=str(input("Enter Name: "))
    phone_no=str(input("Enter Phone Number: "))
    address=str(input("Enter Address: "))
    department=str(input("Enter Department: "))
    designation=str(input("Enter Designation: "))

    def sqlcommand(self,table_name,value_space,a,b,c,d,e,f=None):
        SQLCommand =  table_name + " values(%s,%s,%s,%s,%s" + value_space + ")"
        if not f:
            values=[a,b,c,d,e]
        else:
            values=[a,b,c,d,e,f]
        mycursor.execute(SQLCommand,values)
        mydb.commit()

print("Enter Employee Details")    
p1=personal_info()

#Connection with database
mydb = mysql.connector.connect(host="localhost", user="root", password="12345",database="miniproject")
mycursor = mydb.cursor()
#Take Inputs

table_name="INSERT INTO employee_details"
value_space= ",%s"
p1.sqlcommand(table_name,value_space,p1.emp_id,p1.name,p1.phone_no,p1.address,p1.department,p1.designation)

buffertime=120
punchin='08:45'
no_of_cl=15
salary_decrease=0

table_name="INSERT INTO punchin_details"
value_space= "1"
p1.sqlcommand(table_name,value_space,p1.emp_id,punchin,buffertime,no_of_cl,salary_decrease)

print("Data Successfully Inserted")
mydb.close()