import mysql.connector as connector

mydb = connector.connect(
    host ="localhost",
    user = "root",
    passwd = "shubhakshi",
    database = "second"
)

cur = mydb.cursor(buffered=True)

## join 
# cur.execute("select user.userName, contact, employee.age from user inner join employee on employee.name=user.userName ")
     
# mydb.commit()
# result= cur.fetchall()
# for row in result:
#       print(row)
      
##sort
# cur.execute("select * from user order by userId desc limit 6 offset 2")
# mydb.commit()
# result=cur.fetchall()
# for row in result:
#     print (row)
