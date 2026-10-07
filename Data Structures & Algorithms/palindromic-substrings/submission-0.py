class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l = i
            r = i
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                else:
                    break
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                else:
                    break
                l -= 1
                r += 1
        return count
        
                