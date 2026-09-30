class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        vote = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                vote += 1
            else:
                vote -= 1

            if vote == 0:
                candidate = nums[i]
                vote += 1
        
        return candidate