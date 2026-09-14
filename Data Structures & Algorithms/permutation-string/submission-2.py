class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)

        for i in range(len(s1)):
            mp1[s1[i]] += 1

        for i in range(r):
            mp2[s2[i]] += 1
        
        while r < len(s2):
            mp2[s2[r]] += 1
            if mp1 == mp2:
                return True
            else:
                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
                r += 1


        return False
