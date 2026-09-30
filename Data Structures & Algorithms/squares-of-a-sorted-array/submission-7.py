class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        
        for i in range(len(res) - 1, -1, -1):
            if nums[l] < nums[r]:
                res[i] = nums[r]
                r -= 1
            else:
                res[i] = nums[l]
                l += 1
        return res