# step 1:
import mysql.connector as c
con=c.connect(
    host='localhost',
    user='root',
    password='Shubham@2525',
    database='JulyPython'
)
# if con.is_connected:
#     print('success')
# else:
#     print('kuch to gadbad hai ')
cursor=con.cursor()
# cursor.execute(' create database JulyPython')
# cursor.execute(' create table Emp(eid int, ename varchar(20))')
# cursor.execute('show tables')
# for i in cursor:
#     print(i)

# qury='insert into emp(eid, ename) values(%s,%s)'
# value=(1, 'Rahul')
# value==[(17, 'ABD'),(18, 'Virat', (45, 'Rohit'))]
# cursor.executemany(qury,value)
# print(cursor.rowcount,'Afected')
# con.commit()

# cursor.execute('select*from emp')
# d=cursor.fetchone()
# d=cursor.fetchall()
# print(d)
# for i in d:
#     print(i)

# q='update emp set ename=%s where eid=%s'
# val=[('smriti',18),('komal',45)]
# cursor.execute(q,val)
# cursor.executemany(q,val)
# print(cursor.rowcount, 'Is Afected')
# con.commit()

qd='delete from emp where eid=%'
val=(45)
cursor.executemany(qd,val)
con.commit()
print(f'{cursor.rowcount} Row is Afected..')

tq='truncate table emp'
cursor.executemany(tq)
con.close()