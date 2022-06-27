import mysql.connector as connector
class Db:
    def __init__(self):
        self.con =connector.connect(
                                   host="localhost",
                                   user="root",
                                   passwd="shubhakshi",
                                   database="second"
        )
        
        query = 'create table if not exists user(userId int primary key, userName varchar(100),contact varchar(11))'
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        
    def insert_into(self,userId, userName, contact):
        query= "insert into user (userId, userName, contact) values ('{}','{}','{}')".format(userId, userName, contact)
        cur = self.con.cursor()
        cur.execute(query)
        print(query)
        self.con.commit()

    def fetch_data(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
        #    print(row)
           print("ID: ", row[0])
           print("Name: ", row[1])
           print("contact: ",row[2])
        print(query)
        
    def delete_row(self,userId):
        query ="delete from user where userId ={}".format(userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        
    def update(self, userId, newName):
        query = "update user set userName ='{}' where userId={}".format(newName,userId)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        
    
if __name__ == "__main__":
    print(__name__)
    db = Db()
    db.fetch_data()
   