class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            middle = left + (right - left) // 2

            if nums[left] > nums[right] and nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1

            res = min(nums[middle], res)

        
        return res
