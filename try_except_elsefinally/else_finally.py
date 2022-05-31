while True:
    try:
        num = int(input("enter number..."))
      
    except ValueError:
        print("you haven\'t entered int")
    except:
        print('unexpected error')
    else:          #else blocks runs when try block runs and there are no exceptions
        print(f'user input {num}')
        break
    finally:  #it runs every time wven with exceptions
        print('final block')
        