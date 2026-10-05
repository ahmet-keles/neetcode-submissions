class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_l = 0
        best_r = 0
        for i in range(len(s)):
            l = i
            r = i
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    if (best_r - best_l + 1) < (r - l + 1):
                        best_l = l
                        best_r = r
                else:
                    break
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    if (best_r - best_l + 1) < (r - l + 1):
                        best_l = l
                        best_r = r
                else:
                    break
                l -= 1
                r += 1
        return s[best_l:best_r+1]