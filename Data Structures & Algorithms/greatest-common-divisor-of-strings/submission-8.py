import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            l = str1
            s = str2
        else:
            l = str2
            s = str1
        y = math.gcd(len(s), len(l))
        res = ""
        x = s[:y]
        isEqual = True
        for j in range(0, len(l), len(x)):
            if x != l[j: j + len(x)]:
                isEqual = False
                break
        if isEqual:
            res = x          
                
            
            
        return res

