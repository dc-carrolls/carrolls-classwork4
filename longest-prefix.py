class Solution:
    def longestCommonPrefix(self, strs) -> str:
      str1 = min(strs)
      str2 = max(strs)
      end = False
      i = 0
      while not end and i < min(len(str1),len(str2)):
        if str1[i] != str2[i]:
          end = True
        else:
          i+=1
        #end if
      #end while
      return str1[:i] 
      



x = Solution()
print(x.longestCommonPrefix(["flower","flow","flight"]))