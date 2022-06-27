# name userid phone citycode
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='shubhakshi',
    database='information'
)
mycursor = mydb.cursor()


class User:

    # def __init__(self,name,contact,citycode, userid):
    #     self.name=name
    #     self.userid=userid
    #     self.contact=contact
    #     self.citycode=citycode

    def add_user(self):
        name = input('enter name')
        phone = int(input('enter contact number'))
        code = int(input('enter city code'))
        query = "insert into user(name, contact, citycode) values('{}',{},{})".format(
            name, phone, code)
        mycursor.execute(query)
        mydb.commit()

    def removeuser(self):
        id = int(input('enter unique id'))
        query = "DELETE from user where userid={}".format(id)
        mycursor.execute(query)
        mydb.commit()

    def update_name(self):
        id = int(input("enter id to update name"))
        new_name = input("enter updated name")
        query = "UPDATE user set name='{}' where userid = {}".format(
            new_name, id)
        mycursor.execute(query)
        mydb.commit()

    def update_phone(self):
        id = int(input("enter id to update contact"))
        new_num = int(input("enter updated number"))
        query = "UPDATE user set contact = {} where userid={}".format(
            new_num, id)
        mycursor.execute(query)
        mydb.commit()

    def update_city(self):
        id = int(input("enter id to update city"))
        new_code = int(input("enter updated city code"))
        query = "UPDATE user set citycode={} where userid={}".format(
            new_code, id)
        mycursor.execute(query)
        mydb.commit()

    def showtable(self):
        query = "select * from user"
        mycursor.execute(query)
        book = mycursor.fetchall()
        for row in book:
            print(row)


p = User()
contact = True
while contact:
    print("""---------Contact-Book--------------- 
          what do you want to do??
          press      FOR\n
          1          Add user
          2          Remove user
          3          update name
          4          update contact
          5          update city code
          6          show contact book
          7          exit
          """)
    user_input = int(input('enter your choice---  '))
    if user_input == 1:
        p.add_user()
        print('---user added to contact book-----')
    elif user_input == 2:
        p.removeuser()
        print("----user removed-----")
    elif user_input == 3:
        p.update_name()
        print("updated name")
    elif user_input == 4:
        p.update_phone()
        print("updated contact")
    elif user_input == 5:
        p.update_city()
        print("updated city")
    elif user_input == 6:
        p.showtable()
        print("Contact BOOK")
    elif user_input == 7:
        contact = False
    else:
        print("enter valid code")

    to_quit = input('To quit press q\n press any key to continue:\n')
    to_quit.strip()
    to_quit.lower()

    if to_quit == 'q':
        contact = False
    else:
        continue
