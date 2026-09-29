class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while i < len(haystack):
            if j == len(needle) - 1 and haystack[i] == needle[j]:
                return i - j
            if haystack[i] == needle[j]:
                j += 1
            else:
                i = i - j
                j = 0


            i += 1

        return -1