class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        half_length = len(s) // 2

        while l < r:
            if not s[r].isalnum():
                r -= 1
            elif not s[l].isalnum():
                l += 1
            else:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        
        return True

            