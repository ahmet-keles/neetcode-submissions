class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1
        for key, value in count.items():
            if key == value:
                res = max(value, res)
        return res