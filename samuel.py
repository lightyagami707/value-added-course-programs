from tabulate import tabulate
import pymysql
con=pymysql.connect(host="localhost",user='root',password="root",db="samuel")
def insert(name,age,city,salary,department,gender):
    res=con.cursor()
    sql="insert into student(name,age,city,salary,department,gender)values(%s,%s,%s,%s,%s,%s)"
    user=(name,age,city,salary,department,gender)
    res.execute(sql, user)
    con.commit()
    print("data inserted sucess")
   
def update(age,city,salary,department,gender):
    res=con.cursor()
    sql="update student set age=%s,city=%s,salary=%s,department=%s,gender=%s where name=%s"
    user=(age,city,salary,department,gender)
    res.execute(sql,user)
    con.commit()
    print("data updated")
def select():
    res=con.cursor()
    sql="select * from student"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["NAME","AGE","CITY","SALARY","DEPARTMENT","GENDER"]))
def delete(name):
    res=con.cursor()
    sql="delete from student where name=%s"
    user=(name)
    res.execute(sql,user) 
    con.commit()
while True :
    print("1.insert\n2.update\n3.select\n4.delete")
    a=int(input("enter the operation you want to do")) 
    if a==1:
        name=input("enter the name:")
        age=int(input("enter the age:"))
        city=input("enter the city:")
        salary=int(input("enter the salary:"))
        department=input("enter the department:")
        gender=input("enter the gender:")
        insert(name,age,city,salary,department,gender)
    elif a==2:
        c=int(input("enter the age:"))
        d=input("enter the city:")
        e=int(input("enter the salary:"))
        f=input("enter the department:")
        g=input("enter the gender:")
        update(c,d,e,f,g)
    elif a==3:
        select()
    elif a==4:
        b=input("enter the name:")
        delete(b)
    else:
        print("enter the correct option")
        break
con.close()
