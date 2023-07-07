class Solution:
    def generate(self, numRows: int):
        output=[[1],[1,1]]
        currRow = 2
        while currRow < numRows:
          currRow+=1
          currList = output[-1]
          newList = [1]
          for i in range(len(currList)-1):
            newList.append(currList[i]+currList[i+1])
          newList.append(1)
          output.append(newList)
        #end while
        return output[:numRows]


if __name__ == "__main__":
  x=Solution()
  print(x.generate(5))
