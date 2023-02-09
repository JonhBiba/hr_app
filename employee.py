import mysql.connector as mysql
#connecting with my mysql server
con = mysql.connect(
    host="localhost", user="root", password="", database="hr-g6")
c = con.cursor()
#connect pycharm with mysql database
def Display_Employees(employee_id):
    sql = "SELECT * FROM `employee` WHERE Employee_Code =(%s)"
#connecting with mysql to run a command
    data = (employee_id,)
    c.execute(sql, data)
    r = c.fetchall()
#show all the employees from the table
    print(r)
#Display a Employees from mysql database
def Add_Employee():
    Name = input('First Name : ')
    email = input('Email : ')
    phone = input('Phone Number : ')
    address = input('Your Address : ')
    salary = input('Your Salary : ')
#the inputs for the adding progress
    data = [Name, email, phone, address, salary]
    sql = 'INSERT INTO `employee`( `Name`, `email`, `phone`, `Address`, `Salary`) VALUES (%s,%s,%s,%s,%s)'
    c.execute(sql, data)
    con.commit()
#run execute for adding item and human
    print("Employee Added Successfully ")
    menu()
#Add a Employee from mysql database
def Remove_Employ(employee_id):
        sql = 'DELETE FROM `employee` WHERE Employee_Code =(%s)'
        data = (employee_id,)
        c.execute(sql, data)
        con.commit()
        print("Employee Removed")
        menu()
#Remove a Employee from mysql database
def Promote_Employee(employee_id, salary):
    sql = 'UPDATE employee SET Salary = (%s) WHERE Employee_Code =(%s)'
    data = [salary, employee_id]
    c.execute(sql, data)
    con.commit()
    print("Employee Promoted")
    menu()
#Promote a Employee from mysql database
def Edit_Employee(Name, email, phone, address, employee_id):
    sql =  "UPDATE `employee` SET `Name`= (%s) ,`email`= (%s) ,`phone`= (%s) ,`Address`= (%s)  WHERE Employee_Code = (%s)"
    data = [Name, email, phone, address, employee_id]
    c.execute(sql, data)
    con.commit()
    print("Employee Edited")
    menu()
#Edit a Employee from mysql database
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to edit Employee")
    print("6 to Exit")
    ch = int(input("Enter your Choice "))
#asking what the human want to change,add and more
    if ch == 1:
        Add_Employee()
#calling Add Employee
    elif ch == 2:
        employee_id = str(input("give employee ID"))
        Remove_Employ(employee_id)
#calling Remove Employee
    elif ch == 3:
        employee_id = str(input("give employee ID"))
        Display_Employees(employee_id)
        salary = str(input('give the new salary'))
        Promote_Employee(employee_id, salary)
#calling Promote Employee
    elif ch == 4:
        employee_id = str(input("give employee ID"))
        Display_Employees(employee_id)
#calling Display Employees
    elif ch == 5:
        employee_id = str(input("give employee ID"))
        Display_Employees(employee_id)
        Name  = str(input("give new full name"))
        email = str(input("give new email"))
        phone = str(input("give new phone"))
        address = str(input("give new address"))
        Edit_Employee(Name, email, phone, address, employee_id)
#calling Edit Employee
    elif ch == 6:
        exit(0)
#using exit command
    else:
        print("Invalid Choice")
        menu()
menu()
