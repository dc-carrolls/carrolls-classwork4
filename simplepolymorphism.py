import random

class Animal():
    def __init__(self,name) -> None:
        self.name = name
    #end constructor
    
    def sound(self):
        pass
    #end method

    def __str__(self) -> str:
        self.sound()
        return self.name

class Dog(Animal):
    def sound(self):
        print("Woof")
    #end method
#end class
        
class Cat(Animal):
    def sound(self):
        print("Meoow")
    #end method
#end class

animal_list = []    
for n in range(1,21):
    if random.randint(1,2) == 1:
        animal_list.append(Cat("Cat"+str(n)))
    else:
        animal_list.append(Dog("Dog"+str(n)))
    #end if
#next n

for animal in animal_list:
    print(animal)
   # animal.sound()        