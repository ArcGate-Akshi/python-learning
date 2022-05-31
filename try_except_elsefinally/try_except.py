while True:  
    try:
        age = int(input('enter your age...  '))
        break
    except ValueError: 
        print('do not enter string')
    except:
        print('unexpected error')
    
    
if age < 18:
    print('you can\'t play this game')
else:
    print('let\'s start the game')
    