class Mobile:
    def __init__(self,name):
        self.name = name
        
class Mobile_store:
    def __init__(self):
        self.mobile = []
        
    def add_model(self,new_model):
        if isinstance(new_model, Mobile):
            self.mobile.append(new_model)
        else:
            raise TypeError('new mobile should be object of mobile class')

oneplus=Mobile('one plus 6') #object
samsung = 'samsung galaxy S8' #string
storeObject=Mobile_store()    #object of mobile store class
storeObject.add_model(oneplus)
newphone = storeObject.mobile
print(newphone[0].name)
