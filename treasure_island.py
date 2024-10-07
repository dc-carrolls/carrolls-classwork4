class Treasure:
    age:int = 10
    def __init__(self,value:int,level:str) -> None:
        self.__value = value 
        self.__level = level 
    #end constructor
        
    def getValue(self) -> int:
        return self.__value
    #end function

    def getLevel(self) -> str:
        return self.__level
    #end function

    def setValue(self, value:int) -> None:
        self.__value = value
    #end procedure
        
    def setLevel(self, level:str) -> None:
        self.__level = level
    #end procedure
#end class

goldcup1 = Treasure(None,None)    
Treasure.__init__(goldcup1,500,"Gold")
goldcup2 = Treasure(1000,"Gold")
Treasure.age = 30
print(goldcup1.getValue(),goldcup1.getLevel(),goldcup1.age)
print(goldcup2.getValue(),goldcup2.getLevel(),goldcup2.age)