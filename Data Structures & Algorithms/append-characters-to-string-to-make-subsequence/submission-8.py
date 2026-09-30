class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr_s = 0
        ptr_t = 0
        res = len(t)
        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                res -= 1
                ptr_t += 1
            ptr_s += 1
        return res
            
            