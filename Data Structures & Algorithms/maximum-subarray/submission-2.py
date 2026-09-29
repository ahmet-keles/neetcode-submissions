class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            res = max(sum, res)
            
        return res