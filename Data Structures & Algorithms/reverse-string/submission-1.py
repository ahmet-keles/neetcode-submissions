class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        while r >= (len(s) // 2):
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1
        