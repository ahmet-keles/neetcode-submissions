class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 1
        count = 1
        while l < len(nums) - 1:
            if nums[l + 1] > nums[l]:
                count += 1
                res = max(count, res)
            else:
                count = 1
            l += 1
        
        r = len(nums) - 1
        count = 1
        while 0 < r:
            if nums[r - 1] > nums[r]:
                count += 1
                res = max(count, res)
            else:
                count = 1
            r -= 1       

        return res

            