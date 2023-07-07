class Solution:
    def plusOne(self, digits):
      for n in range(len(digits)-1,-1,-1):
        digits[n]=(digits[n]+1)%10
        if digits[n] != 0: break
      if digits[0] == 0: digits.insert(0,1)
      return digits  
    #   pos = len(digits)-1
    #   while pos != -1 and self.addOne(digits,pos):
    #     pos-=1
    #   if pos == -1:
    #     digits.insert(0,1)
    #   return digits

    # def addOne(self, digits, pos) -> bool:
    #   digits[pos] = (digits[pos] + 1) % 10
    #   return digits[pos] == 0


arr = [9]

x = Solution()
print(x.plusOne(arr))