
class Solution:
    vals = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    def romanToInt(self, s: str) -> int:
        if len(s) == 1: return self.vals[s] 
        elif self.vals[s[0]] < self.vals[s[1]]: return -self.vals[s[0]] + self.romanToInt(s[1:])
        else: return self.vals[s[0]] + self.romanToInt(s[1:])       


    def romanToInt2(self, s: str) -> int:
        vals = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        prev = 0
        total = vals[s[prev]]
        for n in s[1:]:
            if vals[n] <= vals[s[prev]]:
                total += vals[n]
            else:
                total += (vals[n] - 2*vals[s[prev]])
            prev += 1
        return total
    
def conv2roman(num):
    
    
if __name__ = "main":
    main = Solution()
    print(main.romanToInt("MCMLXIV"))
    print(main.romanToInt("MMXXIII"))
