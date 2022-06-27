import mysql.connector as connector

mydb = connector.connect(
    host ="localhost",
    user = "root",
    passwd = "shubhakshi",
    database = "first"
)

cur = mydb.cursor()
#cur.execute("select * from tab1")
# sqlformula = "insert into tab1 (id, name, project, years, company) values(%s, %s, %s, %s, %s)"
# #mydb.commit()
# val1 =[(1027,"ann", "trainee", 2, "arcgate"),
#        (1024,"tim", "manager", 8, "tcs"),
#        (1025,"kat", "executive", 7, "tcs"),
#        (1029,"em", "executive", 6, "arcgate"),
#        (1030,"ray", "trainee", 3, "startup"),
#        (1028,"tom", "executive", 7, "startup"),
#        (1031,"nat", "manager", 9, "tcs"),
#        ]
#cur.executemany(sqlformula, val1)

##searching
# sql = "select * from tab1 where company like '%s'"
# cur.execute(sql)
# result = cur.fetchall()
# for row in result:
#     print(row)

##view
#cur.execute("update tab1 set name='sam' where id =1021")
# cur.execute("select * from tab1 limit 4 offset 2")
# cur.execute("select * from [tabview]")
# result = cur.fetchall()
# for row in result:
#     print (row)
# #mydb.commit()

cur.execute("show databases")
