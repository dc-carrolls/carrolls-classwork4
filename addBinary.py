
class Solution:
    def __init__(self) -> None:
       self.map1 = {"0":False,"1":True}
       self.map2 = {False:"0",True:"1"}

    def addBinary(self, a, b):
        num1 = a[::-1]
        num2 = b[::-1]
        if len(num1) > len(num2):
          num2 = num2 + (len(num1)-len(num2))*"0"
        else:
          num1 = num1 + (len(num2)-len(num1))*"0"
        #end if
        print(num1, num2)
        ans=""
        c = "0"
        for x,y in zip( num1, num2):
          s,c = self.fullAdder(x,y,c)
          ans += s
        #next x,y
        if c == "1": ans += "1"
        return ans[::-1]

    def fullAdder(self,a,b,c):
      a = self.map1[a]
      b = self.map1[b]
      c = self.map1[c]
      s = a ^ b ^ c
      c = a & b | b & c | a & c
      return self.map2[s],self.map2[c]

      

if __name__ == "__main__":
  x = Solution()
  print(x.addBinary("1001","110"))
  