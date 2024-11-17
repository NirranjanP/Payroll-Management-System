import mysql.connector
import datetime
from tabulate import tabulate

db=input('Enter name of database: ')

mydb=mysql.connector.connect(host='localhost',user='root',passwd='siva3-673306')
mycursor=mydb.cursor()

sql='CREATE DATABASE if not exists %s' % (db,)
mycursor.execute(sql)
print('Database created Successfully...')
mycursor=mydb.cursor()
mycursor.execute("Use "+db)
TableName=input("Name of Table to be created: ")
query=("CREATE TABLE "+TableName+ "\
(empno INT PRIMARY KEY,\
name VARCHAR(15) not null,\
job VARCHAR(15),\
BasicSalary INT,\
DA FLOAT,\
HRA FLOAT,\
GrossSalary FLOAT,\
Tax FLOAT,\
Netsalary FLOAT)")
print('Table ' +TableName+ ' created successfully...')
mycursor.execute(query)

while True:
    print('\n\n\n')
    print('*'*95)
    print('\t\t\t\t\tMAIN MENU')
    print('*'*95)
    print('\t\t\t\t1. Adding Employee records')
    print('\t\t\t\t2. For Displaying Records of All the Employees')
    print('\t\t\t\t3. For Displaying Record of a particular Employee')
    print('\t\t\t\t4. For Deleting Records of All the Employees')
    print('\t\t\t\t5. For Deleting a Record of a particular Employee')
    print('\t\t\t\t6. For Modificaion in a Record')
    print('\t\t\t\t7. For Displaying payroll')
    print('\t\t\t\t8. For Displaying Salary Slip for all Employees')
    print('\t\t\t\t9. For Displaying Salary Slip for a particular Employees')
    print('\t\t\t\t10. For Exit')
    print('Enter Choice...',end='')
    choice=int(input())
    if choice==1:
        try:
            print('Enter Employee Information.....')
            mempno=int(input('Enter Employee No:'))
            mname=input('Enter Employee Name:')
            mjob=input('Enter employee Job:')
            mbasic=float(input('Enter basic salary:'))
            if mjob.upper()=='OFFICER':
                mda=mbasic*0.5
                mhra=mbasic*0.25
                mtax=mbasic*0.2
            elif mjob.upper()=='MANAGER':
                mda=mbasic*0.45
                mhra=mbasic*0.35
                mtax=mbasic*0.15
            elif mjob.upper()=='SOFTWARE DELEVOPER':
                mda=mbasic*0.40
                mhra=mbasic*0.30
                mtax=mbasic*0.8
            elif mjob.upper()=='WEBDELEVOPER':
                mda=mbasic*0.35
                mhra=mbasic*0.28
                mtax=mbasic*0.8
            elif mjob.upper()=='SOWTWARE DELEVOPER':
                mda=mbasic*0.40
                mhra=mbasic*0.30
                mtax=mbasic*0.8
            else:
                mda=mbasic*0.28
                mhra=mbasic*0.15
                mtax=mbasic*0.4
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            query='insert into'+TableName+'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,rec)

            mydb.commit()
            print('Record added successfully....')
        except Exception as e:
            print('Something went wrong',e)

            
    elif choice==2:
        try:
            query='select * from'+TableName
            mycursor.execute(query)
            #print(query)
            print(tabulate(mycursor, headers=['Empno','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'],tablefmt='fancy_grid'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
                print(rec)'''
        except:
            print('Something went wrong')
    elif choice==3:
        try:
            en=input('Enter Employee no. of the record to be Displayed...')
            query='select * from'+TableName+'where Empno='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print('\n\nRecord of Employee No.:'+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                print('Nothing to Display')
        except:
            print('Something went wrong')


    elif choice==4:
        try:
            ch=input('Do you want to delete all the records(y/n)')
            if ch.upper()=='y':
                mycursor.execute('delete from '+TableName)
                mydb.commit()
                print('All the records are Deleted...')
        except:
            print('Something went wrong')


    elif choice==5:
        try:
            en=input('Enter Employee no. of the record to be Deleted....')
            query='Deleted from '+TableName+' where Empno='+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print('Deletion Done')
            else:
                print('Employee no ',en,' not found')
        except:
            print('Something went wrong')


    elif choice==6:
        try:
            en=input('Enter Employee no. of the record to be modified...')
            query='select * from'+TableName+'where Empno='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('Empno '+en+' does not exist')
            else:
                mName=myrecord[1]
                mJob=myrecord[2]
                mBasic=myrecord[3]
                print('Empno  :',myrecord[0])
                print('Name   :',myrecord[1])
                print('Job    :',myrecord[2])
                print('Basic  :',myrecord[3])
                print('DA     :',myrecord[4])
                print('HRA    :',myrecord[5])
                print('Gross  :',myrecord[6])
                print('Tax    :',myrecord[7])
                print('Net    :',myrecord[8])
                print('----------------------------------------------------------------------------')
                print('Type Value to modify below or just press enter for no change')
                x=input('Enter Name')
                if len(x)>0:
                    mName=x
                x=input('Enter Job')
                if len(x)>0:
                    mJob=x
                x=input('Enter Basic Salary')
                if len(x)>0:
                    mbasic=float(x)
                query='update '+TableName+' set name='+"'"+mName+"'"+','+'Job='+"'"+mJob+"'"+','+'Basicsalary='+str(mBasic)+' where Empno='+en
                print(query)
                mycursor.execute(query)
                myb.commit()
                print('Record modified')
        except:
            print('Something went wrong')

    elif choice==7:
       try:
           query='select * from'+TableName
           mycursor.execute(query)
           myrecord=mycursor.fetchall()
           print("\n\n\n")
           print(95*'*')
           print('Employee Payroll'.cener(90))
           print(95*'*')
           now=datetime.datetime.now()
           print('Current Date and Time:',end='')
           print(now.strftime('%Y-%m-%d-%H:%M:%S'))
           print()
           print(95*'-')
           print('%-5s %-15s %-10s %-8s %-8s %-8 %-9s %-8s %-9s'\
              %('Empno','Name','Job','Basic','DA','HRA','Gross','Tax','Net'))
           print(95*'-')
       except:
           print('Something went wrong')


    elif choice==8:
       try:
           query='select * from '+TableName
           mycursor.execute(query)
           now=datetime.datetime.now()
           print("\n\n\n")
           print(95*'-')
           print("\t\t\t\tSalary Slip")
           print(95*'-')
           print('Current Date and Time:',end='')
           print(now.strftime('%Y-%m-%d-%H:%M:%S'))
           myrecord=mycursor.fetchall()
           for rec in myrecords:
               print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
       except:
           print('Something went wrong')

    elif choice==9:
       try:
           en=input('Enter employee number whose pay slip you want to retreive:')
           query='Deleted from '+TableName+' where Empno='+en
           mycursor.execute(query)
           now=datetime.datetime.now()
           print("\n\n\n\t\t\t\tSalary Slip")
           print('Current Date and Time:',end='')
           print(now.strftime('%Y-%m-%d-%H:%M:%S'))
           #print(query)
           print(tabylate(mycursor, headers=['Empno','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'],tablefmt='psql'))

       except Exception as e:
           print('Something went wrong',e)

    elif choice==10:
        break
else:
    print('Wrong Choice...')
        
        
        
