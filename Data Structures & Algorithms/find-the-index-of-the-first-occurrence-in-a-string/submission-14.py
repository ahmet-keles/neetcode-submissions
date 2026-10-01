class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = 0
        n = 0

        while h < len(haystack) and n < len(needle):
            if needle[n] == haystack[h]:
                n += 1
            elif n > 0:
                h = h - n
                n = 0
            h += 1
            if n == len(needle):
                return h - n
        
        return -1

        