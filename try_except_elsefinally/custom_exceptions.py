class NameTooShortError(ValueError):
    pass
    

def validate(name):
    if len(name) < 8:
        raise NameTooShortError('Name is too short')
    
username= input('enter your name..')
validate(username)
print(f"hello {username}")
