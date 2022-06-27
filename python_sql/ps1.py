#creating connection to database

import mysql.connector

  
mydb = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="shubhakshi",
  database = "second"
  )
 
mycursor = mydb.cursor()
# # mycursor.execute("show tables")
# # for tb in mycursor:
# #      print(tb)
# sqlformula = "insert into employee (name, age) values(%s, %s)"
# emp1 = [("kat", 24),
#         ("em", 23),
#         ("tim", 25),
#         ("ray", 24),
#         ("nat", 22),
#         ]
# mycursor.executemany (sqlformula, emp1)

mycursor.execute("select * from employee")
result= mycursor.fetchone()
# for row in result:
      # print(row)
print(result)      
mydb.commit()
  
# Disconnecting from the server
#dataBase.close()
