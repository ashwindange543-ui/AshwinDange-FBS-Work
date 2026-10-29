# from hr import Hr
# from dev import Dev
# class EmpManage:
#     Empdetil={}
#     def addEmp(self):
#         eid=input("Enter  Emp Id ")
#         if eid in EmpManage.Empdetil:
#             print("Employee is Aalredy Exist...")
#             return
#         else:
#             ename=input("Enter the EMp  Name= ")
#             esal=float(input("Eneter Emp  sal "))
#             print("1.Hr")
#             print("2.Devloper ")
#             ch=int(input("Enter the Choice= "))
#             if ch==1:
#                 ecom=float(input("enter the com of Hr= "))
#                 emp=Hr(eid,ename,esal,ecom)
#             elif ch==2:
#                 bonus=float(input("enter the Bonus of Dev= "))
#                 emp=Dev(eid,ename,esal,bonus)
#             else:
#                 print("Inavaldi choice ")
#                 return
#             EmpManage.Empdetil[eid]=emp
#             print("Emp added sussefully....")
#     def displyEmp(self):
#         if len(EmpManage.Empdetil)==0:
#             print("Emp is not Exist,..... ")
#         else:
#             for var in EmpManage.Empdetil.values():
#                 print(var)
                
#     def searchEmp(self):
#         eid=input("Eneter the id of Eployee to serch employee ")
#         if eid in EmpManage.Empdetil:
#             print(EmpManage.Empdetil[eid])
#         else:
#             print("Employee is not Exist.... ")
            
#     def UpdateEmp(self):
#         eid=input("Eneter the id of Eployee to serch employee ")
#         if eid not in EmpManage.Empdetil:
#             print("Employee not found,....")
#             return
#         else:
#             emp=EmpManage.Empdetil[eid]
#             print("1.Update Dev ")
#             print("2.Update Hr")
#             ch=int(input("Enter the Choice= "))
#             if ch==1 and isinstance(emp,Dev):
#                 newname=input("Eneter new name of Dev")
#                 emp.setName(newname)
#             elif ch==2 and isinstance(emp,Hr):
#                  newname=input("Eneter new name of Hr")
#                  emp.setName(newname)
#             else:
#                 print("Type miamathed oR Inavalid input")
                
        
        
        
#     def deleteEmp(self):
#          eid=input("Eneter the id of Eployee to serch employee ")
#          if eid in EmpManage.Empdetil:
#              del EmpManage.Empdetil[eid]
#              print("Employee deleted susefully....")
#          else:
#             print("Employee is not avaialable")


import mysql.connector  as ct
from hr import Hr
from dev import Dev
class EmpManage:
    @staticmethod
    def getConection():
        con=ct.connect(
            host='localhost',
            user='root',
            password="root123",
            database="employee_db"
        )
        return con
    def addEmp(self):
       eid=input("Enter  Emp Id ")
       con=EmpManage.getConection()
       cur=con.cursor()
       cur.execute("select eid from employees where eid=%s",(eid,))
       if cur.fetchone():
           print("Employee is alredy exist... ")
           cur.close()
           con.close()
       else:
            ename=input("Enter the name of Employee ")
            esal=float(input("Enter the Sal of Employee "))
            print("1.Hr ")
            print("2.Devloper  ")
            ch=int(input("Enter your choice    "))
            if ch==1:
                extra=float(input("Enter the Com of Hr "))
                emp_type="HR"
            elif ch==2:
                extra=float(input("Enter the Bonus of  Devloper  "))
                emp_type="Dev"
            else:
                print("Inavalic choice...  ")
                cur.close()
                con.close()
            qur="insert into employees (eid,ename,esal,emp_type,extra_amount) values(%s,%s,%s,%s,%s)" 
            cur.execute(qur,(eid,ename,esal,emp_type,extra))
            con.commit()
            print("Employee added suseesfully..... ")
            cur.close()
            con.close()
    def displyEmp(self):
        con=EmpManage.getConection()
        cur=con.cursor()
        cur.execute("select * from employees ")
        row=cur.fetchall()
        if not row:
           print("No one is here...")
        else:
            for r in row:
                print(r)
        cur.close()
        con.close()
    def searchEmp(self):
       eid=input("Eneter the id of Eployee to serch employee ")
       con=EmpManage.getConection()
       cur=con.cursor()
       cur.execute('select * from employees where eid=%s',(eid,))
       row=cur.fetchone()
       if row:
           print(row)
       else:
           print("Employee with this  id is not exist..")
           cur.close()
           con.close()
         
    def UpdateEmp(self):
        eid=input("Enter  Emp Id ")
        con=EmpManage.getConection()
        cur=con.cursor()
        cur.execute("select eid from employees where eid=%s",(eid,))
        row=cur.fetchone()
        if not row:
            print("Emp is not  found... ")
            cur.close()
            con.close()
            return
        emp_type=row[0]
        print("1>Update  Devloper")
        print("2>Update  HR")
        ch=int(input("enter the choice"))
        if ch==1 and emp_type=="Dev":
            newname=input("enter the Name of Devloper to update ")
        elif ch==2 and emp_type=="HR":
            newname=input("enter the Name of HR to update ")
        else:
            print("Type ,issamatch or inavlid input")
            cur.close()
            con.close()
            return
        cur.execute("update employees set ename=%s where eis=%s",(newname,eid))
        con.commit()
        print("Employee update ho gaya bhaii ")
        cur.close()
        con.close()
    def deleteEmp(self):
        eid=input("Enter  Emp Id ")
        con=EmpManage.getConection()
        cur=con.cursor()
        cur.execute("select eid from employees where eid=%s",(eid,))
        row=cur.fetchone()
        if not row:
            print("Emp is not  found... ")
            cur.close()
            con.close()
            return
        else:
            cur.execute("delete from employees where eid=%s",(eid,))
            con.commit()
            print("Employee deleted susesfully ")
            cur.close()
            con.close()
            return