class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        houses = nums
        def helper(houses):
            rob1, rob2 = 0, 0
            for i in range(len(houses)):
                temp = max(houses[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2  
        
        return max(helper(houses[1:]), helper(houses[:-1]))