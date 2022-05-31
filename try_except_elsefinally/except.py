#division problem

def divide(a,b):
    try:
     return a/b
    except ZeroDivisionError as err:
        print(err)
        #print('you cannot divide with zero')
    except TypeError as err:
        print(err)
    except:
        print('unexpected error')    
 
print(divide('y' ,0))
