import random

class Animal:
    #private age 
    #privare vertebrae

    #public procedure sound

    def __init__(self,vertebrae) -> None:
        self.age = 0                #private
        self.vertebrae = vertebrae  #private
    #end public constructor

    def sound(self):
        pass
    #end public procedure
#end class

class Mammal(Animal):
    def __init__(self, legs) -> None:
        self.legs = legs
        super().__init__(True)
    #end constuctor
#end class


class Cat(Mammal):
    def sound(self):
        print('Meow',end=chr(0x20))
    #end public procdure
#end class

class Dog(Mammal):
    def sound(self):
        print('Woof',end=chr(0x20))
    #end public procedure
#end class


seed_list = [n % 2 for n in range(10)]
random.shuffle(seed_list)
animal_list = []
for seed in seed_list:
    if seed == 1:
        animal_list.append(Cat(4))
    else:
        animal_list.append(Dog(4))
    #end if
#next seed

animal_list.append(Animal(False))

for animal in animal_list:
    animal.sound()
#next animal



