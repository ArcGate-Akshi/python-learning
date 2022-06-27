#menu driven program
#using funct from sql_comm

from sql_comm import Db
def main():
    db=Db()
    while True:
        print("""press code to choose action:
            code         action
            1            insert user
            2            display data
            3            delete user
            4            update data
            5            exit"""
            )
        
        try:
            choice=int(input())
            if choice ==1:
                id= int(input("enter id"))
                name = input('enter name')
                phone=input("enter contact")
                db.insert_into(id,name,phone)
               
            elif choice ==2:
               db.fetch_data()
               
            elif choice ==3:
                id = int(input('enter id to delete row'))
                db.delete_row(id)
                
            elif choice ==4:
                id = int(input("enter id to updtae name"))
                name=input("enter new name")
                db.update(id,name)
            elif choice ==5:
                break
            else:
                print('invalid input')
        except Exception as e:
            print(e)
            print("invalid detail")
            
if __name__ =="__main__":
    main()
    
    
                
            