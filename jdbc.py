import mysql.connector as mcon

mydb=mcon.connect(host='localhost', password='abc@1234', user='root')
if mydb.is_connected():
    print(mydb,"Connected...")

mycursor=mydb.cursor()

def _show():
    print("<Showing Databases>")
    mycursor.execute("show databases")
    for i in mycursor:
        print(i)

def _create():
    d_name= input("Enter database name: ")
    mycursor.execute(f"create database if not exists {d_name}")
    print(f"Created {d_name}")

def _use():
    d_name= input("Enter database name: ")
    mycursor.execute(f"use {d_name}")
    print(f"Using {d_name}")
    mycursor.execute("create table if not exists student (roll int primary key, name varchar(50), city varchar(50))")

def _insert():
    print()
    roll=int(input("Enter roll no: "))
    name=(input("Enter name: "))
    city=(input("Enter city: "))
    ### mycursor.execute("insert into student values({a},'{b}','{c}')".format(a=roll,b=name,c=city))
    mycursor.execute(f"insert into student values({roll},'{name}','{city}')")

def _read():
    mycursor.execute("select * from student")
    for i in mycursor:
        print(i)

def _update():
    roll=int(input("Enter roll no of student: "))
    name=(input("Enter new name: "))
    city=(input("Enter new city: "))
    mycursor.execute(f"update student set name='{name}', city='{city}'where roll='{roll}'")

def _delete():
    roll=int(input("Enter roll no of student: "))
    mycursor.execute(f"delete from student where roll={roll}")

while True:
    print("\n\n")
    print("0.Show DB\t1.CreateDB\t2.Insert\t3.Update\n"+"4.Delete\t5.Use DB\t6.Read\t\t7.Exit")
    ch=int(input("Enter choice (0-7): "))
    print("\n\n")
    if ch==0:
        _show()
    if ch==1:
        _create()
    if ch==2:
        _insert()
    if ch==3:
        _update()
    if ch==4:
        _delete()
    if ch==5:
        _use()
    if ch==6:
        _read()
    if ch==7:
        print("<Existing>")
        break