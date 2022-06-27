import mysql.connector
# import os
# os.system("clear")  

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shubhakshi",
    database= "second"
    
)
cur=db.cursor()

class Recipe_book:
    # def __init__(self,recipe_list, libname):
    #     self.recipe=recipe_list
    #     self.libname=libname
    #     self.recipe_book = set()
    #     print(f"----{libname}----\n")
 #functions to be defined
 #add recipe
 #show recipe
 #take back your recipe(delete)

    def add_recipe(self):
       cook =input("enter creator's name")
       recipe=input("enter the name of recipe")
       time=input("mention cook time in minutes")
       query="insert into recipe_book (recipe, creator, cook_time) values('{}','{}',{})".format(recipe, cook,time)
       cur.execute(query)
       db.commit()
      
        
    def takeback_recipe(self):
      recipe = input("what do you want to remove").lower()
      try:
        query="DELETE FROM recipe_book where recipe='{}'".format(recipe)
        cur.execute(query)
        db.commit()
        print('you have removed your recipe')
        print('--------------------------------------')
      except:
            print('Recipe you want to remove doesn\'t exist')
            
    def look_recipe(self):
    
        print('here is the list or recipes available')
        query= "SELECT recipe from recipe_book"
        cur.execute(query)
        book = cur.fetchall()
        for row in book:
            print( row[0])
        
        

obj=Recipe_book()

work_var = True
while work_var:
    print("""--------- Welcome to the Recipe-World--------------- 
          what do you want to do??
          press      FOR\n
          1          Add recipe
          2          Remove Recipe
          3          list Recipe
          """ )
    user_input= int(input('enter your choice---  '))
    if user_input == 1:
        obj.add_recipe()
        print('--------')
        
    elif user_input == 2:
        obj.takeback_recipe()
        print('----------') 
        
    elif user_input ==3:
        obj.look_recipe()
        
    else:
        print('please enter a valid code')
        
    to_quit  = input('To quit press q\n press any key to continue:\n')
    to_quit.strip()
    to_quit.lower()
    
    if to_quit=='q':
       work_var = False
    else:
        continue
    