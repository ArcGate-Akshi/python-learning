import mysql.connector as connector

mydb = connector.connect(
    host ="localhost",
    user = "root",
    passwd = "shubhakshi",
    database = "first"
)

cur = mydb.cursor()
## auto increment 
#cur.execute("alter table student modify id INT NOT NULL PRIMARY KEY AUTO_INCREMENT")
# mydb.commit()


# sqlformula = "insert into student (firstName, lastName, age, skills) values( %s, %s, %s, %s)"
# val1 =[("ann","mark" , 22, "python"),
#        ("tim", "musk", 28, "JS"),
#        ("kat", "stark", 23, "python"),
#        ("em", "green", 22, "angular"),
#        ("ray", "antone", 23, "flask"),
#        ("tom", "", 27, "oracle"),
#        ("nat", "mark", 28, "django"),
#        ]
# cur.executemany(sqlformula, val1)
# mydb.commit()

## create indexing
# cur.execute("alter table student add index personIndex(firstName) ") 
cur.execute("select * from student where id=106")
result = cur.fetchall()
print(result)