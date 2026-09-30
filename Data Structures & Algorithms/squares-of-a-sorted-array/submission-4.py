class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        print(nums)

        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            if r == l:
                l += 1
                r = len(nums) - 1
            

        return nums