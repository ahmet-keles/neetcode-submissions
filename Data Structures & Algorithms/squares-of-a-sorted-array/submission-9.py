class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        
        for i in range(len(res) - 1, -1, -1):
            rs = nums[r] * nums[r]
            ls = nums[l] * nums[l]
            if ls < rs:
                res[i] = rs
                r -= 1
            else:
                res[i] = ls
                l += 1
        return res