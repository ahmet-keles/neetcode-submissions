class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = 0
        for i in range(0, len(heights)):
            if heights[i] != expected[i]:
                res += 1
        
        return res