class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        
        for i in range(len(s)):
            if count_s[s[i]] != count_t[t[i]]:
                return False
            count_s[s[i]] = i + 1
            count_t[t[i]] = i + 1

        return True