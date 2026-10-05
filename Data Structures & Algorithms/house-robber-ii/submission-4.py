class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(self, nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2  
        return max(nums[0], helper(self, nums[1:]), helper(self, nums[:-1]))