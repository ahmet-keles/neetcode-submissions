import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        y = math.gcd(len(str1), len(str2))
        x = str1[:y]
        if x * (len(str1) // y) == str1 and x * (len(str2) // y) == str2:
            return x
        return ""

