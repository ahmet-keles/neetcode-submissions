class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        temp = 0
        for i in range(len(s)):
            if s[i] in seen:
                temp = max(seen[s[i]] + 1, temp)
            seen[s[i]] = i
            res = max(res, i - temp + 1)
        return res
