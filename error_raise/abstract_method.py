#raise error(NotImplementedError)
#abstract method

class Animal:
    def __init__(self,name):
        self.name=name
        
    def sound(self):
        raise NotImplementedError ('define this method in subclasses')
   
class Dog(Animal):
    def __init__ (self,name,breed):
      super().__init__(name)
      self.breed=breed
      
    def sound(self):
        return 'woof'
    
class Cat(Animal):
    def __init__ (self,name,breed):
      super().__init__(name)
      self.breed=breed
      
    # def sound(self):
    #     return 'purr'
    
pet1= Dog('oscar','labro')
print(pet1.sound())

pet2= Cat ('lily', 'sphynx')
print(pet2.sound())
