class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 0:
            return l

        while l <= r:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] == val and nums[r] == val:
                r -= 1
            else:
                l += 1
        
        if l == 0 and nums[l] == val:
            nums[l] = -1
            return l

        return r + 1