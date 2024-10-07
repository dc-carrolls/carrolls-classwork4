class Person:
    def __init__(self, age) -> None:
        self.__age = age #Private
    
    def getAge(self):
        return self.__age


matthew = Person(18)
print(matthew.getAge())
matthew._Person__age = 19
#print(matthew.__age)
print(matthew.getAge())
print(matthew._Person__age)
